"""
    Méthode permettant de manipuler les objets de la nomenclature
"""
from importlib import import_module
from flask import current_app

from .models import (
    TNomenclatures,
    BibNomenclaturesTypes,
    TNomenclatureTaxonomy,
    VNomenclatureTaxonomie,
    BibNomenclaturesTypeTaxo
)
from sqlalchemy import text


USE_AS_SUBMODULE = current_app.config.get("USE_AS_SUBMODULE", True)
if USE_AS_SUBMODULE:
    DB = current_app.config["DB"]
else:
    DB = import_module(".env", "pypnnomenclature").DB


def get_nomenclature_list(
    id_type=None,
    code_type=None,
    regne=None,
    group2_inpn=None,
    hierarchy=None,
    filter_params=None,
):
    """
        Récupération de la liste des termes d'un type de nomenclature
    """

    q = DB.session.query(BibNomenclaturesTypes)
    if filter_params is None:
        filter_params = []

    if code_type:
        nomenclature = q.filter_by(mnemonique=code_type).first()
    elif id_type:
        nomenclature = q.filter_by(id_type=id_type).first()
    else:
        nomenclature = None

    if not nomenclature:
        return None

    # Terme de nomenclatures
    q = (
        DB.session.query(TNomenclatures)
        .filter_by(id_type=nomenclature.id_type)
        .filter_by(active=True)
    )

    # Filtrer sur la hiérarchie
    if hierarchy:
        q = q.filter(TNomenclatures.hierarchy.like("{}%".format(hierarchy)))
    if current_app.config["ENABLE_NOMENCLATURE_TAXONOMIC_FILTERS"]:
        # Filtrer en fonction du groupe taxonomie
        if regne:
            q = q.join(
                VNomenclatureTaxonomie,
                VNomenclatureTaxonomie.id_nomenclature
                == TNomenclatures.id_nomenclature,
            ).filter(VNomenclatureTaxonomie.regne.in_(("all", regne)))
            if group2_inpn:
                q = q.filter(
                    VNomenclatureTaxonomie.group2_inpn.in_(
                        ("all", group2_inpn))
                )
    # Ordonnancement
    if "orderby" in filter_params:
        order_col = getattr(TNomenclatures, filter_params["orderby"])

        if "order" in filter_params:
            if filter_params["order"] == "desc":
                order_col = order_col.desc()

        q = q.order_by(order_col)
    # @TODO Autres filtres
    try:
        data = q.all()
    except Exception as e:
        DB.session.rollback()
        raise

    response = nomenclature.as_dict()
    if data:
        response["values"] = [n.as_dict() for n in data]
    return response


def get_nomenclature_list_formated(nomenclature_params, mapping):
    """
        Permet de récupérer la liste des données d'une nomenclature et de la
            formater de façon particulière
        !! pour le momment ne traite que les objets de type nomenclature
            et pas nomenclature api
        exemple:
        {
            'id': {'object': 'nomenclature', 'field': 'id_nomenclature'},
            'libelle': {'object': 'nomenclature', 'field': 'label_default'}
        }
    """
    data = list()
    nomenclature_data = get_nomenclature_list(**nomenclature_params)

    if not nomenclature_data:
        return None

    if "values" not in nomenclature_data:
        return data

    for term in nomenclature_data["values"]:
        data.append({val: term[mapping[val]["field"]] for val in mapping})

    return data


def get_nomenclature_with_taxonomy_list():
    """
        Fetch nomenclature definition list with taxonomy
    """

    q = DB.session.query(BibNomenclaturesTypeTaxo).order_by("mnemonique")

    nomenclature_types = q.all()
    data = list()

    for t in nomenclature_types:
        nomenclature_type_dict = t.as_dict(
            columns=[
                "id_type",
                "mnemonique",
                "label_default",
                "label_de",
                "label_en",
                "label_es",
                "label_fr",
                "label_it",
            ]
        )

        nomenclatures = list()

        for n in t.nomenclatures:
            nomenclature_dict = n.as_dict(columns=[
                "id_nomenclature",
                "cd_nomenclature",
                "mnemonique",
                "hierarchy",
                "label_default",
                "label_de",
                "label_en",
                "label_es",
                "label_fr",
                "label_it",
            ])

            nomenclature_dict["taxref"] = [tr.as_dict(columns=["regne", "group2_inpn"])
                                           for tr in n.taxref]

            nomenclatures.append(nomenclature_dict)

        nomenclature_type_dict["nomenclatures"] = nomenclatures

        data.append(nomenclature_type_dict)

    return data


def get_nomenclature_id_term(cd_type, cd_term, raise_exp=True):
    """
        Fonction retournant l'identifiant d'un term
        à partir de ses codes mnemoniques

        paramètres:
        ----------
            cd_type : code mnemonique du type de vocabulaire
            cd_term : code du terme recherché
            raise_exp : spécifie le comportement de la
                fonction en cas d'exeception
    """

    t = text("SELECT ref_nomenclatures.get_id_nomenclature(:cd_type, :cd_term) as id")
    try:
        value = (
            DB.session.query("id")
            .from_statement(t.params(cd_type=cd_type, cd_term=cd_term))
            .first()
        )
        return value
    except Exception as e:
        if raise_exp:
            raise e
        return None
