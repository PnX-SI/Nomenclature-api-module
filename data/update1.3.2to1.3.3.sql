-- Suppression des relations avec group2_inpn "fougère" supprimé
DELETE FROM ref_nomenclatures.cor_taxref_nomenclature WHERE group2_inpn = 'Fougères';

-- Geler et desactiver les anciennes nomenclatures du type 'DATA_TYP'
UPDATE ref_nomenclatures.t_nomenclatures 
SET cd_nomenclature = concat('OLD_', cd_nomenclature),
active=false,
statut='Gelé'
WHERE id_type = ref_nomenclatures.get_id_nomenclature_type('DATA_TYP');

-- Insérer les nouvelles nomenclatures du type 'DATA_TYP'
INSERT INTO ref_nomenclatures.t_nomenclatures (id_type, cd_nomenclature, mnemonique, label_fr, label_default, definition_fr,  source, statut, id_broader, meta_create_date, meta_update_date, active) VALUES
(ref_nomenclatures.get_id_nomenclature_type('DATA_TYP'), '1', 'Occtax','Occurrences de Taxons', 'Occurrences de Taxons', 'Occurrences de Taxons', 'SINP', 'Validé', 0, '2017-12-18 00:00:00', '2017-12-18 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('DATA_TYP'), '2', 'Occhab','Occurrences d''habitats', 'Occurrences d''habitats', 'Occurrences d''habitats', 'SINP', 'Validé', 0, '2017-12-18 00:00:00', '2017-12-18 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('DATA_TYP'), '3', 'Syntax', 'Syntax','Synthèse de taxons', 'Synthèse de taxons', 'SINP', 'Validé', 0, '2017-12-18 00:00:00', '2017-12-18 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('DATA_TYP'), '4', 'Synhab', 'Synhab','Synthese d''habitats', 'Synthese d''habitats', 'SINP', 'Validé', 0, '2017-12-18 00:00:00', '2017-12-18 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('DATA_TYP'), '5', 'NR','Non renseigné', 'Non renseigné', 'Non reseigné', 'SINP', 'Validé', 0, '2017-12-18 00:00:00', '2017-12-18 00:00:00', true)
;

-- Supprimer l'ancienne valeur par défaut du type de nomenclature 'DATA_TYP'
DELETE FROM ref_nomenclatures.defaults_nomenclatures_value
WHERE mnemonique_type = 'DATA_TYP';
-- Insérer la nouvelle valeur par défaut du type de nomenclature 'DATA_TYP'
INSERT INTO ref_nomenclatures.defaults_nomenclatures_value (mnemonique_type, id_organism, id_nomenclature) VALUES
('DATA_TYP',0,ref_nomenclatures.get_id_nomenclature('DATA_TYP', '5'));

-- Correction de définitions SINP
UPDATE ref_nomenclatures.bib_nomenclatures_types
SET definition_fr = 'Nomenclature des techniques de collectes ayant présidé à l''obtention de l''information sur l''habitat'
WHERE mnemonique = 'TECHNIQUE_COLLECT_HAB';
UPDATE ref_nomenclatures.bib_nomenclatures_types
SET definition_fr = 'Nomenclature des coefficients de Braun-Blanquet et Pavillard adaptés pour décrire l''abondance relative des habitats au sein d''une station'
WHERE mnemonique = 'ABONDANCE_HAB';
UPDATE ref_nomenclatures.bib_nomenclatures_types
SET definition_fr = 'Nomenclature des valeurs permettant d''indiquer si un habitat est d''intérêt communautaire'
WHERE mnemonique = 'HAB_INTERET_COM';
UPDATE ref_nomenclatures.bib_nomenclatures_types
SET definition_fr = 'Nomenclature des types de détermination d''une surface'
WHERE mnemonique = 'METHOD_CALCUL_SURFACE';
