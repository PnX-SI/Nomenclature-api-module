INSERT INTO ref_nomenclatures.bib_nomenclatures_types (mnemonique, label_fr, label_default, definition_fr, source, statut, meta_create_date, meta_update_date) VALUES
('OCC_COMPORTEMENT', 'Comportement des occurrences observées', 'Comportement des occurrences observées', 'Nomenclature des domportement des occurrences observées', 'SINP', 'Validé', '2018-05-09 00:00:00', '2018-05-09 00:00:00');
  
INSERT INTO ref_nomenclatures.t_nomenclatures (id_type, cd_nomenclature, mnemonique, label_fr, label_default, definition_fr,  source, statut, id_broader, meta_create_date, meta_update_date, active) VALUES
(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '0', 'NSP', 'Inconnu', 'Inconnu', 'Inconnu : Le statut biologique de l''individu n''est pas connu.', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '1', '1', 'Non renseigné', 'Non renseigné', 'Non renseigné : Le statut biologique de l''individu n''a pas été renseigné.', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '2', '2', 'Echouage', 'Echouage', 'Echouage : l''individu tente de s''échouer ou vient de s''échouer sur le rivage', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '3', '3', 'Dortoir', 'Dortoir', 'Dortoir : individus se regroupant dans une zone définie pour y passer la nuit ou la journée.', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '4', '4', 'Migration', 'Migration', 'Migration : L''individu (ou groupe d''individus) est en migration active', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '5', '5', 'Construction de toile', 'Construction de toile', 'Construction de toile : l''individu construit sa toile', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '6', '6', 'Halte migratoire', 'Halte migratoire', 'Halte migratoire : Indique que l''individu procède à une halte au cours de sa migration, et a été découvert sur sa zone de halte.', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '7', '7', 'Swarming', 'Swarming', 'Swarming : Indique que l''individu a un comportement de swarming : il se regroupe avec d''autres individus de taille similaire, sur une zone spécifique, ou en mouvement.', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '8', 'ChassAlim', 'Chasse/alimentation', 'Chasse/alimentation', 'Chasse / alimentation : Indique que l''individu est sur une zone qui lui permet de chasser ou de s''alimenter.', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '9', 'Hivernage', 'Hivernage', 'Hivernage', 'Hivernage : l''individu hiverne (modification de son comportement liée à l''hiver pouvant par exemple comporter un changement de lieu, d''alimentation, de production de sève ou de graisse...)', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '10', '10', 'Passage en vol', 'Passage en vol', 'Passage en vol : Indique que l''individu est de passage et en vol.', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '11', '11', 'Erratique', 'Erratique', 'Erratique : Individu d''une ou de populations d''un taxon qui ne se trouve, actuellement, que de manière occasionnelle dans les limites d’une région. Il a été retenu comme seuil, une absence de 80% d''un laps de temps donné (année, saisons...).', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '12', '12', 'Sédentaire', 'Sédentaire', 'Sédentaire : Individu demeurant à un seul emplacement, ou restant toute l''année dans sa région d''origine, même s''il effectue des déplacements locaux.', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '13', '13', 'Estivage', 'Estivage', 'Estivage : l''individu estive (modification de son comportement liée à l''été pouvant par exemple comporter un changement de lieu, d''alimentation, de production de sève ou de graisse...)', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '14', '14', 'Nourrissage des jeunes', 'Nourrissage des jeunes', 'Nourrissage des jeunes', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '15', '15', 'Posé', 'Posé', 'Posé : Individu(s) posé(s)', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '16', '16', 'Déplacement', 'Déplacement', 'Déplacement : Individu(s) en déplacement', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '17', '17', 'Repos', 'Repos', 'Repos', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '18', '18', 'Chant', 'Chant', 'Chant', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '19', '19', 'Accouplement', 'Accouplement', 'Accouplement', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '20', '20', 'Cœur copulatoire', 'Cœur copulatoire', 'Cœur copulatoire', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '21', '21', 'Tandem', 'Tandem', 'Tandem', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '22', '22', 'Territorial', 'Territorial', 'Territorial', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('OCC_COMPORTEMENT'), '23', '23', 'Pond', 'Pond', 'Pond', 'SINP', 'Validé', 0, '2018-05-09 00:00:00', '2018-05-09 00:00:00', true)
;

INSERT INTO ref_nomenclatures.cor_taxref_nomenclature VALUES
(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '0'), 'all', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '1'), 'all', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '2'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '3'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '4'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '5'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '6'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '7'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '8'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '9'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '10'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '11'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '12'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '13'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '14'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '15'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '16'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '18'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '19'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '20'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '21'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '22'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('OCC_COMPORTEMENT', '23'), 'Animalia', 'all', now(), NULL)
;


-- Suppression des nomenclature dans cor_taxref qui on été gelée
DELETE FROM ref_nomenclatures.cor_taxref_nomenclature
WHERE id_nomenclature IN (
  SELECT id_nomenclature
  FROM ref_nomenclatures.t_nomenclatures
  WHERE id_type = ref_nomenclatures.get_id_nomenclature_type('STATUT_BIO')
AND cd_nomenclature IN ('6', '7', '8', '10', '11', '12')
);

-- gel de certaines nomenclatures 
UPDATE ref_nomenclatures.t_nomenclatures 
SET 
  cd_nomenclature = concat('OLD_', cd_nomenclature),
  active=false,
  statut='Gelé'
WHERE id_type = ref_nomenclatures.get_id_nomenclature_type('STATUT_BIO')
AND cd_nomenclature IN ('6', '7', '8', '10', '11', '12')
;