from rest_framework.request import Request

from flavor_services.generated_client import RaceInput
from flavor_services.views import FlavorApiView, FlavorFactory


class RaceApiView(FlavorApiView):
    def __init__(self, **kwargs):
        super().__init__(FlavorFactory(RaceInput), **kwargs)

    def post(self, request: Request):
        return self.post_resolver(request)
