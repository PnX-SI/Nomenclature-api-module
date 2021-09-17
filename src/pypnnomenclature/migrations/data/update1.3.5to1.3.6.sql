-------------------------------------------------------------------------------------------------
-- Clarification des nomenclatures de sensibilité, en attendant qu'ils évoluent au niveau du SINP
-- Après une première clarification des intitulés dans la 1.3.5, les intitulés sont affinés...
-------------------------------------------------------------------------------------------------

Update ref_nomenclatures.t_nomenclatures 
set label_fr = 'Non sensible - Diffusion précise'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '0';
Update ref_nomenclatures.t_nomenclatures 
set definition_fr = 'Donnée non sensible - Diffusion précise'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '0';

Update ref_nomenclatures.t_nomenclatures 
set label_fr = 'Sensible - Diffusion à la Commune ou Znieff'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '1';
Update ref_nomenclatures.t_nomenclatures 
set definition_fr = 'Sensible - Commune ou Znieff (visible uniquement à partir du niveau)'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '1';

Update ref_nomenclatures.t_nomenclatures 
set label_fr = 'Sensible - Diffusion à la maille 10km'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '2';
Update ref_nomenclatures.t_nomenclatures 
set definition_fr = 'Sensibile - Mailles 10 (visible uniquement à partir du niveau)'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '2';

Update ref_nomenclatures.t_nomenclatures 
set label_fr = 'Sensible - Diffusion au département'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '3';
Update ref_nomenclatures.t_nomenclatures 
set definition_fr = 'Sensible - Départements (visible uniquement à partir du niveau)'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '3';

Update ref_nomenclatures.t_nomenclatures 
set label_fr = 'Sensible - Aucune diffusion'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '4';
Update ref_nomenclatures.t_nomenclatures 
set definition_fr = 'Sensible - Aucune diffusion'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '4';
