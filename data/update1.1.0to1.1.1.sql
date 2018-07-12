CREATE OR REPLACE FUNCTION ref_nomenclatures.get_nomenclature_label_by_cdnom_mnemonique(
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