from importlib import import_module
from functools import partial

from flask import has_app_context, g
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.filters import BaseSQLAFilter
from .models import TNomenclatures, BibNomenclaturesTypes
from .env import db
from sqlalchemy import select


# https://github.com/flask-admin/flask-admin/issues/1807
# https://stackoverflow.com/questions/54638047/correct-way-to-register-flask-admin-views-with-application-factory
class ReloadingIterator:
    def __init__(self, iterator_factory):
        self.iterator_factory = iterator_factory

    def __iter__(self):
        return self.iterator_factory()


class TNomenclatureFiltersType(BaseSQLAFilter):
    # Override to create an appropriate query and apply a filter to
    # said query with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(TNomenclatures.id_type == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return "equals"

    def get_dynamic_options(self, view):
        if has_app_context():
            if not hasattr(g, "TNomenclatureFiltersType"):
                bib_nomenc_labels = db.session.scalars(
                    db.select(BibNomenclaturesTypes).order_by(BibNomenclaturesTypes.label_default)
                ).all()
                g.TNomenclatureFiltersType = [
                    (nomenclature.id_type, nomenclature.label_default)
                    for nomenclature in bib_nomenc_labels  # noqa
                ]
            yield from g.TNomenclatureFiltersType

    def get_options(self, view):
        return ReloadingIterator(partial(self.get_dynamic_options, view))


class TNomenclatureFiltersMnemonique(BaseSQLAFilter):
    # Override to create an appropriate query and apply a filter to
    # said query with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(TNomenclatures.id_type == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return "equals"

    def get_dynamic_options(self, view):
        if has_app_context():
            if not hasattr(g, "TNomenclatureFiltersMnemonique"):
                bib_nomenc_type = db.session.scalars(
                    db.select(BibNomenclaturesTypes).order_by(BibNomenclaturesTypes.mnemonique)
                ).all()
                g.TNomenclatureFiltersMnemonique = [
                    (nomenclature.id_type, nomenclature.mnemonique)
                    for nomenclature in bib_nomenc_type  # noqa
                ]
            yield from g.TNomenclatureFiltersMnemonique

    def get_options(self, view):
        return ReloadingIterator(partial(self.get_dynamic_options, view))


class TNomenclatureFiltersId(BaseSQLAFilter):
    # Override to create an appropriate query and apply a filter to said query
    # with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(TNomenclatures.id_nomenclature == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return "equals"


class TNomenclaturesAdmin(ModelView):
    page_size = 10
    form_columns = [
        "nomenclature_type",
        "cd_nomenclature",
        "mnemonique",
        "label_fr",
        "definition_fr",
        "label_default",
        "definition_default",
        "statut",
        "active",
        "hierarchy",
        "id_broader",
    ]
    column_list = [
        "id_nomenclature",
        "nomenclature_type",
        "mnemonique",
        "cd_nomenclature",
        "label_default",
        "definition_default",
        "label_fr",
        "definition_fr",
        "id_type",
        "statut",
        "active",
    ]
    page_size = 15

    column_filters = [
        TNomenclatureFiltersType(column=None, name="Type de nomenclature"),
        TNomenclatureFiltersId(column=None, name="Id nomenclature"),
        TNomenclatureFiltersMnemonique(column=None, name="Mnemonique"),
    ]


class BibNomenclatureFiltersLabel(BaseSQLAFilter):
    # Override to create an appropriate query and apply a filter to said query
    # with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(BibNomenclaturesTypes.label_default == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return "equals"

    def get_dynamic_options(self, view):
        if has_app_context():
            if not hasattr(g, "BibNomenclatureFiltersLabel"):
                nomenc_def_label = db.session.scalars(
                    select(BibNomenclaturesTypes).order_by(BibNomenclaturesTypes.label_default)
                ).all()
                g.BibNomenclatureFiltersLabel = [
                    (nomenclature.label_default, nomenclature.label_default)
                    for nomenclature in nomenc_def_label  # noqa
                ]
            yield from g.BibNomenclatureFiltersLabel

    def get_options(self, view):
        return ReloadingIterator(partial(self.get_dynamic_options, view))


class BibNomenclatureFiltersID(BaseSQLAFilter):
    # Override to create an appropriate query and apply a filter to said query
    # with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(BibNomenclaturesTypes.id_type == value)

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return "equals"


class BibNomenclatureFiltersMnemonique(BaseSQLAFilter):
    # Override to create an appropriate query and apply a filter to said query
    # with the passed value from the filter UI
    def apply(self, query, value, alias=None):
        return query.filter(BibNomenclaturesTypes.mnemonique == value)

    def get_dynamic_options(self, view):
        if has_app_context():
            if not hasattr(g, "BibNomenclatureFiltersMnemonique"):
                nomenc_mnemonique = db.session.scalars(
                    select(BibNomenclaturesTypes).order_by(BibNomenclaturesTypes.mnemonique)
                ).all()
                g.BibNomenclatureFiltersMnemonique = [
                    (nomenclature.mnemonique, nomenclature.mnemonique)
                    for nomenclature in nomenc_mnemonique  # noqa
                ]
            yield from g.BibNomenclatureFiltersMnemonique

    def get_options(self, view):
        return ReloadingIterator(partial(self.get_dynamic_options, view))

    # readable operation name. This appears in the middle filter line drop-down
    def operation(self):
        return "equals"


class BibNomenclaturesTypesAdmin(ModelView):
    page_size = 10
    column_list = [
        "id_type",
        "mnemonique",
        "label_default",
        "definition_default",
        "label_fr",
        "source",
        "statut",
    ]
    column_display_pk = True
    form_columns = [
        "mnemonique",
        "label_default",
        "definition_default",
        "label_fr",
        "definition_fr",
        "source",
        "statut",
    ]

    column_filters = [
        BibNomenclatureFiltersLabel(column=None, name="Type de nomenclature"),
        BibNomenclatureFiltersID(column=None, name="Id type"),
        BibNomenclatureFiltersMnemonique(column=None, name="Mnémonique"),
    ]
