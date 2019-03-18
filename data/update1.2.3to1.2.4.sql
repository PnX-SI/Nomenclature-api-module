DELETE FROM ref_nomenclatures.cor_taxref_nomenclature tax
WHERE tax.id_nomenclature IN (
SELECT t.id_nomenclature 
FROM ref_nomenclatures.t_nomenclatures t
JOIN ref_nomenclatures.bib_nomenclatures_types bib ON bib.id_type = t.id_type
WHERE bib.mnemonique = 'STATUT_OBS' AND t.cd_nomenclature = 'NSP'
);

UPDATE ref_nomenclatures.t_nomenclatures t 
SET ACTIVE = false 
FROM ref_nomenclatures.bib_nomenclatures_types bib 
WHERE bib.id_type = t.id_type AND bib.mnemonique = 'STATUT_OBS' AND t.cd_nomenclature = 'NSP';

INSERT INTO ref_nomenclatures.t_nomenclatures (id_type, cd_nomenclature, mnemonique, label_default, label_fr, definition_fr,  source, statut, id_broader, hierarchy, meta_create_date, meta_update_date, active) VALUES
(ref_nomenclatures.get_id_nomenclature_type('CONFID'), '1', 'Public', 'Public', 'Public', 'Public : la fiche du site n''est pas confidentielle.', 'SINP', 'Validé', 0, '031.001', '2019-01-04 13:41:33.526915', '2019-01-04 13:41:33.526915', true)
,(ref_nomenclatures.get_id_nomenclature_type('CONFID'), '2', 'Confidentiel', 'Confidentiel', 'Confidentiel', 'Confidentiel : la fiche a un niveau de confidentialité élevé.', 'SINP', 'Validé', 0, '031.002', '2019-01-04 13:41:33.526915', '2019-01-04 13:41:33.526915', true)
,(ref_nomenclatures.get_id_nomenclature_type('SOCIAB'), '1', '1', '1', '1', '1 : Individu qui pousse seul', 'SINP', 'Validé', 0, '072.001', '2019-01-04 13:42:57.088685', '2019-01-04 13:42:57.088685', true)
,(ref_nomenclatures.get_id_nomenclature_type('SOCIAB'), '2', '2', '2', '2', '2 : Individu cespiteux, qui pousse en touffe', 'SINP', 'Validé', 0, '072.002', '2019-01-04 13:42:57.088685', '2019-01-04 13:42:57.088685', true)
,(ref_nomenclatures.get_id_nomenclature_type('SOCIAB'), '3', '3', '3', '3', '3 : Individu qui pousse en groupe formant de petits patchs ou des coussins', 'SINP', 'Validé', 0, '072.003', '2019-01-04 13:42:57.088685', '2019-01-04 13:42:57.088685', true)
,(ref_nomenclatures.get_id_nomenclature_type('SOCIAB'), '4', '4', '4', '4', '4 : Individu qui pousse en colonie formant de grands patchs ou des tapis', 'SINP', 'Validé', 0, '072.004', '2019-01-04 13:42:57.088685', '2019-01-04 13:42:57.088685', true)
,(ref_nomenclatures.get_id_nomenclature_type('SOCIAB'), '5', '5', '5', '5', '5 : Individu qui pousse en grand nombre, population pure, monospécifique', 'SINP', 'Validé', 0, '072.005', '2019-01-04 13:42:57.088685', '2019-01-04 13:42:57.088685', true)
;