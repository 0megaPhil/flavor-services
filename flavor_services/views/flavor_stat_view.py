from rest_framework.request import Request

from flavor_services.generated_client import StatInput
from flavor_services.views import FlavorApiView, FlavorFactory


class StatApiView(FlavorApiView):
    def __init__(self, **kwargs):
        super().__init__(FlavorFactory(StatInput()), **kwargs)

    def post(self, request: Request):
        return self.post_resolver(request)
