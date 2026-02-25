# CHANGELOG

## 1.6.6 (2026-02-25)

**🚀 Nouveautés**

- Mise à jour des dépendances

## 1.6.5 (2025-05-23)

**🚀 Nouveautés**

- Ajout de la nomenclature du SINP "Type de sol" pour les occurrences d'habitat (#79)
- Ajout du support de Debian 13 dans les tests automatisés (#78)
- Mise à jour de TaxHub en version 2.2.1
- Mise à jour de Utils-Flask-SQLAlchemy en version 0.4.2

## 1.6.4 (2024-09-09)

**🚀 Nouveautés**

- Ajout de la nomenclature du SINP "Type de mosaïque d'habitats" (#74)

**🐛 Corrections**

- Correction de la fonction `get_nomenclature_id_term()` (#72)

**⚠️ Notes de version**

- Le module `UsersHub-Authentification-module` n'est plus
  requis au fonctionnement de `Nomenclature-api-module`
  (#76)

## 1.6.3 (2024-05-27)

**🚀 Nouveautés**

- Mise à jour de TaxHub en 1.14.1
- Mise à jour de UserHub-authentication-module en 2.1.5

## 1.6.2 (2024-04-26)

**🚀 Nouveautés**

- Mise à jour vers TaxHub 1.14.0
- Mise à jour vers UserHub-authentication-module 2.1.4

## 1.6.1 (2024-02-12)

**🚀 Nouveautés**

- Mise à jour vers TaxHub 1.13.3

## 1.6.0 (2024-01-30)

**🚀 Nouveautés**

- Mise à jour de SQLAlchemy version 1.3 à 1.4 (#52 et #54)
- Arrêt du support de Debian 10 (#54)
- Ajout du support de Debian 12 dans les tests automatisés (#54)
- Ajout de la possibilité d'associer des nomenclatures à des Group3
  INPN, en ajoutant le champs `group3_inpn` à la table
  `cor_taxref_nomenclature` (#53)
- Mise à jour des dépendances Python : TaxHub, Utils-Flask-SQLAlchemy,
  UsersHub-authentification-module

## 1.5.4 (2023-03-04)

**🚀 Nouveautés**

- Compatibilité SQLAlchemy 1.4
- Amélioration de la documentation de `NomenclaturesMixin`
- Simplification des modèles et de leur homologue Flask-Admin
- Mise à jour des dépendances :
  - TaxHub 1.11.1
  - UsersHub-authentification-module 1.6.5
  - Utils-Flask-SQLAlchemy 0.3.2

**🐛 Corrections**

- Ajout de shapely <2 aux requirements

## 1.5.3 (2022-09-01)

**🚀 Nouveautés**

- Ajout du type de nomenclature « Catégorie de liste rouge » et des
  nomenclatures associées.
- La branche `nomenclature_taxonomie_inpn_data` est renommée en
  `nomenclature_taxonomie_data`, et ne dépend plus du référentiel
  TaxRef qui doit être importé manuellement.
- Le code est désormais formaté avec Black et une Github Action y
  veille.
- Possibilité de filtrer les nomenclatures par code
  (`cd_nomenclature`).
- Mise à jour des dépendances :
  - Utils-Flask-SQLAlchemy 0.3.0
  - TaxHub 1.10.0
  - UsersHub-authentification-module 1.6.0

**🐛 Corrections**

- Correction de la définition d'un type de nomenclature
- Correction des tests unitaires

## 1.5.1 (2022-01-12)

**🚀 Nouveautés**

- `NomenclaturesConverter` : Utilitaire pour ajouter automatiquement à
  un auto-schéma Marshmallow des champs Nested pour toutes les
  relations du modèle vers une nomenclature.
- `NomenclaturesMixin` : Ajoute automatiquement aux modèles une
  propriété `__nomenclatures__` contenant la liste des relations vers
  une nomenclature.

## 1.5.0 (2022-01-04)

**🚀 Nouveautés**

- Possibilité de lancer l'API Nomenclature de manière autonome
- Possibilité de créer son schéma de base de données de manière
  autonome
- Mise en place des tests unitaires
- Mise en place de l'intégration continue
- Intégration des dépendances en tant que sous-module Git
  - Utils-Flask-SQLAlchemy
  - TaxHub (pour la taxonomie)
  - UsersHub-authentification-module (car requis par TaxHub)

**🐛 Corrections**

- Suppression d'anciens fichiers devenus inutiles suite au paquetage

## 1.4.5 (2021-01-03)

**🐛 Corrections**

- `ref_nomenclatures.get_nomenclature_label` : retourne `NULL` si
  l'identifiant de nomenclature est nul.

## 1.4.4 (2021-10-06)

**🐛 Corrections**

- Correction des champs par défaut pour la sérialisation du modèle
  `TNomenclatures`

## 1.4.3 (2021-10-06)

**🐛 Corrections**

- Correction de la fonction `get_default_nomenclature_value` : si
  l'organisme n'est pas trouvé, retourne la nomenclature de
  l'organisme « `ALL` »

## 1.4.2 (2021-10-06)

**🐛 Corrections**

- Correction de la fonction `get_default_nomenclature_value`
  lorsqu'appelé sans organisme

## 1.4.1 (2021-10-01)

**🐛 Corrections**

- Ajout d'un fichier `__init__.py` dont l'absence excluait les
  révisions Alembic lors du paquetage du module

## 1.4.0 (2021-10-01)

**🚀 Nouveautés**

- Gestion du schéma `ref_nomenclature` avec Alembic. Branches
  disponibles :
  - `nomenclatures` : crée le schema `ref_nomenclatures`
  - `nomenclatures_taxonomie` : crée la table
    `ref_nomenclatures.cor_taxref_nomenclature`, et les fonctions et
    vues associées
  - `nomenclatures_inpn_data` : insère les données de nomenclature
    de l'INPN
  - `nomenclatures_taxonomie_inpn_data` : insère les données de
    nomenclature de l'INPN lié à la taxonomie

## 1.3.8 (2021-06-30)

**🐛 Corrections**

- Correction sur la route `/nomenclatures/taxonomy`

## 1.3.7 (2021-06-03)

**🚀 Nouveautés**

- Ajout de schémas Marshmallow

**🐛 Corrections**

- Correction du script de mise à jour de la BDD
  `data/update1.3.4to1.3.5.sql`
- Interface d'administration instantiable sans app context

## 1.3.6 (2021-02-08)

**🚀 Nouveautés**

- Clarification des nomenclatures de sensibilité, avec des
  vocabulaires plus précis et cohérents, en attendant les évolutions
  au niveau du SINP (#39)

**🐛 Corrections**

- Correction du script de mise à jour de la BDD
  `data/update1.3.4to1.3.5.sql` si la nomenclature ajoutée dans la
  version 1.3.5 étant déjà présent dans la BDD (#42)

**⚠️ Notes de version**

- Si vous mettez à jour le module, exécuter le script SQL
  `data/update1.3.5to1.3.6.sql`

## 1.3.5 (2021-02-04)

**🚀 Nouveautés**

- Passage de l'instance de SQLAlchemy du module parent via une
  variable d'environnement

**🐛 Corrections**

- Les dépendances du fichier `requirements.txt` ne sont plus fixées à
  une version
- Ajout de vocabulaire manquant

**⚠️ Notes de version**

- Si vous mettez à jour le module, exécuter le script SQL
  `data/update1.3.4to1.3.5.sql`

## 1.3.4 (2020-09-29)

**🚀 Nouveautés**

- Compatibilité avec la version 2.0 du standard Occurrences de taxons
  du SINP
- Ajout de la nomenclature "Comportement" et ses correspondances
  avec la taxonomie
- Mise à jour de la nomenclature "Statut biologique"
- Ajouts mineurs dans les nomenclatures "Floutage DEE", "Techniques
  d'observation" (anciennement "Méthode d'observation"), "Stade
  de vie"
- Compatibilité avec la version 1.3.10 du standard Métadonnées du SINP
- Mise à jour de la nomenclature "Objectifs du cadre d'acquisition"

**⚠️ Notes de version**

- Si vous mettez à jour le module, exécuter le script SQL
  `data/update1.3.3to1.3.4.sql`

## 1.3.3 (2020-06-17)

**🐛 Corrections**

- Correction des dates des nomenclatures (#32)
- Correction des définitions SINP des nomenclatures d'habitats (#33)
- Mise à jour des nomenclatures de type `DATA_TYP` (#33)
- Taxref 13 : Les group2_inpn `Fougères` et `Algues brunes` ont été
  remplacés par `Ptéridophytes` et `Ochrophytes`. Répercussion dans la
  table `ref_nomenclatures.cor_taxref_nomenclature`

**⚠️ Notes de version**

- Si vous mettez à jour le module, exécuter le script SQL
  `data/update1.3.2to1.3.3.sql`
- Si vous avez mis à jour Taxref en version 13, répercutez les
  changements de group2_inpn avec le script SQL
  `data/update_taxref_v13.sql`

## 1.3.2 (2019-12-30)

**🐛 Corrections**

- Correction de données SQL mineures

**Notes de version**

- Si vous mettez à jour le module, exécuter le script SQL
  `data/update1.3.1to1.3.2.sql`

## 1.3.1 (2019-12-20)

**🚀 Nouveautés**

- Utilisation de la librairie Utils-Flask-SQLAlchemy
- Ajout de nomenclatures SINP concernant les habitats
- Ajout d'une contrainte d'unicité sur la combinaison des champs
  `id_type` et `cd_nomenclature` de la table `t_nomenclatures` (#28)

**🐛 Corrections**

- Séparation de modèles faisant référence à la taxonomie

## 1.3.0 (2019-09-16)

**Nouveautés**

- Ajout d'une route pour remettre à plat toutes les nomenclatures et
  leurs correspondances taxonomiques (par @sgrimault)
- Passage à Flask 1.1.1

## 1.2.6 (2019-07-19)

**Corrections**

- Le module Flask-admin a été retiré du sous-module. Il est désormais
  à la charge de l'application qui utilise le sous-module de
  l'instancier.

## 1.2.5 (2019-05-29)

**Nouveautés**

- Mise à jour de SQLAlchemy 1.1.13 vers 1.3.3

## 1.2.4 (2019-03-18)

**Corrections**

- Suppression d'un item de nomenclature absent du standard SINP
- Ajouts d'items sur les types 'Valeur de confidentialité' et
  'Sociabilité' (PR @xavyeah39)

**Notes de version**

- Exécuter le script
  <https://github.com/PnX-SI/Nomenclature-api-module/blob/master/data/update1.2.3to1.2.4.sql>

## 1.2.3 (2018-12-20)

**Corrections**

- Optimisation des accès à la BDD en utilisant l'instance `DB` de
  l'application dans laquelle est utilisée ce sous-module. Cependant
  si elle n'existe pas, alors l'instance `DB` de SQLAlchemy est
  créée automatiquement (#17)
- Correction de la fonction `ref_nomenclatures.get_nomenclature_label`
- Récupération dynamique du numéro de version du module à partir du
  fichier `VERSION`
- Mise à jour de Flask-admin de 1.5.1 à 1.5.3 pour corriger des
  vulnérabilités XSS

**Notes de version**

- Exécuter le script `data/update1.2.2to1.2.3.sql`

## 1.2.2 (2018-10-17)

**Corrections**

- Mise à jour de psycopg2 (2.7.3 à 2.7.5)

## 1.2.1 (2018-09-20)

**Nouveautés**

- Ajout d'une fonction BDD de récupération du label à partir du
  cd_nomenclature, code_type et de la langue
  (`get_nomenclature_label_by_cdnom_mnemonique_and_language`)
- Ajout d'une fonction BDD de récupération du label à partir de
  l'id_nomenclature et de la langue
  (`get_nomenclature_label_by_cdnom_mnemonique`)
- Ajout d'une fonction BDD de récupération du label à partir d'un
  id_nomenclature (`get_nomenclature_label`)
- Création d'une fonction Python retournant l'identifiant d'une
  nomenclature à partir de ses codes mnemoniques
  (`get_nomenclature_id_term`)
- Création d'un script SQL de mise à jour de la BDD
- Mise à jour de Flask (0.12.2 à 1.0.2)

**Corrections**

- Correction d'un bug sur la fonction BDD
  `get_nomenclature_by_type_list_and_taxonomy` si on ne passe passe
  pas d'`id_type` ou de `code_type`

**Notes de version**

- Exécuter le script `data/update1.1.0to1.2.1.sql`
- Ne pas prendre en compte la version 1.2.0 qui est une erreur de
  manipulation

## 1.1.0 (2018-07-10)

**Nouveautés**

- Création d'une interface d'administration (Flask-admin) pour gérer
  les nomenclatures et leurs types. URL paramétrable avec
  `URL_ADMIN_NOMENCLATURES` dans le fichier `config.py`
  (`/nomenclatures/admin` par défaut)
- Intégration des scripts SQL dans le dépôt du module et suppression
  du dépôt GeoNature (#3)
- Gestion des conflits de nomenclatures en ne définissant ni
  n'utilisant les `id_type` ni `id_nomenclature` dans le SQL et le
  code du module et des applications qui utilisent la nomenclature
  (#9)
- Ajout de fonctions pour retrouver ces ID à partir des codes des
  nomenclatures et des mnemoniques des types (SQL et API)
- Découpage des scripts SQL pour permettre de ne pas intégrer les
  liens entre Nomenclatures et Taxonomie
  (<https://github.com/PnX-SI/GeoNature/issues/384>) et ajout du
  paramètre `ENABLE_NOMENCLATURE_TAXONOMIC_FILTERS` dans le fichier
  `config.py`
- Mise à jour des dépendances (`requirements.txt`)

## 1.0.0 (2018-05-16)

Première version stabilisée du sous-module de gestion des nomenclatures.

- SQL et API fonctionnels pour gérer et utiliser les nomenclatures
  dans un référentiel centralisé
- Intégration des nomenclatures SINP et GeoNature
- Définition de nomenclatures par défaut dans
  `ref_nomenclatures.defaults_nomenclatures_value`
- Définition de correspondances entre nomenclatures et taxonomie
  (règnes et groupes) dans
  `ref.nomenclatures.defaults_nomenclatures_value`
- Mise en place de fonctions SQL pour retrouver ou vérifier les
  nomenclatures
