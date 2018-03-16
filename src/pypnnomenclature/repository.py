'''
    Méthode permettant de manipuler les objets de la nomenclature
'''
from .models import (
    VNomenclatureTaxonomie,
    TNomenclatures,
    BibNomenclaturesTypes
)
from .env import DB

def get_nomenclature_list(id_type, regne=None, group2_inpn=None, hierarchy=None, filter=None):
    '''
        Récupération de la liste des termes d'un type de nomenclature
    '''
    nomenclature = DB.session.query(BibNomenclaturesTypes)\
        .filter_by(id_type=id_type).first()

    if (not nomenclature):
        return None

    # Terme de nomenclatures
    q = DB.session.query(TNomenclatures)\
        .filter_by(id_type=id_type)\
        .filter_by(active=True)

    # Filtrer en fonction du groupe taxonomie
    if regne:
        q = q.join(
            VNomenclatureTaxonomie,
            VNomenclatureTaxonomie.id_nomenclature ==
            TNomenclatures.id_nomenclature
        ).filter(VNomenclatureTaxonomie.regne.in_(('all', regne)))
        if group2_inpn:
            q = q.filter(
                VNomenclatureTaxonomie.group2_inpn.in_(('all', group2_inpn))
            )

    # Filtrer sur la hiérarchie
    if hierarchy:
        q = q.filter(TNomenclatures.hierarchy.like("{}%".format(hierarchy)))

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
