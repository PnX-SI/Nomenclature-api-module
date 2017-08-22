# Nomenclature-api-module

Flask (Python) module for Nomenclature APIModule Flask (Python)

It is used in [GeoNature](https://github.com/PnX-SI/GeoNature) but can also be used as a standalone API service to manage and returns various nomenclatures. 

Can be used as a standalone module or as git submodule. 

# Database

`bib_nomenclatures_types` contains nomenclatures types list.

id_type | mnemonique | label_fr | label_en | definition_fr | definition_en | source | statut | meta_create_date | meta_update_date
------- | ---------- | -------- | -------- | ------------- | ------------- | ------ | ------ | ---------------- | ----------------
10 | TYP_DENBR | Type de dénombrement | Counting type | Nomenclature des types de dénombrement possibles (comptage, estimation...) | Possible counting types (count, estimation...) | SINP | Validated | 2014-01-22 00:00:00 | 2015-12-16 00:00:00 | 

`t_nomenclatures` contains all nomenclatures with their type, their parent (broader) and their hierarchy.

id_nomenclature | id_type | cd_nomenclature | mnemonique | label_fr | definition_fr | source | statut | id_broader | hierarchy | meta_create_date | meta_update_date | activ
------- | ---------- | -------- | -------- | -------- | --------- | ------ | ------ | -------- | ------ | ------ | ------ | ------
10 | 10 | 8 | Têtard | Têtard | Larve de batracien | SINP | Validé | 2 | 010.008 | 2015-07-29 00:00:00 | 2015-10-09 00:00:00 | true

## Database usage

Get all nomenclatures of a type :

```
SELECT *
FROM nomenclatures.t_nomenclatures n
WHERE n.id_type = 100 AND n.active = true
```

Get all nomenclatures of a rank of a type :

```
SELECT *
FROM JAIPASCAPTE
```

# Usage


# Installation

Cloner repository and then launch in the folder:

```
python setup.py install
```
