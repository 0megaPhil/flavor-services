from rest_framework.request import Request

from flavor_services.generated.services_models import *
from flavor_services.views import FlavorApiView
from flavor_services.views.flavor_factory import FlavorFactory


class ItemApiView(FlavorApiView):

    def __init__(self, **kwargs):
        super().__init__(FlavorFactory(ItemInput()), **kwargs)

    def post(self, request: Request):
        return self.post_resolver(request)
