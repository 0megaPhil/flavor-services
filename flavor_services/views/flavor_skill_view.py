from rest_framework.request import Request

from flavor_services.generated_client import SkillInput
from flavor_services.views import FlavorFactory, FlavorApiView

system_prompt = r'''You are a dungeon master in a grim dark setting'''


class SkillApiView(FlavorApiView):
    def __init__(self, **kwargs):
        super().__init__(FlavorFactory(SkillInput()), **kwargs)

    def post(self, request: Request):
        return self.post_resolver(request)
