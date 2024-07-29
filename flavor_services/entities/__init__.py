import json

from django.db import models


class Entity(models.Model):
    def __init__(self, uuid, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uuid = uuid

    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)


class Object(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def to_json(self):
        self.id = None
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)


class Attribute(models.Model):
    def __init__(self, key, value, description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key = key
        self.value = value
        self.description = description

    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)
