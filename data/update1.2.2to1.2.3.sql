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