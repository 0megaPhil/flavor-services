from rest_framework.request import Request

from flavor_services.generated_client.input_types import *
from flavor_services.views import FlavorFactory, FlavorApiView


class AttributeApiView(FlavorApiView):

    def __init__(self, **kwargs):
        super().__init__(FlavorFactory(AttributeInput()), **kwargs)

    def post(self, request: Request):
        return self.post_resolver(request)
