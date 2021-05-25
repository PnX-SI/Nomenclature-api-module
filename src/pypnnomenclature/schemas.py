from pypnnomenclature.env import MA 
from pypnnomenclature.models import TNomenclatures

class NomenclatureSchema(MA.SQLAlchemyAutoSchema):
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
            "meta_update_date"
        )