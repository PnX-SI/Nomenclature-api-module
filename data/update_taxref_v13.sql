-- MAJ des relations des nomenclatures avec les group2_inpn "Fougères" et "Algues brunes" renommés dans Taxref 13
UPDATE ref_nomenclatures.cor_taxref_nomenclature
SET group2_inpn = 'Ptéridophytes' WHERE group2_inpn = 'Fougères';

UPDATE ref_nomenclatures.cor_taxref_nomenclature
SET group2_inpn = 'Ochrophytes' WHERE group2_inpn = 'Algues brunes';
