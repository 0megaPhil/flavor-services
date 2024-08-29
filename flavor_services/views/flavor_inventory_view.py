from typing import List

from rest_framework.request import Request

from flavor_services.generated_client.input_types import PlayerInput, CommonObject, apply_details
from flavor_services.views import FlavorApiView
from flavor_services.views.flavor_factory import FlavorFactory


class InventoryApiView(FlavorApiView):

    def __init__(self, **kwargs):
        super().__init__(FlavorFactory(PlayerInput()), **kwargs)

    def detail_entities(self, entity) -> List[CommonObject]:
        details: List[CommonObject] = apply_details(entity.items, [])
        details = apply_details(entity.currencies, details)
        return details

    def post(self, request: Request):
        return self.post_resolver(request)
