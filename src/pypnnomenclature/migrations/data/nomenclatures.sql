SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

CREATE SCHEMA ref_nomenclatures;

SET search_path = ref_nomenclatures, pg_catalog, public;

-------------
--FUNCTIONS--
-------------


CREATE OR REPLACE FUNCTION get_id_nomenclature_type(mytype character varying) RETURNS integer
IMMUTABLE
LANGUAGE plpgsql AS
$$
--Function which return the id_type from the mnemonique of a nomenclature type
DECLARE theidtype character varying;
  BEGIN
SELECT INTO theidtype id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = mytype;
return theidtype;
  END;
$$;

CREATE OR REPLACE FUNCTION get_default_nomenclature_value(mytype character varying, myidorganism integer DEFAULT 0) RETURNS integer
IMMUTABLE
LANGUAGE plpgsql AS
$$
--Function that return the default nomenclature id with wanted nomenclature type (mnemonique), organism id
--Return -1 if nothing matches with given parameters
  DECLARE
    thenomenclatureid integer;
  BEGIN
      SELECT INTO thenomenclatureid id_nomenclature
      FROM ref_nomenclatures.defaults_nomenclatures_value
      WHERE mnemonique_type = mytype
      AND (id_organism = myidorganism OR id_organism = 0)
      ORDER BY id_organism DESC LIMIT 1;
    IF (thenomenclatureid IS NOT NULL) THEN
      RETURN thenomenclatureid;
    END IF;
    RETURN -1;
  END;
$$;

CREATE OR REPLACE FUNCTION check_nomenclature_type_by_mnemonique(id integer , mytype character varying) RETURNS boolean
IMMUTABLE
LANGUAGE plpgsql AS
$$
--Function that checks if an id_nomenclature matches with wanted nomenclature type (use mnemonique type)
  BEGIN
    IF (id IN (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE id_type = ref_nomenclatures.get_id_nomenclature_type(mytype))
        OR id IS NULL) THEN
      RETURN true;
    ELSE
	    RAISE EXCEPTION 'Error : id_nomenclature --> (%) and nomenclature --> (%) type didn''t match. Use id_nomenclature in corresponding type (mnemonique field). See ref_nomenclatures.t_nomenclatures.id_type.', id,mytype;
    END IF;
    RETURN false;
  END;
$$;

CREATE OR REPLACE FUNCTION check_nomenclature_type_by_cd_nomenclature(mycdnomenclature character varying , mytype character varying) RETURNS boolean
IMMUTABLE
LANGUAGE plpgsql AS
$$
--Function that checks if an id_nomenclature matches with wanted nomenclature type (use mnemonique type)
  BEGIN
    IF (mycdnomenclature IN (SELECT cd_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE id_type = ref_nomenclatures.get_id_nomenclature_type(mytype))
        OR mycdnomenclature IS NULL) THEN
      RETURN true;
    ELSE
	    RAISE EXCEPTION 'Error : cd_nomenclature --> % and nomenclature type --> % didn''t match.', mycdnomenclature, mytype
	    USING HINT = 'Use cd_nomenclature in corresponding type (mnemonique field). See ref_nomenclatures.t_nomenclatures.id_type and ref_nomenclatures.bib_nomenclatures_types.mnemonique';
    END IF;
    RETURN false;
  END;
$$;

CREATE OR REPLACE FUNCTION check_nomenclature_type_by_id(id integer, myidtype integer) RETURNS boolean
  IMMUTABLE
LANGUAGE plpgsql AS
$$
--Function that checks if an id_nomenclature matches with wanted nomenclature type (use id_type)
  BEGIN
    IF (id IN (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE id_type = myidtype )
        OR id IS NULL) THEN
      RETURN true;
    ELSE
	    RAISE EXCEPTION 'Error : id_nomenclature --> (%) and id_type --> (%) didn''t match. Use nomenclature with corresponding type (id_type). See ref_nomenclatures.t_nomenclatures.id_type and ref_nomenclatures.bib_nomenclatures_types.id_type.', id, myidtype ;
    END IF;
    RETURN false;
  END;
$$;


CREATE OR REPLACE FUNCTION get_id_nomenclature(
    mytype character varying,
    mycdnomenclature character varying)
  RETURNS integer AS
$BODY$
--Function which return the id_nomenclature from an mnemonique_type and an cd_nomenclature
DECLARE theidnomenclature integer;
  BEGIN
SELECT INTO theidnomenclature id_nomenclature
FROM ref_nomenclatures.t_nomenclatures n
WHERE n.id_type = ref_nomenclatures.get_id_nomenclature_type(mytype) AND mycdnomenclature = n.cd_nomenclature;
return theidnomenclature;
  END;
$BODY$
  LANGUAGE plpgsql IMMUTABLE
  COST 100;

CREATE OR REPLACE FUNCTION ref_nomenclatures.get_nomenclature_label(
    myidnomenclature integer DEFAULT NULL::integer,
    mylanguage character varying DEFAULT 'fr'::character varying)
  RETURNS character varying AS
$BODY$
--Function which return the label from the id_nomenclature and the language
DECLARE
	labelfield character varying;
	thelabel character varying;
  BEGIN
  labelfield = 'label_'||mylanguage;
  EXECUTE format( ' SELECT  %s
  FROM ref_nomenclatures.t_nomenclatures n
  WHERE id_nomenclature = $1',labelfield)INTO thelabel USING myidnomenclature;
return thelabel;
  END;
$BODY$
  LANGUAGE plpgsql IMMUTABLE
  COST 100;

CREATE OR REPLACE FUNCTION get_cd_nomenclature(myidnomenclature integer)
  RETURNS character varying AS
$BODY$
--Function which return the cd_nomenclature from an id_nomenclature
DECLARE thecdnomenclature character varying;
  BEGIN
SELECT INTO thecdnomenclature cd_nomenclature
FROM ref_nomenclatures.t_nomenclatures n
WHERE myidnomenclature = n.id_nomenclature;
return thecdnomenclature;
  END;
$BODY$
  LANGUAGE plpgsql IMMUTABLE
  COST 100;

CREATE OR REPLACE FUNCTION ref_nomenclatures.get_nomenclature_label_by_cdnom_mnemonique_and_language(
    mytype character varying,
    mycdnomenclature character varying,
    mylanguage character varying)
  RETURNS character varying AS
$BODY$
--Function which return the label from the cd_nomenclature, the code_type and the language
DECLARE
	labelfield character varying;
	thelabel character varying;
  BEGIN
  labelfield = 'label_'||mylanguage;
  EXECUTE format( ' SELECT  %s
  FROM ref_nomenclatures.t_nomenclatures n
  WHERE cd_nomenclature = $1 AND id_type = ref_nomenclatures.get_id_nomenclature_type($2)',labelfield )INTO thelabel USING mycdnomenclature, mytype;
return thelabel;
  END;
$BODY$
  LANGUAGE plpgsql IMMUTABLE
  COST 100;

CREATE OR REPLACE FUNCTION get_nomenclature_label_by_cdnom_mnemonique(
    mytype character varying,
    mycdnomenclature character varying)
  RETURNS character varying AS
$BODY$
--Function which return the label from the id_nomenclature and the language
DECLARE
	labelfield character varying;
	thelabel character varying;
  BEGIN
  EXECUTE format( ' SELECT  label_default
  FROM ref_nomenclatures.t_nomenclatures n
  WHERE cd_nomenclature = $1 AND id_type = ref_nomenclatures.get_id_nomenclature_type($2)' )INTO thelabel USING mycdnomenclature, mytype;
return thelabel;
  END;
$BODY$
  LANGUAGE plpgsql IMMUTABLE
  COST 100;

----------
--TABLES--
----------

CREATE TABLE bib_nomenclatures_types (
    id_type integer NOT NULL,
    mnemonique character varying(255),
    label_default character varying(255),
    definition_default text,
    label_fr character varying(255),
    definition_fr text,
    label_en character varying(255),
    definition_en text,
    label_es character varying(255),
    definition_es text,
    label_de character varying(255),
    definition_de text,
    label_it character varying(255),
    definition_it text,
    source character varying(50),
    statut character varying(20),
    meta_create_date timestamp without time zone DEFAULT now(),
    meta_update_date timestamp without time zone DEFAULT now()
);
COMMENT ON TABLE bib_nomenclatures_types IS 'Types of nomenclature (SINP, CAMPanule, GeoNature...)';

CREATE SEQUENCE bib_nomenclatures_types_id_type_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE bib_nomenclatures_types_id_type_seq OWNED BY bib_nomenclatures_types.id_type;
ALTER TABLE ONLY bib_nomenclatures_types ALTER COLUMN id_type SET DEFAULT nextval('bib_nomenclatures_types_id_type_seq'::regclass);


CREATE TABLE t_nomenclatures (
    id_nomenclature integer NOT NULL,
    id_type integer NOT NULL,
    cd_nomenclature character varying(255) NOT NULL,
    mnemonique character varying(255),
    label_default character varying(255),
    definition_default text,
    label_fr character varying(255),
    definition_fr text,
    label_en character varying(255),
    definition_en text,
    label_es character varying(255),
    definition_es text,
    label_de character varying(255),
    definition_de text,
    label_it character varying(255),
    definition_it text,
    source character varying(50),
    statut character varying(20),
    id_broader integer,
    hierarchy character varying(255),
    meta_create_date timestamp without time zone DEFAULT now(),
    meta_update_date timestamp without time zone,
    active boolean NOT NULL DEFAULT true
);
CREATE SEQUENCE t_nomenclatures_id_nomenclature_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE t_nomenclatures_id_nomenclature_seq OWNED BY t_nomenclatures.id_nomenclature;
ALTER TABLE ONLY t_nomenclatures ALTER COLUMN id_nomenclature SET DEFAULT nextval('t_nomenclatures_id_nomenclature_seq'::regclass);

CREATE TABLE cor_nomenclatures_relations (
    id_nomenclature_l integer NOT NULL,
    id_nomenclature_r integer NOT NULL,
    relation_type character varying(250) NOT NULL
);


CREATE TABLE defaults_nomenclatures_value (
    mnemonique_type character varying(255) NOT NULL,
    id_organism integer NOT NULL,
    id_nomenclature integer NOT NULL
);


CREATE TABLE cor_application_nomenclature
(
  id_nomenclature integer NOT NULL,
  id_application integer NOT NULL
);
COMMENT ON TABLE cor_application_nomenclature
  IS 'Allow to create specific list per module for one nomenclature.';

---------------
--PRIMARY KEY--
---------------

ALTER TABLE ONLY cor_nomenclatures_relations
    ADD CONSTRAINT pk_cor_nomenclatures_relations PRIMARY KEY (id_nomenclature_l, id_nomenclature_r, relation_type);

ALTER TABLE ONLY bib_nomenclatures_types
    ADD CONSTRAINT pk_bib_nomenclatures_types PRIMARY KEY (id_type);

ALTER TABLE ONLY t_nomenclatures
    ADD CONSTRAINT pk_t_nomenclatures PRIMARY KEY (id_nomenclature);

ALTER TABLE ONLY defaults_nomenclatures_value
    ADD CONSTRAINT pk_defaults_nomenclatures_value PRIMARY KEY (mnemonique_type, id_organism);

ALTER TABLE ONLY cor_application_nomenclature
  ADD CONSTRAINT pk_cor_application_nomenclature PRIMARY KEY (id_nomenclature, id_application);


--------------
--CONSTRAINS--
--------------

ALTER TABLE bib_nomenclatures_types
  ADD CONSTRAINT unique_bib_nomenclatures_types_mnemonique UNIQUE (mnemonique);

ALTER TABLE ONLY defaults_nomenclatures_value
    ADD CONSTRAINT check_defaults_nomenclatures_value_is_nomenclature_in_type CHECK (check_nomenclature_type_by_mnemonique(id_nomenclature, mnemonique_type)) NOT VALID;

ALTER TABLE t_nomenclatures
  ADD CONSTRAINT unique_id_type_cd_nomenclature UNIQUE (id_type, cd_nomenclature);

---------------
--FOREIGN KEY--
---------------

ALTER TABLE ONLY cor_nomenclatures_relations
    ADD CONSTRAINT fk_cor_nomenclatures_relations_id_nomenclature_l FOREIGN KEY (id_nomenclature_l) REFERENCES t_nomenclatures(id_nomenclature);

ALTER TABLE ONLY cor_nomenclatures_relations
    ADD CONSTRAINT fk_cor_nomenclatures_relations_id_nomenclature_r FOREIGN KEY (id_nomenclature_r) REFERENCES t_nomenclatures(id_nomenclature);

ALTER TABLE ONLY t_nomenclatures
    ADD CONSTRAINT fk_t_nomenclatures_id_broader FOREIGN KEY (id_broader) REFERENCES t_nomenclatures(id_nomenclature);

ALTER TABLE ONLY t_nomenclatures
    ADD CONSTRAINT fk_t_nomenclatures_id_type FOREIGN KEY (id_type) REFERENCES bib_nomenclatures_types(id_type) ON UPDATE CASCADE;

ALTER TABLE ONLY defaults_nomenclatures_value
    ADD CONSTRAINT fk_defaults_nomenclatures_value_mnemonique_type FOREIGN KEY (mnemonique_type) REFERENCES bib_nomenclatures_types(mnemonique) ON UPDATE CASCADE;

ALTER TABLE ONLY defaults_nomenclatures_value
    ADD CONSTRAINT fk_defaults_nomenclatures_value_id_organism FOREIGN KEY (id_organism) REFERENCES utilisateurs.bib_organismes(id_organisme) ON UPDATE CASCADE;

ALTER TABLE ONLY defaults_nomenclatures_value
    ADD CONSTRAINT fk_defaults_nomenclatures_value_id_nomenclature FOREIGN KEY (id_nomenclature) REFERENCES t_nomenclatures(id_nomenclature) ON UPDATE CASCADE;

ALTER TABLE ONLY cor_application_nomenclature
  ADD CONSTRAINT fk_cor_application_nomenclature_id_nomenclature FOREIGN KEY (id_nomenclature) REFERENCES ref_nomenclatures.t_nomenclatures (id_nomenclature) MATCH SIMPLE ON UPDATE CASCADE ON DELETE NO ACTION;

ALTER TABLE ONLY cor_application_nomenclature ADD CONSTRAINT fk_cor_application_nomenclature_id_application FOREIGN KEY (id_application) REFERENCES utilisateurs.t_applications (id_application) MATCH SIMPLE ON UPDATE CASCADE ON DELETE NO ACTION;


---------
--INDEX--
---------

CREATE INDEX index_t_nomenclatures_bib_nomenclatures_types_fkey ON t_nomenclatures USING btree (id_type);

------------
--TRIGGERS--
------------

CREATE TRIGGER tri_meta_dates_change_bib_nomenclatures_types
  BEFORE INSERT OR UPDATE
  ON bib_nomenclatures_types
  FOR EACH ROW
  EXECUTE PROCEDURE public.fct_trg_meta_dates_change();

CREATE TRIGGER tri_meta_dates_change_t_nomenclatures
  BEFORE INSERT OR UPDATE
  ON t_nomenclatures
  FOR EACH ROW
  EXECUTE PROCEDURE public.fct_trg_meta_dates_change();
