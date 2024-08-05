from flavor_services import entities


class Dimension(entities.Object):
    def __init__(self, json):
        super().__init__()
        self.name = extract_field(json, "name")
        self.unit_type = extract_field(json, "unit_type")
        self.value = extract_field(json, "value")
        self.description = extract_field(json, "description")


class Race(entities.Entity):
    def __init__(self, json):
        super().__init__(extract_field(json, "uuid"))
        self.name = extract_field(json, "name")
        self.world_id = extract_field(json, "world_id")
        self.characteristics = extract_field(json, "characteristics")
        self.description = extract_field(json, "description")


def extract_field(json, field):
    try:
        return json[field]
    except KeyError as err:
        print(f"Field {field} not found")
        return None


class Skill(entities.Entity):

    def __init__(self, uuid, name, **kwargs):
        super().__init__(uuid)
        self.name = name
        self.description = kwargs.get("description")


class CharacterSkill(entities.Object):
    def __init__(self, json):
        super().__init__()
        self.skill_id = extract_field(json, "skill_id")
        self.name = extract_field(json, "name")
        self.skill_value = extract_field(json, "skill_value")
        self.description = extract_field(json, "description")


class CharacterStat(entities.Object):
    def __init__(self, json):
        super().__init__()
        self.stat_id = extract_field(json, "stat_id")
        self.name = extract_field(json, "name")
        self.stat_value = extract_field(json, "stat_value")
        self.description = extract_field(json, "description")


class Character(entities.Entity):
    skills: [CharacterSkill] = []
    stats: [CharacterStat] = []
    dimensions: [Dimension] = []
    race: [Race]

    def __init__(self, json):
        super().__init__(extract_field(json, "uuid"))
        self.name = extract_field(json, "name")
        self.summary = extract_field(json, "summary")
        self.appearance = extract_field(json, "appearance")
        self.personality = extract_field(json, "personality")
        self.background = extract_field(json, "background")
        self.sex = extract_field(json, "sex")
        self.race = Race(extract_field(json, "race"))
        if extract_field(json, "dimensions") is not None:
            for dim in extract_field(json, "dimensions"):
                self.dimensions.append(Dimension(dim))
        self.user = extract_field(json, "user")
        self.inventory = extract_field(json, "inventory")
        if extract_field(json, "stats") is not None:
            for stat in json["stats"]:
                self.stats.append(CharacterStat(stat))
        if extract_field(json, "skills") is not None:
            for skill in json["skills"]:
                self.skills.append(CharacterSkill(skill))


def __str__(self):
    return self.name
