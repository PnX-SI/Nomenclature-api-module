from sqlalchemy import inspect
from marshmallow_sqlalchemy.convert import ModelConverter
from marshmallow.fields import Nested

from .models import TNomenclatures as Nomenclature
from .schemas import NomenclatureSchema

"""
This converter automatically add Nested(NomenclatureSchema) fields
for all relationships to Nomenclature model.

Usage:

    class MyModel(db.Model):
        nomenclature_foo = relationships(Foo)

    class MyModelSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = MyModel
            include_fk = True
            model_converter = NomenclaturesConverter
"""


class NomenclaturesConverter(ModelConverter):
    def fields_for_model(self, model, **kwargs):
        fields = super().fields_for_model(model, **kwargs)
        mapper = inspect(model)
        for key, rel in mapper.relationships.items():
            if rel.entity.class_ == Nomenclature:
                fields[key] = Nested(NomenclatureSchema)
        return fields


"""
Add a property __nomenclatures__ on a Model class to list
all relationships to Nomenclature.

Usage:

    from pypnnomenclature.models import TNomenclatures as Nomenclature
    from pypnnomenclature.utils import NomenclaturesMixin

    class MyModel(NomenclaturesMixin, db.Model):
        id_nomenclature_foo = db.Column(db.Integer, ForeignKey(Nomenclature.id_nomenclature))
        nomenclature_foo = relationships(Nomenclature, foreign_keys=[id_nomenclature_foo])

    assert(MyModel.__nomenclatures__ == ['nomenclature_foo'])
"""


class NomenclaturesMixin:
    @classmethod
    def __declare_last__(cls):
        mapper = inspect(cls)
        cls.__nomenclatures__ = [
            key for key, rel in mapper.relationships.items() if rel.entity.class_ == Nomenclature
        ]
