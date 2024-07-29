from flavor_services.entities import Entity


class Item(Entity):
    def __init__(self, uuid, name, description, **kwargs):
        super().__init__(uuid)
        self.name = name
        self.description = description
        self.attributes = dict(kwargs)
