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
-- Ajout NSP dans floutage
,(ref_nomenclatures.get_id_nomenclature_type('DEE_FLOU'), 'NSP', 'NSP', 'NSP', 'NSP', 'NSP : Indique qu''on ignore si un floutage a eu lieu.', 'SINP', 'Validé', 0, '2018-05-15 00:00:00', '2018-05-15 00:00:00', true)
-- Ajout méthod obs (renommé technique d'obs)
,(ref_nomenclatures.get_id_nomenclature_type('METH_OBS'), '26', 'Olfactif', 'Olfactif', 'Olfactif', 'Contact olfactif : l''occurrence a été sentie sur le lieu d''observation', 'SINP', 'Validé', 0, '2018-03-15 00:00:00', '2018-03-15 00:00:00', true)
,(ref_nomenclatures.get_id_nomenclature_type('METH_OBS'), '27', 'Empreintes et fèces', 'Empreintes et fèces', 'Empreintes et fèces', 'Empreintes et fèces', 'SINP', 'Validé', 0, '2018-03-15 00:00:00', '2018-03-15 00:00:00', true)
-- ajout stade de vie
,(ref_nomenclatures.get_id_nomenclature_type('STADE_VIE'), '27', 'Fruit', 'Fruit', 'Fruit', 'Fruit : L''individu est sous forme de fruit.', 'SINP', 'Validé', 0, '2018-03-15 00:00:00', '2018-03-15 00:00:00', true)
--ajout statut bio
,(ref_nomenclatures.get_id_nomenclature_type('STATUT_BIO'), '13', 'Végétatif', 'Végétatif', 'Végétatif', 'L''individu est au stade végétatif.', 'SINP', 'Validé', 0, '2018-03-15 00:00:00', '2018-03-15 00:00:00', true)


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

,(ref_nomenclatures.get_id_nomenclature('METH_OBS', '26'), 'all', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('METH_OBS', '27'), 'Animalia', 'all', now(), NULL)
,(ref_nomenclatures.get_id_nomenclature('STADE_VIE', '27'), 'Plantae', 'all', now(), NULL)

,(ref_nomenclatures.get_id_nomenclature('STATUT_BIO', '13'), 'Plantae', 'all', now(), NULL)


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
WHERE (id_type = ref_nomenclatures.get_id_nomenclature_type('STATUT_BIO') AND cd_nomenclature IN ('6', '7', '8', '10', '11', '12'))
OR (id_type = ref_nomenclatures.get_id_nomenclature_type('DS_PUBLIQUE') AND cd_nomenclature IN ('Ac', 'Re'))
;

-- Changement définitions DEE FLOU
UPDATE ref_nomenclatures.t_nomenclatures
SET definition_fr = 'Non : indique qu''aucun floutage n''a eu lieu. Donnée non floutée, fournie précise par le producteur.'
WHERE id_nomenclature = ref_nomenclatures.get_id_nomenclature('DEE_FLOU', 'NON')
;

UPDATE ref_nomenclatures.t_nomenclatures
SET definition_fr = 'Oui : indique qu''un floutage a eu lieu. Floutage effectué par le producteur avant envoi vers le SINP (une plateforme du SINP).'
WHERE id_nomenclature = ref_nomenclatures.get_id_nomenclature('DEE_FLOU', 'OUI')
;

UPDATE ref_nomenclatures.t_nomenclatures
SET definition_fr = 'Observation indirecte : Galerie forée dans le bois, les racines ou les tiges, par des larves (Lépidoptères, Coléoptères, Diptères) ou creusée dans la terre (micro-mammifères, mammifères... ).'
WHERE id_nomenclature = ref_nomenclatures.get_id_nomenclature('METH_OBS', '23')
;


-- Mise à jour des nomenclatures "CA_OBJECTIFS" et mise à jour des données en conséquence (standard métadonnées 1.3.10)
-- Geler les valeurs obsolètes des objectifs du Cadre d'acquisition
UPDATE ref_nomenclatures.t_nomenclatures
SET active=false,
	statut='Gelée', 
	cd_nomenclature='OLD_'||cd_nomenclature										
WHERE id_nomenclature in (
	SELECT n.id_nomenclature
	FROM ref_nomenclatures.t_nomenclatures n
	JOIN ref_nomenclatures.bib_nomenclatures_types t on t.id_type=n.id_type 
	WHERE t.mnemonique='CA_OBJECTIFS');

-- Importer les nouvelles valeurs 
DO $$
DECLARE
	my_id_type INTEGER;
BEGIN
	my_id_type := (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique='CA_OBJECTIFS');

	INSERT INTO ref_nomenclatures.t_nomenclatures (id_type, cd_nomenclature, mnemonique, label_default, definition_default, label_fr, definition_fr, source, statut, id_broader, hierarchy, meta_create_date, meta_update_date, active)
	VALUES
		(my_id_type, '8', 'InvCart', 'Inventaires et cartographie', 'L''acquisition des données d''occurrence est réalisée avec la démarche d''avoir des informations sur la présence/absence ou effectif/abondance (dénombrement…) d''un ou de plusieurs objets de biodiversité. Le dispositif de collecte est établi pour avoir une représentation spatiale de la répartition d''un ou de plusieurs objets de biodiversité à des dates ou des périodes prédéfinies.', 'Inventaires et cartographie', 'L''acquisition des données d''occurrence est réalisée avec la démarche d''avoir des informations sur la présence/absence ou effectif/abondance (dénombrement…) d''un ou de plusieurs objets de biodiversité. Le dispositif de collecte est établi pour avoir une représentation spatiale de la répartition d''un ou de plusieurs objets de biodiversité à des dates ou des périodes prédéfinies.', 'SINP', 'Validé', 0, (select lpad(my_id_type::text,3,'0')||'.'||'008'),now(),now(), true),
		(my_id_type, '9', 'SuivSurv', 'Suivi/surveillance dans le temps', 'L''acquisition des données d''occurrence est réalisée avec un dispositif de collecte comprenant une répétition de l''acquisition au cours du temps. La démarche permet une comparaison d''un état entre différentes périodes pour un ou plusieurs objets de biodiversité. Elle est mise en place en lien avec une thématique prédéterminée (biologie de la conservation, changements globaux, …).', 'Suivi/surveillance dans le temps', 'L''acquisition des données d''occurrence est réalisée avec un dispositif de collecte comprenant une répétition de l''acquisition au cours du temps. La démarche permet une comparaison d''un état entre différentes périodes pour un ou plusieurs objets de biodiversité. Elle est mise en place en lien avec une thématique prédéterminée (biologie de la conservation, changements globaux, …).', 'SINP', 'Validé', 0, (select lpad(my_id_type::text,3,'0')||'.'||'009'),now(),now(), true),
		(my_id_type, '10', 'Exp/Rech', 'Expérimentation/recherche', 'L''acquisition des données est réalisée avec une démarche d''amélioration de la connaissance scientifique ciblée sur une ou plusieurs questions précises (de la description des patrons de biodiversité à l''expérimentation pour expliquer les processus ou démontrer des relations causales de type ''avant/après'' (effet de la gestion, mécanismes etc.)). L''expérimentation et la recherche de type purement ''observationnelle'' ou ''corrélative'' doivent figurer dans les catégories ''inventaires'' ou ''suivis/surveillance''.' , 'Expérimentation/recherche', 'L''acquisition des données est réalisée avec une démarche d''amélioration de la connaissance scientifique ciblée sur une ou plusieurs questions précises (de la description des patrons de biodiversité à l''expérimentation pour expliquer les processus ou démontrer des relations causales de type ''avant/après'' (effet de la gestion, mécanismes etc.)). L''expérimentation et la recherche de type purement ''observationnelle'' ou ''corrélative'' doivent figurer dans les catégories ''inventaires'' ou ''suivis/surveillance''.' , 'SINP', 'Validé', 0, (select lpad(my_id_type::text,3,'0')||'.'||'010'),now(),now(), true),
		(my_id_type, '11', 'MultAutr', 'Multiples ou autres', 'L''acquisition des données est réalisée avec une démarche propre faisant intervenir plusieurs démarches préalablement décrites.', 'Multiples ou autres', 'L''acquisition des données est réalisée avec une démarche propre faisant intervenir plusieurs démarches préalablement décrites.', 'SINP', 'Validé', 0, (select lpad(my_id_type::text,3,'0')||'.'||'011'),now(),now(), true);

END $$;
