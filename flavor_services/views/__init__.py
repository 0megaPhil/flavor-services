from typing import List

from camel_converter import dict_to_snake
from django.http import HttpResponse
from pydantic.v1.utils import to_camel
from rest_framework.request import Request
from rest_framework.views import APIView

from flavor_services.generated_client.input_types import FlavorInput, CommonObject, schema_dumps
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

    def detail_entities(self, entity) -> List[CommonObject]:
        return [entity]

    def post_resolver(self, request: Request):
        self.flavor.characteristics.clear()
        body_dict: dict = request.data
        print(body_dict)
        entity = self.entity_type.from_dict(dict_to_snake(body_dict))
        detail_entities = self.detail_entities(entity)
        if detail_entities is not None and len(detail_entities) > 0:
            flavor = self.generate_flavor(entity.id, detail_entities)
        else:
            flavor = FlavorInput
        json_str = schema_dumps(flavor)
        camel_json = to_camel(json_str)
        return HttpResponse(camel_json)

    def generate_flavor(self, target_id: str, entities: List[CommonObject]):
        for detail in entities:
            self.flavor.initialize_prompt(detail)
        self.flavor.start_all()
        self.flavor.join_all()
        flavor = self.flavor.complete_flavor(target_id)
        print(flavor)
        return flavor
