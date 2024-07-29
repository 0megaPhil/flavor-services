import json

from rest_framework import serializers
from flavor_services import entities


class CharacterStat(entities.Attribute):
    def __init__(self, key, value, description, *args, **kwargs):
        super().__init__(key, value, description, *args, **kwargs)


class Character(entities.Entity):
    stats = []

    def __init__(self, name, uuid, stats: list[CharacterStat], **kwargs):
        super().__init__(uuid)
        self.name = name
        self.gender = kwargs.get("gender")
        self.description = kwargs.get("description")
        self.inventory_id = kwargs.get("inventory_id")
        self.user_id = kwargs.get("user_id")
        self.weight = kwargs.get("weight")
        self.height = kwargs.get("height")
        self.age = kwargs.get("age")
        self.stats = stats

def __str__(self):
    return self.name
