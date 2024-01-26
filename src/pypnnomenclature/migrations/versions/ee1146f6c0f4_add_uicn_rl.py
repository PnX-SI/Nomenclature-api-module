"""Add UICN Red List

Revision ID: ee1146f6c0f4
Revises: 618542880d1f
Create Date: 2022-07-28 15:01:47.927979

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ee1146f6c0f4"
down_revision = "618542880d1f"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
    INSERT INTO
        ref_nomenclatures.bib_nomenclatures_types (
            mnemonique,
            label_fr,
            definition_fr,
            label_default,
            definition_default,
            source, statut,
            meta_create_date,
            meta_update_date
        )
    VALUES
        (
            'CAT_LISTE_ROUGE',
            'Catégorie de liste rouge',
            'Nomenclature des catégorie de menace',
            'Catégorie de liste rouge',
            'Nomenclature des catégorie de menace',
            'UICN',
            'Validé',
            '2019-04-11 00:00:00',
            '2019-04-11 00:00:00'
        )
    """
    )
    op.execute(
        """
    INSERT INTO
        ref_nomenclatures.t_nomenclatures (
            id_type,
            cd_nomenclature,
            mnemonique,
            label_fr,
            definition_fr,
            source,
            statut,
            id_broader,
            hierarchy,
            meta_create_date,
            meta_update_date,
            active,
            label_default
        )
    VALUES
        (ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE'), 'LC', 'LC', 'Préoccupation mineure', 'Un taxon est dit de Préoccupation mineure lorsqu’il a été évalué d’après les critères et ne remplit pas les critères des catégories En danger critique, En danger, Vulnérable ou Quasi menacé. Dans cette catégorie sont inclus les taxons largement répandus et abondants.', 'UICN', 'Validé', 0, NULL, '2019-04-11 00:00:00', '2019-04-11 00:00:00', true, '')
        ,(ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE'), 'NT', 'NT', 'Quasi-menacé', 'Un taxon est dit Quasi menacé lorsqu’il a été évalué d’après les critères et ne remplit pas, pour l’instant, les critères des catégories En danger critique, En danger ou Vulnérable mais qu’il est près de remplir les critères correspondant aux catégories du groupe Menacé ou qu’il les remplira probablement dans un proche avenir.', 'UICN', 'Validé', 0, NULL, '2019-04-11 00:00:00', '2019-04-11 00:00:00', true, '')
        ,(ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE'), 'VU', 'VU', 'Vulnérable', 'Un  taxon  est  dit Vulnérable  lorsque  les  meilleures  données  disponibles  indiquent  qu’il remplit l’un des critères correspondant à la catégorie Vulnérable et, en conséquence, qu’il est confronté à un risque élevé d’extinction à l’état sauvage.', 'UICN', 'Validé', 0, NULL, '2019-04-11 00:00:00', '2019-04-11 00:00:00', true, '')
        ,(ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE'), 'EN', 'EN', 'En danger', 'Un  taxon  est  dit En  danger  lorsque  les  meilleures  données  disponibles  indiquent  qu’il remplit l’un des critères correspondant à la catégorie En danger et, en conséquence, qu’il est confronté à un risque très élevé d’extinction à l’état sauvage.', 'UICN', 'Validé', 0, NULL, '2019-04-11 00:00:00', '2019-04-11 00:00:00', true, '')
        ,(ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE'), 'CR', 'CR', 'En danger critique', 'Un taxon est dit En danger critique lorsque les meilleures données disponibles indiquent qu’il  remplit  l’un  des  critères correspondant  à  la  catégorie En  danger  critique et, en conséquence, qu’il est confronté à un risque extrêmement élevé d’extinction à l’état sauvage.', 'UICN', 'Validé', 0, NULL, '2019-04-11 00:00:00', '2019-04-11 00:00:00', true, '')
        ,(ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE'), 'CR*', 'CR*', 'En danger critique, probablement éteint', 'En danger critique, probablement éteint', 'UICN', 'Validé', 0, NULL, '2019-04-11 00:00:00', '2019-04-11 00:00:00', true, '')
        ,(ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE'), 'EW', 'EW', 'Eteint à l''état sauvage', 'Un taxon est dit Éteint à l’état sauvage lorsqu’il ne survit qu’en culture, en captivité ou dans le cadre d’une population (ou de populations) naturalisée(s), nettement en dehors de son ancienne aire de répartition. Un taxon est présumé Éteint à l’état sauvage lorsque des études détaillées menées dans ses habitats connus et/ou probables, à des périodes appropriées  (rythme  diurne,  saisonnier,  annuel),  et  dans  l’ensemble  de  son  aire  de répartition historique n’ont pas permis de noter la présence d’un seul individu. Les études doivent être faites sur une durée adaptée au cycle et aux formes biologiques du taxon. ', 'UICN', 'Validé', 0, NULL, '2019-04-11 00:00:00', '2019-04-11 00:00:00', true, '')
        ,(ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE'), 'EX', 'EX', 'Eteint', 'Un  taxon  est  dit Éteint  lorsqu’il  ne  fait  aucun  doute  que  le  dernier  individu  est  mort. Un taxon est présumé Éteint lorsque des études exhaustives menées dans son habitat connu  et/ou  présumé,  à  des  périodes  appropriées  (rythme  diurne,  saisonnier,  annuel), et  dans  l’ensemble  de  son  aire  de  répartition  historique  n’ont  pas  permis  de  noter  la présence  d’un  seul  individu.  Les  études  doivent  être  faites  sur  une  durée  adaptée  au cycle et aux formes biologiques du taxon.', 'UICN', 'Validé', 0, NULL, '2019-04-11 00:00:00', '2019-04-11 00:00:00', true, '')
        ,(ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE'), 'RE', 'RE', 'Eteint au niveau régional', 'Catégorie  assignée  à  un  taxon  lorsqu’il  n’y  a  aucun  doute  raisonnable  que  le  dernier individu en mesure de se reproduire dans la région est mort ou a disparu à l’état sauvage dans  cette  région,  ou  encore,  s’il  s’agit  d’un  ancien  taxon  visiteur,  lorsque  le  dernier individu  est  mort  ou  a  disparu  à  l’état  sauvage  dans  cette  région.  La  limite  de  temps choisie pour inscrire un taxon dans la catégorie RE est laissée à la discrétion de l’autorité régionale pour la Liste rouge mais ne devrait normalement pas être antérieure à l’an 1500 de notre ère.', 'UICN', 'Validé', 0, NULL, '2019-04-11 00:00:00', '2019-04-11 00:00:00', true, '')
        ,(ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE'), 'NA', 'NA', 'Non applicable', 'Catégorie réservée à un taxon considéré comme impossible à évaluer au niveau régional. Un  taxon  peut  entrer  dans  la  catégorie  NA  parce  qu’il  ne  s’agit  pas  d’une  population sauvage ou parce qu’il n’est pas dans son aire de répartition naturelle dans cette région, ou  encore  parce  qu’il  est  erratique  dans  la  région.  Un  taxon  peut  aussi  entrer  dans  la catégorie  NA  parce  qu’il  n’est  présent  qu’en  très  petit  nombre  dans  la  région  (p.  ex. lorsque l’autorité régionale pour la Liste rouge a décidé d’utiliser un «filtre» pour exclure certains  taxons  avant  la  procédure  d’évaluation)  ou  parce  qu’il  est  classé  à  un  niveau taxonomique inférieur (p. ex. au-dessous du niveau de l’espèce ou de la sous-espèce) aux  niveaux  considérés  comme  éligibles  par  l’autorité  régionale  pour  la  Liste  rouge.  À la  différence  d’autres  catégories  de  la  Liste  rouge,  il  n’est  pas  obligatoire  d’assigner  la catégorie NA à tous les taxons auxquels elle s’applique mais c’est cependant recommandé lorsque cela a une valeur informative.', 'UICN', 'Validé', 0, NULL, '2019-04-11 00:00:00', '2019-04-11 00:00:00', true, '')
        ,(ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE'), 'DD', 'DD', 'Données insuffisantes', 'Un  taxon  entre  dans  la  catégorie Données  insuffisantes  lorsqu’on  ne  dispose  pas d’assez  de  données  pour  évaluer  directement  ou  indirectement  le  risque  d’extinction en  fonction  de  sa  distribution  et/ou  de  l’état  de  sa  population.  Un  taxon  inscrit  dans cette catégorie peut avoir fait l’objet d’études approfondies et sa biologie peut être bien connue, sans que l’on dispose pour autant de données pertinentes sur l’abondance et/ou la distribution. Il ne s’agit donc pas d’une catégorie Menacé. L’inscription d’un taxon dans cette catégorie indique qu’il est nécessaire de rassembler davantage de données et n’exclut pas la possibilité de démontrer, grâce à de futures recherches, que le taxon aurait pu être classé dans une catégorie Menacé. Il est impératif d’utiliser pleinement toutes les données disponibles.', 'UICN', 'Validé', 0, NULL, '2019-04-11 00:00:00', '2019-04-11 00:00:00', true, '')
        ,(ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE'), 'NE', 'NE', 'Non évalué', 'Un taxon est dit Non évalué lorsqu’il n’a pas encore été confronté aux critères.', 'UICN', 'Validé', 0, NULL, '2019-04-11 00:00:00', '2019-04-11 00:00:00', true, '')
    """
    )
    op.execute(
        """
    UPDATE
        ref_nomenclatures.t_nomenclatures
    SET
        label_default = label_fr,
        definition_default = definition_fr
    WHERE
        id_type = ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE')
    """
    )


def downgrade():
    op.execute(
        """
    DELETE FROM
        ref_nomenclatures.t_nomenclatures
    WHERE
        id_type = ref_nomenclatures.get_id_nomenclature_type('CAT_LISTE_ROUGE')
    """
    )
    op.execute(
        """
    DELETE FROM
        ref_nomenclatures.bib_nomenclatures_types
    WHERE
        mnemonique = 'CAT_LISTE_ROUGE'
    """
    )
