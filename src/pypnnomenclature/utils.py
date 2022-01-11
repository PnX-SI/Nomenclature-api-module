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

    class MyModel(NomenclaturesMixin, db.Model):
        nomenclature_foo = relationships(Foo)

    assert(MyModel.__nomenclatures__ == ['nomenclature_foo'])
"""
class NomenclaturesMixin:
    @classmethod
    def __declare_last__(cls):
        mapper = inspect(cls)
        cls.__nomenclatures__ = [
            key
            for key, rel in mapper.relationships.items()
            if rel.entity.class_ == Nomenclature
        ]
