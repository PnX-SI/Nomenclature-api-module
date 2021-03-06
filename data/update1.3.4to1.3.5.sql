-- Ajout d'un vocabulaire de nomenclature manquant
DO $$
BEGIN
    IF EXISTS (select * from ref_nomenclatures.t_nomenclatures where cd_nomenclature = 'NSP' and id_type=ref_nomenclatures.get_id_nomenclature_type('STATUT_OBS'))
    THEN
    UPDATE ref_nomenclatures.t_nomenclatures SET active = true WHERE id_nomenclature = ref_nomenclatures.get_id_nomenclature('STATUT_OBS', 'NSP');
    ELSE
    INSERT INTO ref_nomenclatures.t_nomenclatures (id_type, cd_nomenclature, mnemonique, label_fr, label_default, definition_fr, source, statut, id_broader, hierarchy, meta_create_date, meta_update_date, active) VALUES
    (ref_nomenclatures.get_id_nomenclature_type('STATUT_OBS'), 'NSP', 'NSP', 'Ne Sait Pas', 'Ne Sait Pas', 'Ne Sait Pas : l''information n''est pas connue', 'SINP', 'Validé', 0, '018.003', '2020-12-22 00:00:00', '2020-12-22 00:00:00', true);
    END IF;
END $$;
DO $$
BEGIN
    IF EXISTS(
        SELECT * FROM ref_nomenclatures.cor_taxref_nomenclature WHERE 
        id_nomenclature = ref_nomenclatures.get_id_nomenclature('STATUT_OBS', 'NSP') AND 
        regne = 'all' AND group2_inpn = 'all'
        )
        THEN RAISE NOTICE 'Already exists';
    ELSE 
    INSERT INTO ref_nomenclatures.cor_taxref_nomenclature VALUES
    (ref_nomenclatures.get_id_nomenclature('STATUT_OBS', 'NSP'), 'all', 'all', now(), NULL);
    END IF;
END $$;

-------------------------------------------------------------------------------------------------
-- Clarification des nomenclatures de sensibilité, en attendant qu'ils évoluent au niveau du SINP
-------------------------------------------------------------------------------------------------

update ref_nomenclatures.t_nomenclatures 
set label_fr = 'Non sensible'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '0';

update ref_nomenclatures.t_nomenclatures 
set label_fr = 'Commune ou Znieff (visible uniquement à partir du niveau)'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '1';

update ref_nomenclatures.t_nomenclatures 
set label_fr = 'Mailles 10 (visible uniquement à partir du niveau)'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '2';

update ref_nomenclatures.t_nomenclatures 
set label_fr = 'Départements (visible uniquement à partir du niveau)'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '3';

update ref_nomenclatures.t_nomenclatures 
set label_fr = 'Aucune diffusion'
where id_type = (select id_type from ref_nomenclatures.bib_nomenclatures_types where mnemonique = 'SENSIBILITE') and cd_nomenclature = '4';
