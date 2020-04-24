INSERT INTO ref_nomenclatures.bib_nomenclatures_types (id_type, mnemonique, label_fr, label_default, definition_fr, source, statut, meta_create_date, meta_update_date) VALUES
(123, 'JDD_DATA_TYPE', 'Type de jeu de donnéees', 'Type de jeu de donnéees', 'Nomenclature des types de jeux de données', 'SINP', 'Validé', '2020-03-21 00:00:00', '2020-03-21 00:00:00')

INSERT INTO ref_nomenclatures.t_nomenclatures (id_type, cd_nomenclature, mnemonique, label_fr, label_default, definition_fr,  source, statut, id_broader, hierarchy, meta_create_date, meta_update_date, active) VALUES
(ref_nomenclatures.get_id_nomenclature_type('JDD_DATA_TYPE'), 'NR', 'NR', 'Non renseigné', 'Non renseigné', 'Le type de JDD n''est pas renseigné', 'SINP', 'Validé', 0, '123.001', '2020-03-21 00:00:00', '2020-03-21 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('JDD_DATA_TYPE'), 'Hab', 'Hab', 'Habitats', 'Habitats', 'Habitats', 'SINP', 'Validé', 0, '123.002', '2020-03-21 00:00:00', '2020-03-21 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('JDD_DATA_TYPE'), 'Tax', 'Tax', 'Taxons', 'Taxons', 'Taxons', 'SINP', 'Validé', 0, '123.003', '2020-03-21 00:00:00', '2020-03-21 00:00:00', true);

INSERT INTO ref_nomenclatures.defaults_nomenclatures_value (mnemonique_type, id_organism, id_nomenclature) VALUES
('JDD_DATA_TYPE',0,ref_nomenclatures.get_id_nomenclature('JDD_DATA_TYPE', 'NR'));

ALTER TABLE gn_meta.t_datasets add column
id_nomenclature_jdd_data_type integer NOT NULL DEFAULT ref_nomenclatures.get_default_nomenclature_value('JDD_DATA_TYPE');

ALTER TABLE only gn_meta.t_datasets add CONSTRAINT
fk_t_datasets_jdd_data_type FOREIGN KEY (id_nomenclature_jdd_data_type) REFERENCES ref_nomenclatures.t_nomenclatures(id_nomenclature) ON UPDATE CASCADE;
