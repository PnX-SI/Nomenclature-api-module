'''
    Méthode permettant de manipuler les objets de la nomenclature
'''
from .models import (
    VNomenclatureTaxonomie,
    TNomenclatures,
    BibNomenclaturesTypes
)
from .env import DB



def get_nomenclature_list(
    id_type, regne=None, group2_inpn=None, hierarchy=None, filter=None
):
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
    

    # Ordonnancement
    if 'orderby' in filter:
        orderCol = getattr(
            TNomenclatures,
            filter['orderby']
        )

        if 'order' in filter:
            if filter['order'] == 'desc':
                orderCol = orderCol.desc()

        q = q.order_by(orderCol)
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
    '''
        Permet de récupérer la liste des données d'une nomenclature et de la 
            formater de façon particulière
        !! pour le momment ne traite que les objets de type nomenclature 
            et pas nomenclature api
        exemple: 
        {
            'id': {'object': 'nomenclature', 'field': 'id_nomenclature'},
            'libelle': {'object': 'nomenclature', 'field': 'label_default'}
        }
    '''
    data = list()
    nomenclature_data = get_nomenclature_list(**nomenclature_params)

    if 'values' not in nomenclature_data:
        return data

    for term in nomenclature_data['values']:
        data.append({val: term[mapping[val]['field']] for val in mapping})

    return data