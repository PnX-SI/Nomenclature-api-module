SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
--SET row_security = off;

SET search_path = ref_nomenclatures, pg_catalog, public;

INSERT INTO bib_nomenclatures_types (
        mnemonique,
        label_fr,
        definition_fr,
        label_default,
        definition_default,
        source,
        statut
        )
VALUES
('SUPPORT_ORGANISM',
'Support sur lequel est observé le sujet d''observation',
'Indique sur quel support (biologique ou non) a été observé le sujet d’observation (l’organisme).',
'Support sur lequel est observé le sujet d''observation',
'Indique sur quel support (biologique ou non) a été observé le sujet d’observation (l’organisme).',
'SINP',
'Validé'
)
;

SELECT setval('ref_nomenclatures.bib_nomenclatures_types_id_type_seq', (SELECT max(id_type) FROM ref_nomenclatures.bib_nomenclatures_types), true);


INSERT INTO t_nomenclatures (
    id_type,
    cd_nomenclature,
    mnemonique,
    label_fr,
    definition_fr,
    label_default,
    definition_default,
    source,
    statut,
    id_broader,
    hierarchy,
    active
)
VALUES
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '1', 'Roc', 'Roche (dalle, paroi, rocher, tuiles, mur, etc.)', 'Roche (dalle, paroi, rocher, tuiles, mur, etc.)', 'Roche (dalle, paroi, rocher, tuiles, mur, etc.)', 'Roche (dalle, paroi, rocher, tuiles, mur, etc.)', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('1', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '2', 'Eco', 'Ecorce (bois vivant)', 'Ecorce (bois vivant)', 'Ecorce (bois vivant)', 'Ecorce (bois vivant)', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('2', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '3', 'Den', 'Dendrotelme', 'Dendrotelme', 'Dendrotelme', 'Dendrotelme', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('3', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '4', 'Hum', 'Humus', 'Humus', 'Humus', 'Humus', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('4', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '5', 'Ter', 'Terre nue (inclus limons, sables, graviers)', 'Terre nue (inclus limons, sables, graviers)', 'Terre nue (inclus limons, sables, graviers)', 'Terre nue (inclus limons, sables, graviers)', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('5', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '6', 'Tou', 'Tourbe', 'Tourbe', 'Tourbe', 'Tourbe', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('6', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '7', 'EauLib', 'Eau libre', 'Eau libre', 'Eau libre', 'Eau libre', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('7', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '8', 'BoiMorSol', 'Bois mort au sol', 'Bois mort au sol', 'Bois mort au sol', 'Bois mort au sol', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('8', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '9', 'SphaiBryo', 'Sphaignes vivantes ou bryophytes', 'Sphaignes vivantes ou bryophytes', 'Sphaignes vivantes ou bryophytes', 'Sphaignes vivantes ou bryophytes', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('9', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '10', 'BoiMorDeb', 'Bois mort debout', 'Bois mort debout', 'Bois mort debout', 'Bois mort debout', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('10', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '11', 'BoiImm', 'Bois immergé', 'Bois immergé', 'Bois immergé', 'Bois immergé', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('11', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '12', 'Con', 'Cône, fruit, châton', 'Cône, fruit, châton', 'Cône, fruit, châton', 'Cône, fruit, châton', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('12', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '13', 'Rac', 'Racine', 'Racine', 'Racine', 'Racine', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('13', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '14', 'Feu', 'Feuille', 'Feuille', 'Feuille', 'Feuille', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('14', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '15', 'Aig', 'Aiguille', 'Aiguille', 'Aiguille', 'Aiguille', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('15', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '16', 'PlanMor', 'Plante morte', 'Plante morte', 'Plante morte', 'Plante morte', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('16', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '17', 'PlanViv', 'Plante vivante', 'Plante vivante', 'Plante vivante', 'Plante vivante', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('17', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '18', 'Lic', 'Lichen', 'Lichen', 'Lichen', 'Lichen', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('18', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '19', 'Cham', 'Champignon non lichénisé', 'Champignon non lichénisé', 'Champignon non lichénisé', 'Champignon non lichénisé', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('19', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '20', 'AniMor', 'Animal mort', 'Animal mort', 'Animal mort', 'Animal mort', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('20', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM'), '21', 'Exc', 'Excrément', 'Excrément', 'Excrément', 'Excrément', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('SUPPORT_ORGANISM')::text, 3, '0') || '.' || LPAD('21', 3, '0'), true)
;

SELECT setval('ref_nomenclatures.t_nomenclatures_id_nomenclature_seq', (SELECT max(id_nomenclature) FROM ref_nomenclatures.t_nomenclatures), true);

