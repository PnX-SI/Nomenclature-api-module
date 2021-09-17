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

CREATE OR REPLACE FUNCTION calculate_sensitivity(
    mycdnom integer,
    mynomenclatureid integer)
  RETURNS integer AS
$BODY$
  --Function to return id_nomenclature depending on observation sensitivity
  --USAGE : SELECT ref_nomenclatures.calculate_sensitivity(240,21);
  DECLARE
  sensitivityid integer;
  BEGIN
    SELECT max(id_nomenclature_niv_precis) INTO sensitivityid
    FROM ref_nomenclatures.cor_taxref_sensitivity
    WHERE cd_nom = mycdnom
    AND (id_nomenclature = mynomenclatureid OR id_nomenclature = 0);
  IF sensitivityid IS NULL THEN
    sensitivityid = ref_nomenclatures.get_id_nomenclature('NIV_PRECIS', '5');
  END IF;
  RETURN sensitivityid;
  END;
$BODY$
  LANGUAGE plpgsql IMMUTABLE
  COST 100;


----------
--TABLES--
----------

CREATE TABLE cor_taxref_sensitivity
(
  cd_nom integer NOT NULL,
  id_nomenclature_niv_precis integer NOT NULL,
  id_nomenclature integer NOT NULL,
  sensitivity_duration integer NOT NULL,
  sensitivity_territory character varying(50),
  meta_create_date timestamp without time zone DEFAULT now(),
  meta_update_date timestamp without time zone
);


---------------
--PRIMARY KEY--
---------------

ALTER TABLE ONLY cor_taxref_sensitivity
    ADD CONSTRAINT pk_cor_taxref_sensitivity PRIMARY KEY (cd_nom, id_nomenclature_niv_precis, id_nomenclature);


--------------
--CONSTRAINS--
--------------

ALTER TABLE ONLY cor_taxref_sensitivity
    ADD CONSTRAINT check_cor_taxref_sensitivity_niv_precis CHECK (check_nomenclature_type_by_mnemonique(id_nomenclature_niv_precis,'NIV_PRECIS')) NOT VALID;


---------------
--FOREIGN KEY--
---------------

ALTER TABLE ONLY cor_taxref_sensitivity
    ADD CONSTRAINT fk_cor_taxref_sensitivity_cd_nom FOREIGN KEY (cd_nom) REFERENCES taxonomie.taxref(cd_nom) ON UPDATE CASCADE;

ALTER TABLE ONLY cor_taxref_sensitivity
    ADD CONSTRAINT fk_cor_taxref_sensitivity_niv_precis FOREIGN KEY (id_nomenclature_niv_precis) REFERENCES t_nomenclatures(id_nomenclature) ON UPDATE CASCADE;

ALTER TABLE ONLY cor_taxref_sensitivity
    ADD CONSTRAINT fk_cor_taxref_sensitivity_id_nomenclature FOREIGN KEY (id_nomenclature) REFERENCES t_nomenclatures(id_nomenclature) ON UPDATE CASCADE;


------------
--TRIGGERS--
------------

CREATE TRIGGER tri_meta_dates_change_cor_taxref_sensitivity
  BEFORE INSERT OR UPDATE
  ON cor_taxref_sensitivity
  FOR EACH ROW
  EXECUTE PROCEDURE public.fct_trg_meta_dates_change();

