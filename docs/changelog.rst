=========
CHANGELOG
=========

1.1.1 (unreleased)
------------------

**Corrections**

*

1.1.0 (2018-07-10)
------------------

**Nouveautés**

* Création d'une interface d'administration (Flask-admin) pour gérer les nomenclatures et leurs types. URL paramétrable avec ``URL_ADMIN_NOMENCLATURES`` dans le fichier ``config.py`` (``/nomenclatures/admin`` par défaut)
* Intégration des scripts SQL dans le dépôt du module et suppression du dépôt GeoNature (#3)
* Gestion des conflits de nomenclatures en ne définissant ni n'utilisant les ``id_type`` ni ``id_nomenclature`` dans le SQL et le code du module et des applications qui utilisent la nomenclature (#9) 
* Ajout de fonctions pour retrouver ces ID à partir des codes des nomenclatures et des mnemoniques des types (SQL et API)
* Découpage des scripts SQL pour permettre de ne pas intégrer les liens entre Nomenclatures et Taxonomie (https://github.com/PnX-SI/GeoNature/issues/384) et ajout du paramètre ``ENABLE_NOMENCLATURE_TAXONOMIC_FILTERS`` dans le fichier ``config.py``
* Mise à jour des dépendances (``requirements.txt``)


1.0.0 (2018-05-16)
------------------

Première version stabilisée du sous-module de gestion des nomenclatures.

* SQL et API fonctionnels pour gérer et utiliser les nomenclatures dans un référentiel centralisé
* Intégration des nomenclatures SINP et GeoNature
* Définition de nomenclatures par défaut dans ``ref_nomenclatures.defaults_nomenclatures_value``
* Définition de correspondances entre nomenclatures et taxonomie (règnes et groupes) dans ``ref.nomenclatures.defaults_nomenclatures_value``
* Mise en place de fonctions SQL pour retrouver ou vérifier les nomenclatures
