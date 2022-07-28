from pypnnomenclature.env import ma
from pypnnomenclature.models import TNomenclatures


class NomenclatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TNomenclatures
        load_instance = True
        exclude = (
            "label_en",
            "definition_en",
            "label_es",
            "definition_es",
            "label_de",
            "definition_de",
            "label_it",
            "definition_it",
            "meta_create_date",
            "meta_update_date",
        )
        include_fk = True
