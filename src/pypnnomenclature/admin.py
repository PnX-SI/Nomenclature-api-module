from flask import current_app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .env import DB
from .models import (
    TNomenclatures,
    BibNomenclaturesTypes
)


class TNomenclaturesAdmin(ModelView):
    page_size = 10
    column_searchable_list = ['id_type', 'mnemonique', 'id_nomenclature']
    form_columns = ['id_nomenclature','nomenclature_type_name', 'cd_nomenclature', 'mnemonique', 'label_fr', 'definition_fr' , 'label_default', 'definition_default', 'statut', 'active', 'hierarchy', 'id_broader']
    column_list = ['id_nomenclature','nomenclature_type_name', 'mnemonique','cd_nomenclature','label_default','definition_default', 'label_fr', 'definition_fr', 'id_type', 'statut', 'active']
    page_size = 15    

class BibNomenclaturesTypesAdmin(ModelView):
    page_size = 10
    column_searchable_list = ['label_default', 'id_type']
    column_list = ['id_type', 'mnemonique', 'label_default', 'definition_default', 'label_fr', 'source', 'statut'  ]
    column_display_pk = True
    form_columns = [
      'id_type',
      'mnemonique',
      'label_default',
      'definition_default',
      'label_fr',
      'definition_fr',
      'source',
      'statut'
    ]


admin = Admin(
  current_app,
  name="Backoffice d'administration des nomenclatures",
  template_mode='bootstrap3',
  url='/nomenclatures/admin',
  )
admin.add_view(BibNomenclaturesTypesAdmin(BibNomenclaturesTypes, DB.session, name="Nomenclatures"))
admin.add_view(TNomenclaturesAdmin(TNomenclatures, DB.session, name="Items de nomenclatures"))



