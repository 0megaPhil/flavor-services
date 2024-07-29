from flavor_service.dialog import Dialog
from flavor_service.entities import Entity


class DialogStatement(Dialog):
    def __init__(self, entity: Entity):
        super().__init__(entity)
