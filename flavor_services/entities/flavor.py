from flavor_services import entities


class Flavor(entities.Object):

    def __init__(self, uuid, object_type, **kwargs):
        super().__init__()
        self.target_id = uuid
        self.object_type = object_type
        self.appearance = kwargs.get('appearance')
        self.background = kwargs.get('background')
        self.personality = kwargs.get('personality')
        self.summary = kwargs.get('summary')
