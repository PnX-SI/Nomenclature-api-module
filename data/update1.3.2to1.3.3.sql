UPDATE ref_nomenclatures.t_nomenclatures 
SET cd_nomenclature = concat('OLD_', cd_nomenclature),
active=false,
statut='Gelé'
WHERE id_type = ref_nomenclatures.get_id_nomenclature_type('DATA_TYP');


INSERT INTO ref_nomenclatures.t_nomenclatures (id_type, cd_nomenclature, mnemonique, label_fr, label_default, definition_fr,  source, statut, id_broader, meta_create_date, meta_update_date, active) VALUES
(ref_nomenclatures.get_id_nomenclature_type('DATA_TYP'), '1', 'Occtax','Occurrences de Taxons', 'Occurrences de Taxons', 'Occurrences de Taxons', 'SINP', 'Validé', 0, '2017-12-18 00:00:00', '2017-12-18 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('DATA_TYP'), '2', 'Occhab','Occurrences d''habitats', 'Occurrences d''habitats', 'Occurrences d''habitats', 'SINP', 'Validé', 0, '2017-12-18 00:00:00', '2017-12-18 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('DATA_TYP'), '3', 'Syntax', 'Syntax','Synthèse de taxons', 'Synthèse de taxons', 'SINP', 'Validé', 0, '2017-12-18 00:00:00', '2017-12-18 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('DATA_TYP'), '4', 'Synhab', 'Synhab','Synthese d''habitats', 'Synthese d''habitats', 'SINP', 'Validé', 0, '2017-12-18 00:00:00', '2017-12-18 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('DATA_TYP'), '5', 'NR','Non reseigné', 'Non renseigné', 'Non reseigné', 'SINP', 'Validé', 0, '2017-12-18 00:00:00', '2017-12-18 00:00:00', true)
;


DELETE FROM ref_nomenclatures.defaults_nomenclatures_value
WHERE mnemonique_type = 'DATA_TYP';
INSERT INTO ref_nomenclatures.defaults_nomenclatures_value (mnemonique_type, id_organism, id_nomenclature) VALUES
('DATA_TYP',0,ref_nomenclatures.get_id_nomenclature('DATA_TYP', '5'));
