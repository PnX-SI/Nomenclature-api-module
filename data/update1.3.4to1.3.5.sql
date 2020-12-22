INSERT INTO ref_nomenclatures.t_nomenclatures (id_type, cd_nomenclature, mnemonique, label_fr, label_default, definition_fr,  source, statut, id_broader, hierarchy, meta_create_date, meta_update_date, active) VALUES
(ref_nomenclatures.get_id_nomenclature_type('STATUT_OBS'), 'NSP', 'NSP', 'Ne Sait Pas', 'Ne Sait Pas', 'Ne Sait Pas : l''information n''est pas connue', 'SINP', 'Validé', 0, '018.003', '2020-12-22 00:00:00', '2020-12-22 00:00:00', true);

INSERT INTO ref_nomenclatures.cor_taxref_nomenclature VALUES
(ref_nomenclatures.get_id_nomenclature('STATUT_OBS', 'NSP'), 'all', 'all', now(), NULL);
