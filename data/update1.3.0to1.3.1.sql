ALTER TABLE ref_nomenclatures.t_nomenclatures
  ADD CONSTRAINT unique_id_type_cd_nomenclature UNIQUE (id_type, cd_nomenclature);
