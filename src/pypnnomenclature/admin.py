from flask import current_app
from flask_admin import expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.filters import BaseSQLAFilter
from .env import DB
from .models import (
    TNomenclaturesAdmin,
    BibNomenclaturesTypesAdmin
)


class TNomenclatureFiltersType(BaseSQLAFilter):

    # Override to create an appropriate query and apply a filter to
    # said query with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(TNomenclaturesAdmin.id_type == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return u'equals'

    def get_options(self, view):
        return [
            (nomenclature.id_type, nomenclature.label_default)
            for nomenclature
            in BibNomenclaturesTypesAdmin.query.order_by(BibNomenclaturesTypesAdmin.label_default)  # noqa
        ]


class TNomenclatureFiltersMnemonique(BaseSQLAFilter):

    # Override to create an appropriate query and apply a filter to
    # said query with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(TNomenclaturesAdmin.id_type == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return u'equals'

    def get_options(self, view):
        return [
            (nomenclature.id_type, nomenclature.mnemonique)
            for nomenclature
            in BibNomenclaturesTypesAdmin.query.order_by(BibNomenclaturesTypesAdmin.mnemonique)  # noqa
        ]


class TNomenclatureFiltersId(BaseSQLAFilter):

    # Override to create an appropriate query and apply a filter to said query
    # with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(TNomenclaturesAdmin.id_nomenclature == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return u'equals'


class TNomenclaturesAdminConfig(ModelView):
    page_size = 10
    form_columns = [
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
        TNomenclatureFiltersId(column=None, name='Id nomenclature'),
        TNomenclatureFiltersMnemonique(column=None, name='Mnemonique'),
    ]

    # Need this so the filter options are always up-to-date
    @expose('/')
    def index_view(self):
        self._refresh_filters_cache()
        return super(TNomenclaturesAdminConfig, self).index_view()


class BibNomenclatureFiltersLabel(BaseSQLAFilter):
    # Override to create an appropriate query and apply a filter to said query
    # with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(BibNomenclaturesTypesAdmin.label_default == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return u'equals'

    def get_options(self, view):
        return [
            (nomenclature.label_default, nomenclature.label_default)
            for nomenclature
            in BibNomenclaturesTypesAdmin.query.order_by(BibNomenclaturesTypesAdmin.label_default)  # noqa
        ]


class BibNomenclatureFiltersID(BaseSQLAFilter):

    # Override to create an appropriate query and apply a filter to said query
    # with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(BibNomenclaturesTypesAdmin.id_type == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return u'equals'


class BibNomenclatureFiltersMnemonique(BaseSQLAFilter):

    # Override to create an appropriate query and apply a filter to said query
    # with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(BibNomenclaturesTypesAdmin.mnemonique == value)

    def get_options(self, view):
        return [
            (nomenclature.mnemonique, nomenclature.mnemonique)
            for nomenclature
            in BibNomenclaturesTypesAdmin.query.order_by(BibNomenclaturesTypesAdmin.mnemonique)  # noqa
        ]

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return u'equals'


class BibNomenclaturesTypesAdminConfig(ModelView):
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
        BibNomenclatureFiltersID(column=None, name='Id type'),
        BibNomenclatureFiltersMnemonique(column=None, name='Mnémonique')
    ]

    # Need this so the filter options are always up-to-date
    @expose('/')
    def index_view(self):
        self._refresh_filters_cache()
        return super(BibNomenclaturesTypesAdminConfig, self).index_view()
