# Nomenclature-api-module

[![pytest](https://github.com/PnX-SI/Nomenclature-api-module/actions/workflows/pytest.yml/badge.svg)](https://github.com/PnX-SI/Nomenclature-api-module/actions/workflows/pytest.yml)
[![codecov](https://codecov.io/gh/PnX-SI/Nomenclature-api-module/branch/master/graph/badge.svg?token=KGZRGXFWCK)](https://codecov.io/gh/PnX-SI/Nomenclature-api-module)

Flask (Python) module for Nomenclature API.

It is used in [GeoNature](https://github.com/PnX-SI/GeoNature) but can also be used as a standalone API service to manage and returns various nomenclatures with their hierarchy. 

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

# API

* Récupération des termes d'une nomenclature à partir de l'identifiant : ```/nomenclature/6[?regne=Animalia[&group2_inpn=Bivalves]]```
 DEPRECIE

* Récupération des termes d'une nomenclature à partir du code mnemonique :```/nomenclature/STADE_VIE[?regne=Animalia[&group2_inpn=Bivalves]]```
* Récupération des termes d'un ensemble de nomenclature :
  * ```/nomenclatures?id_type=22&id_type=6[&regne=Animalia[&group2_inpn=Bivalves]]```  DEPRECIE
  * ```/nomenclatures?code_type=STADE_VIE&code_type=REF_HAB[&regne=Animalia[&group2_inpn=Bivalves]]```


# Interface d'administration des données

 * Accessible via l'url /nomenclatures/admin

# Installation

Cloner repository and then launch in the folder:

```
python setup.py install
```
