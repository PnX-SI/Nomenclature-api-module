-- MAJ des relations avec group2_inpn "fougère" et "Algues brunes" supprimé
UPDATE ref_nomenclatures.cor_taxref_nomenclature
SET group2_inpn = 'Ptéridophytes' WHERE group2_inpn = 'Fougères';

UPDATE ref_nomenclatures.cor_taxref_nomenclature
SET group2_inpn = 'Ochrophytes' WHERE group2_inpn = 'Algues brunes';