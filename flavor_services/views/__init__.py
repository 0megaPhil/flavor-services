from typing import List

from camel_converter import dict_to_snake
from django.http import HttpResponse
from pydantic.v1.utils import to_camel
from rest_framework.request import Request
from rest_framework.views import APIView

from flavor_services.generated.services_models import FlavorInput, CommonObject, schema_dumps, AttributeInput
from flavor_services.views.flavor_factory import FlavorFactory
from flavor_services.views.flavor_factory import FlavorFactory


class FlavorApiView(APIView):
    flavor = FlavorFactory
    entity_type: CommonObject
    entity_name: str

    def __init__(self, flavor: FlavorFactory, **kwargs):
        super().__init__(**kwargs)
        self.flavor = flavor
        self.entity_type = flavor.entity_type
        self.entity_name = flavor.entity_name

    @staticmethod
    def detail_entities(entity) -> List[CommonObject]:
        details: List[CommonObject] = []
        for entry in entity.entries:
            if hasattr(entry, "attribute"):
                attribute: AttributeInput = entry.attribute
                if hasattr(attribute, "type"):
                    entry.type = attribute.type
                else:
                    entry.type = "OTHER"
                if hasattr(attribute, "rarity"):
                    entry.rarity = attribute.rarity
                else:
                    entry.rarity = "OTHER"
                details.append(entry)
        return details

    def post_resolver(self, request: Request):
        self.flavor.features.clear()
        body_dict: dict = request.data
        print(body_dict)
        req_snake = dict_to_snake(body_dict)
        entity: CommonObject = self.entity_type.from_dict(req_snake)
        detail_entities = self.detail_entities(entity)
        if detail_entities is not None and len(detail_entities) > 0:
            flavor = self.generate_flavor(entity, detail_entities)
        else:
            flavor = FlavorInput
        json_str = schema_dumps(flavor)
        camel_json = to_camel(json_str)
        return HttpResponse(camel_json)

    def generate_flavor(self, parent_entity: [CommonObject], entities: List[CommonObject]):
        target_id: str = parent_entity.get_id()
        self.flavor.initialize_all(target_id, entities)
        self.flavor.start_all(target_id)
        self.flavor.join_all(target_id)
        flavor = self.flavor.complete_flavor(parent_entity.get_flavor_type(), target_id)
        print(flavor)
        return flavor
