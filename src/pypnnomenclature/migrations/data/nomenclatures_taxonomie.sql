SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = ref_nomenclatures, pg_catalog, public;

-------------
--FUNCTIONS--
-------------

CREATE FUNCTION get_filtered_nomenclature(mytype character varying, myregne character varying, mygroup character varying) RETURNS SETOF integer
IMMUTABLE
LANGUAGE plpgsql AS
$$
--Function that returns a list of id_nomenclature depending on regne and/or group2_inpn sent with parameters.
  DECLARE
    thegroup character varying(255);
    theregne character varying(255);
    r integer;

BEGIN
  thegroup = NULL;
  theregne = NULL;

  IF mygroup IS NOT NULL THEN
      SELECT INTO thegroup DISTINCT group2_inpn
      FROM ref_nomenclatures.cor_taxref_nomenclature ctn
      JOIN ref_nomenclatures.t_nomenclatures n ON n.id_nomenclature = ctn.id_nomenclature
      WHERE n.id_type = ref_nomenclatures.get_id_nomenclature_type(mytype)
      AND group2_inpn = mygroup;
  END IF;

  IF myregne IS NOT NULL THEN
    SELECT INTO theregne DISTINCT regne
    FROM ref_nomenclatures.cor_taxref_nomenclature ctn
    JOIN ref_nomenclatures.t_nomenclatures n ON n.id_nomenclature = ctn.id_nomenclature
    WHERE n.id_type = ref_nomenclatures.get_id_nomenclature_type(mytype)
    AND regne = myregne;
  END IF;

  IF theregne IS NOT NULL THEN
    IF thegroup IS NOT NULL THEN
      FOR r IN
        SELECT DISTINCT ctn.id_nomenclature
        FROM taxonomie.cor_taxref_nomenclature ctn
        JOIN ref_nomenclatures.t_nomenclatures n ON n.id_nomenclature = ctn.id_nomenclature
        WHERE n.id_type = ref_nomenclatures.get_id_nomenclature_type(mytype)
        AND regne = theregne
        AND group2_inpn = mygroup
      LOOP
        RETURN NEXT r;
      END LOOP;
      RETURN;
    ELSE
      FOR r IN
        SELECT DISTINCT ctn.id_nomenclature
        FROM taxonomie.cor_taxref_nomenclature ctn
        JOIN ref_nomenclatures.t_nomenclatures n ON n.id_nomenclature = ctn.id_nomenclature
        WHERE n.id_type = ref_nomenclatures.get_id_nomenclature_type(mytype)
        AND regne = theregne
      LOOP
        RETURN NEXT r;
      END LOOP;
      RETURN;
    END IF;
  ELSE
    FOR r IN
      SELECT DISTINCT ctn.id_nomenclature
      FROM taxonomie.cor_taxref_nomenclature ctn
      JOIN ref_nomenclatures.t_nomenclatures n ON n.id_nomenclature = ctn.id_nomenclature
      WHERE n.id_type = ref_nomenclatures.get_id_nomenclature_type(mytype)
    LOOP
      RETURN NEXT r;
    END LOOP;
    RETURN;
  END IF;
END;
$$;



----------
--TABLES--
----------

CREATE TABLE cor_taxref_nomenclature
(
  id_nomenclature integer NOT NULL,
  regne character varying(255) NOT NULL,
  group2_inpn character varying(255) NOT NULL,
  meta_create_date timestamp without time zone DEFAULT now(),
  meta_update_date timestamp without time zone
);


---------------
--PRIMARY KEY--
---------------
ALTER TABLE ONLY cor_taxref_nomenclature
    ADD CONSTRAINT pk_cor_taxref_nomenclature PRIMARY KEY (id_nomenclature, regne, group2_inpn);


--------------
--CONSTRAINS--
--------------
ALTER TABLE ONLY cor_taxref_nomenclature
    ADD CONSTRAINT check_cor_taxref_nomenclature_isgroup2inpn CHECK (taxonomie.check_is_group2inpn(group2_inpn::text) OR group2_inpn::text = 'all'::text) NOT VALID;

ALTER TABLE ONLY cor_taxref_nomenclature
    ADD CONSTRAINT check_cor_taxref_nomenclature_isregne CHECK (taxonomie.check_is_regne(regne::text) OR regne::text = 'all'::text) NOT VALID;


---------------
--FOREIGN KEY--
---------------

ALTER TABLE ONLY cor_taxref_nomenclature
    ADD CONSTRAINT fk_cor_taxref_nomenclature_id_nomenclature FOREIGN KEY (id_nomenclature) REFERENCES t_nomenclatures(id_nomenclature) ON UPDATE CASCADE;


---------
--VIEWS--
---------
CREATE OR REPLACE VIEW v_nomenclature_taxonomie AS
  SELECT tn.id_type,
    tn.label_default AS type_label,
    tn.definition_default AS type_definition,
    tn.label_fr AS type_label_fr,
    tn.definition_fr AS type_definition_fr,
    tn.label_en AS type_label_en,
    tn.definition_en AS type_definition_en,
    tn.label_es AS type_label_es,
    tn.definition_es AS type_definition_es,
    tn.label_de AS type_label_de,
    tn.definition_de AS type_definition_de,
    tn.label_it AS type_label_it,
    tn.definition_it AS type_definition_it,
    ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS nomenclature_label,
    n.definition_default AS nomenclature_definition,
    n.label_fr AS nomenclature_label_fr,
    n.definition_fr AS nomenclature_definition_fr,
    n.label_en AS nomenclature_label_en,
    n.definition_en AS nomenclature_definition_en,
    n.label_es AS nomenclature_label_es,
    n.definition_es AS nomenclature_definition_es,
    n.label_de AS nomenclature_label_de,
    n.definition_de AS nomenclature_definition_de,
    n.label_it AS nomenclature_label_it,
    n.definition_it AS nomenclature_definition_it,
    n.id_broader,
    n.hierarchy
  FROM ref_nomenclatures.t_nomenclatures n
    JOIN ref_nomenclatures.bib_nomenclatures_types tn ON tn.id_type = n.id_type
    JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
  WHERE n.active = true
  ORDER BY tn.id_type, ctn.regne, ctn.group2_inpn, n.id_nomenclature;

CREATE OR REPLACE VIEW v_technique_obs AS(
SELECT ctn.regne,ctn.group2_inpn, n.id_nomenclature, n.mnemonique, n.label_default AS label, n.definition_default AS definition, n.id_broader, n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
WHERE n.mnemonique = 'TECHNIQUE_OBS'
);
--USAGE :
--SELECT * FROM ref_nomenclatures.v_technique_obs WHERE group2_inpn = 'Oiseaux';
--SELECT * FROM ref_nomenclatures.v_technique_obs WHERE regne = 'Plantae';

CREATE OR REPLACE VIEW v_eta_bio AS
SELECT
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'ETA_BIO'
AND n.active = true;

CREATE OR REPLACE VIEW v_stade_vie AS
SELECT
    ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'STADE_VIE'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_stade_vie WHERE (regne = 'Animalia' OR regne = 'all') AND (group2_inpn = 'Amphibiens' OR group2_inpn = 'all');

CREATE OR REPLACE VIEW v_sexe AS
SELECT ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'SEXE'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_sexe WHERE (regne = 'Animalia' OR regne = 'all') AND (group2_inpn = 'Amphibiens' OR group2_inpn = 'all');

CREATE OR REPLACE VIEW v_objet_denbr AS
SELECT ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'OBJ_DENBR'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_objet_denbr WHERE (regne = 'Animalia' OR regne = 'all') AND (group2_inpn = 'Amphibiens' OR group2_inpn = 'all');

CREATE OR REPLACE VIEW v_type_denbr AS
SELECT ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'TYP_DENBR'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_type_denbr WHERE (regne = 'Animalia' OR regne = 'all') AND (group2_inpn = 'Amphibiens' OR group2_inpn = 'all');

CREATE OR REPLACE VIEW v_meth_obs AS
SELECT ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'METH_OBS'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_meth_obs WHERE (regne = 'Animalia' OR regne = 'all') AND (group2_inpn = 'Amphibiens' OR group2_inpn = 'all');

CREATE OR REPLACE VIEW v_statut_bio AS
SELECT ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'STATUT_BIO'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_statut_bio WHERE (regne = 'Animalia' OR regne = 'all') AND (group2_inpn = 'Amphibiens' OR group2_inpn = 'all');

CREATE OR REPLACE VIEW v_naturalite AS
SELECT ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'NATURALITE'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_naturalite WHERE (regne = 'Animalia' OR regne = 'all');

CREATE OR REPLACE VIEW v_preuve_exist AS
 SELECT ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
   FROM ref_nomenclatures.t_nomenclatures n
     LEFT JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
  WHERE n.mnemonique = 'PREUVE_EXIST'
  AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_preuve_exist;

CREATE OR REPLACE VIEW v_statut_obs AS
SELECT ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'STATUT_OBS'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_statut_obs;

CREATE OR REPLACE VIEW v_statut_valid AS
SELECT ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'STATUT_VALID'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_statut_valid;

CREATE OR REPLACE VIEW v_niv_precis AS
SELECT ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'NIV_PRECIS'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_niv_precis;

CREATE OR REPLACE VIEW v_resource_typ AS
SELECT
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'RESOURCE_TYP'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_resource_typ;

CREATE OR REPLACE VIEW v_data_typ AS
SELECT
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'DATA_TYP'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_data_typ;

CREATE OR REPLACE VIEW v_sampling_plan_typ AS
SELECT
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'SAMPLING_PLAN_TYP'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_sampling_plan_typ;

CREATE OR REPLACE VIEW v_sampling_units_typ AS
SELECT
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'SAMPLING_UNITS_TYP'
AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_sampling_units_typ;

CREATE OR REPLACE VIEW v_meth_determin AS
SELECT ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS label,
    n.definition_default AS definition,
    n.id_broader,
    n.hierarchy
FROM ref_nomenclatures.t_nomenclatures n
LEFT JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
LEFT JOIN ref_nomenclatures.bib_nomenclatures_types t ON t.id_type = n.id_type
WHERE t.mnemonique = 'METH_DETERMIN'
  AND n.active = true;
--USAGE :
--SELECT * FROM ref_nomenclatures.v_meth_determin;

------------
--TRIGGERS--
------------

CREATE TRIGGER tri_meta_dates_change_cor_taxref_nomenclature
  BEFORE INSERT OR UPDATE
  ON cor_taxref_nomenclature
  FOR EACH ROW
  EXECUTE PROCEDURE public.fct_trg_meta_dates_change();
