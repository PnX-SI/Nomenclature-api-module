UPDATE ref_nomenclatures.t_nomenclatures 
SET cd_nomenclature = concat('OLD_', cd_nomenclature)
WHERE id_type = ref_nomenclatures.get_id_nomenclature_type('DATA_TYP');


INSERT INTO ref_nomenclatures.t_nomenclatures (id_type, cd_nomenclature, mnemonique, label_fr, label_default, definition_fr,  source, statut, id_broader, meta_create_date, meta_update_date, active) VALUES
(ref_nomenclatures.get_id_nomenclature_type('DATA_TYP'), 'NR', 'NR', 'Non renseigné', 'Non renseigné', 'Le type de JDD n''est pas renseigné', 'SINP', 'Validé', 0, '2017-12-18 00:00:00', '2017-12-18 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('DATA_TYP'), 'Hab', 'Hab', 'Habitats', 'Habitats', 'Habitats', 'SINP', 'Validé', 0, '2017-12-18 00:00:00', '2017-12-18 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('DATA_TYP'), 'Tax', 'Tax', 'Taxons', 'Taxons', 'Taxons', 'SINP', 'Validé', 0, '2017-12-18 00:00:00', '2017-12-18 00:00:00', true);

DELETE FROM ref_nomenclatures.defaults_nomenclatures_value
WHERE mnemonique_type = 'DATA_TYP';
INSERT INTO ref_nomenclatures.defaults_nomenclatures_value (mnemonique_type, id_organism, id_nomenclature) VALUES
('DATA_TYP',0,ref_nomenclatures.get_id_nomenclature('DATA_TYP', 'NR'));
