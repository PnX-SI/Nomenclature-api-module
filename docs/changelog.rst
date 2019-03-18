=========
CHANGELOG
=========

1.2.4
------------------

**Corrections**

* Suppression d'un item de nomenclature absent du standard SINP
* Ajouts d'items sur les types 'valeur de confidentialité' et 'Sociabilité (PR @xavyeah39) 

1.2.3 (2018-12-20)
------------------

**Corrections**

* Optimisation des accès à la BDD en utilisant l'instance ``DB`` de l'application dans laquelle est utilisée ce sous-module. Cependant si elle n'existe pas, alors l'instance ``DB`` de SQLAlchemy est créée automatiquement (#17)
* Correction de la fonction ``ref_nomenclatures.get_nomenclature_label``
* Récupération dynamique du numéro de version du module à partir du fichier ``VERSION``
* Mise à jour de Flask-admin de 1.5.1 à 1.5.3 pour corriger des vulnérabilités XSS

**Notes de version**

* Exécuter le script ``data/update1.2.2to1.2.3.sql``

1.2.2 (2018-10-17)
------------------

**Corrections**

* Mise à jour de psycopg2 (2.7.3 à 2.7.5)

1.2.1 (2018-09-20)
------------------

**Nouveautés**

* Ajout d'une fonction BDD de récupération du label à partir du cd_nomenclature, code_type et de la langue (``get_nomenclature_label_by_cdnom_mnemonique_and_language``)
* Ajout d'une fonction BDD de récupération du label à partir de l'id_nomenclature et de la langue (``get_nomenclature_label_by_cdnom_mnemonique``)
* Ajout d'une fonction BDD de récupération du label à partir d'un id_nomenclature (``get_nomenclature_label``)
* Création d'une fonction Python retournant l'identifiant d'une nomenclature à partir de ses codes mnemoniques (``get_nomenclature_id_term``)
* Création d'un script SQL de mise à jour de la BDD
* Mise à jour de Flask (0.12.2 à 1.0.2)

**Corrections**

* Correction d'un bug sur la fonction BDD ``get_nomenclature_by_type_list_and_taxonomy`` si on ne passe passe pas d'``id_type`` ou de ``code_type``

**Notes de version**

* Exécuter le script ``data/update1.1.0to1.2.1.sql``
* Ne pas prendre en compte la version 1.2.0 qui est une erreur de manipulation

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
