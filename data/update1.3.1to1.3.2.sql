UPDATE ref_nomenclatures.t_nomenclatures set mnemonique = 'sig'
WHERE id_nomenclature = (
SELECT id_nomenclature 
FROM ref_nomenclatures.t_nomenclatures
WHERE id_type = ref_nomenclatures.get_id_nomenclature_type('METHOD_CALCUL_SURFACE') AND cd_nomenclature = 'sig');

UPDATE ref_nomenclatures.t_nomenclatures set mnemonique = 'lin'
WHERE id_nomenclature = (
SELECT id_nomenclature 
FROM ref_nomenclatures.t_nomenclatures
WHERE id_type = ref_nomenclatures.get_id_nomenclature_type('METHOD_CALCUL_SURFACE') AND cd_nomenclature = 'lin');
