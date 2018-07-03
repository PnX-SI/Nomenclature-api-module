from flask import current_app
from flask_admin import Admin, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.filters import BaseSQLAFilter
from .env import DB
from .models import (
    TNomenclatures,
    BibNomenclaturesTypes
)


class TNomenclatureFiltersType(BaseSQLAFilter):

    # Override to create an appropriate query and apply a filter to
    # said query with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(TNomenclatures.id_type == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return u'equals'

    def get_options(self, view):
        return [
            (nomenclature.id_type, nomenclature.label_default)
            for nomenclature
            in BibNomenclaturesTypes.query.order_by(BibNomenclaturesTypes.label_default) # noqa
        ]


class TNomenclatureFiltersId(BaseSQLAFilter):

    # Override to create an appropriate query and apply a filter to said query
    # with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(TNomenclatures.id_nomenclature == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return u'equals'


class TNomenclaturesAdmin(ModelView):
    page_size = 10
    form_columns = [
      'id_nomenclature',
      'nomenclature_type_name',
      'cd_nomenclature',
      'mnemonique',
      'label_fr',
      'definition_fr',
      'label_default',
      'definition_default',
      'statut',
      'active',
      'hierarchy',
      'id_broader'
    ]
    column_list = [
      'id_nomenclature',
      'nomenclature_type_name',
      'mnemonique',
      'cd_nomenclature',
      'label_default',
      'definition_default',
      'label_fr',
      'definition_fr',
      'id_type',
      'statut',
      'active'
    ]
    page_size = 15

    column_filters = [
        TNomenclatureFiltersType(column=None, name='Type de nomenclature'),
        TNomenclatureFiltersId(column=None, name='Id nomenclature')
        ]

    # Need this so the filter options are always up-to-date
    @expose('/')
    def index_view(self):
        self._refresh_filters_cache()
        return super(TNomenclaturesAdmin, self).index_view()


class BibNomenclatureFiltersLabel(BaseSQLAFilter):
    # Override to create an appropriate query and apply a filter to said query
    # with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(BibNomenclaturesTypes.label_default == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return u'equals'

    def get_options(self, view):
        return [
            (nomenclature.label_default, nomenclature.label_default)
            for nomenclature
            in BibNomenclaturesTypes.query.order_by(BibNomenclaturesTypes.label_default) # noqa
        ]


class BibNomenclatureFiltersID(BaseSQLAFilter):

    # Override to create an appropriate query and apply a filter to said query
    # with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(BibNomenclaturesTypes.id_type == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return u'equals'

    # def get_options(self, view):
    #     return [(nomenclature.label_default, nomenclature.label_default)
    #      for nomenclature in BibNomenclaturesTypes.query.order_by(BibNomenclaturesTypes.label_default)]


class BibNomenclaturesTypesAdmin(ModelView):
    page_size = 10
    column_list = [
      'id_type',
      'mnemonique',
      'label_default',
      'definition_default',
      'label_fr',
      'source',
      'statut'
    ]
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

    column_filters = [
        BibNomenclatureFiltersLabel(column=None, name='Type de nomenclature'),
        BibNomenclatureFiltersID(column=None, name='Id type')
        ]

    # Need this so the filter options are always up-to-date
    @expose('/')
    def index_view(self):
        self._refresh_filters_cache()
        return super(BibNomenclaturesTypesAdmin, self).index_view()


"""
    Configuration de l'admin
"""
admin = Admin(
  current_app,
  name="Backoffice d'administration des nomenclatures",
  template_mode='bootstrap3',
  url='/nomenclatures/admin',
)

admin.add_view(
    BibNomenclaturesTypesAdmin(
        BibNomenclaturesTypes, DB.session, name="Type de nomenclatures"
    )
)

admin.add_view(
    TNomenclaturesAdmin(
        TNomenclatures, DB.session, name="Items de nomenclatures"
    )
)