from rest_framework import serializers

from flavor_services import entities


class Flavor(entities.Object):

    def __init__(self, uuid, object_type, text):
        super().__init__()
        self.targetId = uuid
        self.objectType = object_type
        self.text = text
