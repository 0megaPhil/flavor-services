import jsonpickle


class Entity:
    def __init__(self, uuid):
        self.uuid = uuid

    def to_json(self):
        return jsonpickle.encode(self, indent=4)


class Object:
    def to_json(self):
        return jsonpickle.encode(self, indent=4)
