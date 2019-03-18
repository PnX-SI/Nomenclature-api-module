UPDATE ref_nomenclatures.t_nomenclatures t 
SET ACTIVE = false 
FROM ref_nomenclatures.bib_nomenclatures_types bib 
WHERE bib.id_type = t.id_type AND bib.mnemonique = 'STATUT_OBS' AND t.cd_nomenclature = 'NSP';