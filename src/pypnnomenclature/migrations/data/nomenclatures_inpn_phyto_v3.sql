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
('STRATE_VEGETATION',
'Niveau d’étagement vertical du peuplement végétal',
'Niveau d’étagement vertical du peuplement végétal',
'Niveau d’étagement vertical du peuplement végétal',
'Niveau d’étagement vertical du peuplement végétal',
'SINP',
'Validé'
),
('PHYTO_ABUNDANCE',
'Abondance-dominance du taxon',
'Abondance-dominance du taxon, suivant l''échelle de Braun Blanquet Barkman (Géhu, 2006).',
'Abondance-dominance du taxon',
'Abondance-dominance du taxon, suivant l''échelle de Braun Blanquet Barkman (Géhu, 2006).',
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
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '1', 'AqEn', 'Aquatique enracinée', 'Aquatique enracinée', 'Aquatique enracinée', 'Aquatique enracinée', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('1', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '2', 'AqNa', 'Aquatique nageante', 'Aquatique nageante', 'Aquatique nageante', 'Aquatique nageante', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('2', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '3', 'AqFlo', 'Aquatique flottante', 'Aquatique flottante', 'Aquatique flottante', 'Aquatique flottante', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('3', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '4', 'Arbo', 'Arborée', 'Arborée', 'Arborée', 'Arborée', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('4', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '5', 'Arbu', 'Arbustive', 'Arbustive', 'Arbustive', 'Arbustive', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('5', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '6', 'SouArb', 'Sous-arbustive', 'Sous-arbustive', 'Sous-arbustive', 'Sous-arbustive', 'CBNA', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('6', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '7', 'Bryo', 'Bryo-lychénique', 'Bryo-lychénique', 'Bryo-lychénique', 'Bryo-lychénique', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('7', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '8', 'Crypt', 'Cryptogamique', 'Cryptogamique', 'Cryptogamique', 'Cryptogamique', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('8', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '9', 'Epig', 'Épigéique', 'Épigéique', 'Épigéique', 'Épigéique', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('9', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '10', 'Epil', 'Épilithique', 'Épilithique', 'Épilithique', 'Épilithique', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('10', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '11', 'Epiph', 'Épiphytique', 'Épiphytique', 'Épiphytique', 'Épiphytique', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('11', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '12', 'Epix', 'Épixylique', 'Épixylique', 'Épixylique', 'Épixylique', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('12', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '13', 'Herb', 'Herbacée', 'Herbacée', 'Herbacée', 'Herbacée', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('13', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '14', 'Musc', 'Muscinale', 'Muscinale', 'Muscinale', 'Muscinale', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('14', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION'), '15', 'Uniq', 'Unique', 'Unique', 'Unique', 'Unique', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('STRATE_VEGETATION')::text, 3, '0') || '.' || LPAD('15', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE'), 'i', 'IndI', 'Un seul individu présent, recouvrement très faible (<5%)', 'Un seul individu présent, recouvrement très faible (<5%)', 'Un seul individu présent, recouvrement très faible (<5%)', 'Un seul individu présent, recouvrement très faible (<5%)', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE')::text, 3, '0') || '.' || LPAD('1', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE'), 'r', 'IndR', 'Individus rares ou très rares, recouvrement faible (<5%)', 'Individus rares ou très rares, recouvrement faible (<5%)', 'Individus rares ou très rares, recouvrement faible (<5%)', 'Individus rares ou très rares, recouvrement faible (<5%)', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE')::text, 3, '0') || '.' || LPAD('2', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE'), '+', 'IndPA', 'Individus peu abondants, recouvrement faible (<5%)', 'Individus peu abondants, recouvrement faible (<5%)', 'Individus peu abondants, recouvrement faible (<5%)', 'Individus peu abondants, recouvrement faible (<5%)', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE')::text, 3, '0') || '.' || LPAD('3' , 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE'), '1', 'Ind1', 'Individus assez abondants, recouvrement faible (< 5%)', 'Individus assez abondants, recouvrement faible (< 5%)', 'Individus assez abondants, recouvrement faible (< 5%)', 'Individus assez abondants, recouvrement faible (< 5%)', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE')::text, 3, '0') || '.' || LPAD('4', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE'), '2', 'Ind2', 'Individus abondants, recouvrement de 5 à 25%', 'Individus abondants, recouvrement de 5 à 25%', 'Individus abondants, recouvrement de 5 à 25%', 'Individus abondants, recouvrement de 5 à 25%', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE')::text, 3, '0') || '.' || LPAD('5', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE'), '2m', 'Ind2m', 'Individus abondants, recouvrement < 5%', 'Individus abondants, recouvrement < 5%', 'Individus abondants, recouvrement < 5%', 'Individus abondants, recouvrement < 5%', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE')::text, 3, '0') || '.' || LPAD('6', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE'), '2a', 'Ind2a', 'Individus en nombre quelconque, recouvrement entre 5 et 12,5%', 'Individus en nombre quelconque, recouvrement entre 5 et 12,5%', 'Individus en nombre quelconque, recouvrement entre 5 et 12,5%', 'Individus en nombre quelconque, recouvrement entre 5 et 12,5%', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE')::text, 3, '0') || '.' || LPAD('7', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE'), '2b', 'Ind2b', 'Individus en nombre quelconque, recouvrement entre 12,5 et 25%', 'Individus en nombre quelconque, recouvrement entre 12,5 et 25%', 'Individus en nombre quelconque, recouvrement entre 12,5 et 25%', 'Individus en nombre quelconque, recouvrement entre 12,5 et 25%', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE')::text, 3, '0') || '.' || LPAD('8', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE'), '3', 'Ind3', 'Individus en nombre quelconque, recouvrement entre 25 et 50%', 'Individus en nombre quelconque, recouvrement entre 25 et 50%', 'Individus en nombre quelconque, recouvrement entre 25 et 50%', 'Individus en nombre quelconque, recouvrement entre 25 et 50%', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE')::text, 3, '0') || '.' || LPAD('9', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE'), '4', 'Ind4', 'Individus en nombre quelconque, recouvrement entre 50 et 75%', 'Individus en nombre quelconque, recouvrement entre 50 et 75%', 'Individus en nombre quelconque, recouvrement entre 50 et 75%', 'Individus en nombre quelconque, recouvrement entre 50 et 75%', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE')::text, 3, '0') || '.' || LPAD('10', 3, '0'), true),
(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE'), '5', 'Ind5', 'Individus en nombre quelconque, recouvrement > 75%', 'Individus en nombre quelconque, recouvrement > 75%', 'Individus en nombre quelconque, recouvrement > 75%', 'Individus en nombre quelconque, recouvrement > 75%', 'SINP', 'Validé', '0', LPAD(ref_nomenclatures.get_id_nomenclature_type('PHYTO_ABUNDANCE')::text, 3, '0') || '.' || LPAD('11', 3, '0'), true)
;



SELECT setval('ref_nomenclatures.t_nomenclatures_id_nomenclature_seq', (SELECT max(id_nomenclature) FROM ref_nomenclatures.t_nomenclatures), true);

