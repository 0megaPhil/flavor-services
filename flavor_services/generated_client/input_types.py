import json
import uuid
from dataclasses import dataclass as dc, field
from typing import List, Optional, Dict

import marshmallow_dataclass
from marshmallow import Schema

from .enums import (
    MagicLevels,
    Sexes,
    TechLevels, Species,
)


@dc
class CommonObject:
    id = None
    schema = None
    entity_type = None
    entity_name = None

    def get_id(self) -> str:
        if self.id is None and not isinstance(self, CommonObject):
            self.id = uuid.uuid4().__str__()
            print("Warning, no id, using uuid", self.id)
        return self.id

    def __str__(self):
        return self.get_schema().dumps(self)

    def get_schema(self):
        if self.schema is None and self.__class__ != CommonObject:
            self.schema = marshmallow_dataclass.class_schema(self.__class__)()
        return self.schema

    def from_dict(self, obj_dict: Dict):
        return self.get_schema().load(obj_dict)

    def from_json(self, obj_json: str):
        return self.get_schema().loads(obj_json)

    def get_name(self):
        if self.entity_name is None and self.__class__ != CommonObject:
            self.entity_name = self.__class__.__name__.replace("Input", "").lower()
        return self.entity_name

    def get_title(self):
        if hasattr(self, 'type'):
            title = f"{self.type} - {self.get_name()}"
        else:
            title = self.get_name()
        return title


def apply_details(entities, details: List[CommonObject] or None) -> List[CommonObject]:
    if details is None:
        details = []
    if entities is not None:
        if isinstance(entities, List):
            for detail in entities:
                details.append(detail)
        if isinstance(entities, CommonObject):
            details.append(entities)
    return details


def schema_dumps(entities):
    if entities is not None:
        if isinstance(entities, List):
            return json.dumps([json.loads(str(entity)) for entity in entities], indent=2)
        elif isinstance(entities, CommonObject):
            return entities.get_schema().dumps(entities, indent=2)
    return json.dumps(entities, indent=2)


def schema_dumps_set(entities) -> List[str]:
    json_list = [str]
    if entities is not None:
        for entity in entities:
            json_list.append(schema_dumps(entity))
    return json_list


@dc
class AttributeInput(CommonObject):
    type: Optional[str] = field(default_factory=str)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)
    name: Optional[str] = field(default_factory=str)
    prompt: Optional[str] = field(default_factory=str)


@dc
class CharacteristicInput(CommonObject):
    target_id: Optional[str] = field(default_factory=str)
    title: Optional[str] = field(default_factory=str)
    description: Optional[str] = field(default_factory=str)


@dc
class CreatureInput(CommonObject):
    type: Optional[str] = field(default_factory=str)
    name: Optional[str] = field(default_factory=str)
    attributes: Optional[List[Optional["AttributeEntry"]]] = field(default_factory=list)
    features: Optional[List[Optional["FeatureInput"]]] = field(default_factory=list)
    histories: Optional[List[Optional["HistoryInput"]]] = field(default_factory=list)
    dimensions: Optional[List[Optional["DimensionInput"]]] = field(default_factory=list)
    effects: Optional[List[Optional["EffectEntry"]]] = field(default_factory=list)
    skills: Optional[List[Optional["SkillEntry"]]] = field(default_factory=list)
    stats: Optional[List[Optional["StatEntry"]]] = field(default_factory=list)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)
    inventory: Optional["InventoryInput"] = field(default=None)
    profession: Optional["ProfessionInput"] = field(default=None)
    prompt: Optional[str] = field(default_factory=str)
    sex: Optional[Sexes] = field(default=Sexes.OTHER)


@dc
class CurrencyInput(CommonObject):
    name: Optional[str] = field(default_factory=str)
    prompt: Optional[str] = field(default_factory=str)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)


@dc
class DimensionInput(CommonObject):
    title: Optional[str] = field(default_factory=str)
    value: Optional[float] = field(default=0)
    unit_type: Optional[str] = field(default_factory=str)
    percentile: Optional[str] = field(default=None)


@dc
class DistributionInput(CommonObject):
    title: Optional[str] = field(default_factory=str)
    type: Optional[str] = field(default_factory=str)
    veryBelowAverage: Optional[float] = field(default_factory=float)
    belowAverage: Optional[float] = field(default_factory=float)
    average: Optional[float] = field(default_factory=float)
    aboveAverage: Optional[float] = field(default_factory=float)
    veryAboveAverage: Optional[float] = field(default_factory=float)


@dc
class FeatureInput(CommonObject):
    schema: Schema
    target_id: Optional[str] = field(default_factory=str)
    title: Optional[str] = field(default_factory=str)
    description: Optional[str] = field(default_factory=str)
    type: Optional[str] = field(default_factory=str)
    rarity: Optional[str] = field(default_factory=str)


@dc
class HistoryInput(CommonObject):
    target_id: Optional[str] = field(default_factory=str)
    title: Optional[str] = field(default_factory=str)
    description: Optional[str] = field(default_factory=str)
    type: Optional[str] = field(default_factory=str)


@dc
class EffectInput(CommonObject):
    type: Optional[str] = field(default_factory=str)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)
    name: Optional[str] = field(default_factory=str)
    prompt: Optional[str] = field(default_factory=str)
    distribution: Optional["DistributionInput"] = field(default=None)


@dc
class Filter(CommonObject):
    by_field: Optional[str] = field(default_factory=str)
    for_value: Optional[str] = field(default_factory=str)


@dc
class FlavorInput(CommonObject):
    target_id: Optional[str] = field(default_factory=str)
    type: Optional[str] = field(default_factory=str)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default_factory=str)


@dc
class InventoryCurrencyInput(CommonObject):
    currency: Optional["CurrencyInput"] = field(default=None)
    value: Optional[float] = field(default_factory=float)


@dc
class InventoryInput(CommonObject):
    currencies: Optional[List[Optional["InventoryCurrencyInput"]]] = field(default_factory=list)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)
    items: Optional[List[Optional["InventoryItemInput"]]] = field(default_factory=list)
    prompt: Optional[str] = field(default_factory=str)


@dc
class InventoryItemInput(CommonObject):
    item: Optional["ItemInput"] = field(default=None)
    value: Optional[float] = field(default=0)


@dc
class ItemInput(CommonObject):
    name: Optional[str] = field(default_factory=str)
    prompt: Optional[str] = field(default_factory=str)
    dimensions: Optional[List[Optional["DimensionInput"]]] = field(default_factory=list)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    rarity: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)


@dc
class NPCInput(CommonObject):
    attributes: Optional[List[Optional["AttributeEntry"]]] = field(default_factory=list)
    dimensions: Optional[List[Optional["DimensionInput"]]] = field(default_factory=list)
    features: Optional[List[Optional["FeatureInput"]]] = field(default_factory=list)
    histories: Optional[List[Optional["HistoryInput"]]] = field(default_factory=list)
    effects: Optional[List[Optional["EffectEntry"]]] = field(default_factory=list)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)
    inventory: Optional["InventoryInput"] = field(default=None)
    name: Optional[str] = field(default_factory=str)
    profession: Optional["ProfessionInput"] = field(default=None)
    prompt: Optional[str] = field(default_factory=str)
    race: Optional["RaceInput"] = field(default=None)
    sex: Optional[Sexes] = field(default=Sexes.OTHER)
    skills: Optional[List[Optional["SkillEntry"]]] = field(default_factory=list)
    stats: Optional[List[Optional["StatEntry"]]] = field(default_factory=list)
    user: Optional["UserInput"] = field(default=None)


@dc
class Options(CommonObject):
    limit: Optional[int] = field(default=None)
    sort_by: Optional[str] = field(default_factory=str)
    filters: Optional[List[Optional["Filter"]]] = field(default_factory=list)


@dc
class AttributeEntry(CommonObject):
    value: Optional[float] = field(default=0)
    attribute: Optional["AttributeInput"] = field(default=None)


@dc
class EffectEntry(CommonObject):
    effect: Optional["EffectInput"] = field(default=None)
    value: Optional[float] = field(default=0)
    magnitude: Optional[str] = field(default=None)


@dc
class PlayerInput(CommonObject):
    attributes: Optional[List[Optional["AttributeEntry"]]] = field(default_factory=list)
    dimensions: Optional[List[Optional["DimensionInput"]]] = field(default_factory=list)
    features: Optional[List[Optional["FeatureInput"]]] = field(default_factory=list)
    histories: Optional[List[Optional["HistoryInput"]]] = field(default_factory=list)
    effects: Optional[List[Optional["EffectEntry"]]] = field(default_factory=list)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)
    inventory: Optional["InventoryInput"] = field(default=None)
    name: Optional[str] = field(default_factory=str)
    profession: Optional["ProfessionInput"] = field(default=None)
    prompt: Optional[str] = field(default_factory=str)
    race: Optional["RaceInput"] = field(default=None)
    sex: Optional[Sexes] = field(default=Sexes.OTHER)
    skills: Optional[List[Optional["SkillEntry"]]] = field(default_factory=list)
    stats: Optional[List[Optional["StatEntry"]]] = field(default_factory=list)
    user: Optional["UserInput"] = field(default=None)


@dc
class SkillEntry(CommonObject):
    skill: Optional["SkillInput"] = field(default=None)
    value: Optional[float] = field(default=0)
    magnitude: Optional[str] = field(default=None)


@dc
class StatEntry(CommonObject):
    stat: Optional["StatInput"] = field(default=None)
    value: Optional[float] = field(default=0)
    magnitude: Optional[str] = field(default=None)


@dc
class ProfessionInput(CommonObject):
    type: Optional[str] = field(default_factory=str)
    name: Optional[str] = field(default_factory=str)
    attributes: Optional[List[Optional["AttributeEntry"]]] = field(default_factory=list)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)
    prompt: Optional[str] = field(default_factory=str)
    skills: Optional[List[Optional["SkillEntry"]]] = field(default_factory=list)
    stats: Optional[List[Optional["StatEntry"]]] = field(default_factory=list)


@dc
class RaceInput(CommonObject):
    name: Optional[str] = field(default_factory=str)
    type: Optional[Species] = field(default_factory=str)
    prompt: Optional[str] = field(default_factory=str)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)


@dc
class SkillInput(CommonObject):
    type: Optional[str] = field(default_factory=str)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)
    name: Optional[str] = field(default_factory=str)
    prompt: Optional[str] = field(default_factory=str)
    distribution: Optional["DistributionInput"] = field(default=None)


@dc
class StatInput(CommonObject):
    id: Optional[str] = field(default_factory=str)
    type: Optional[str] = field(default_factory=str)
    name: Optional[str] = field(default_factory=str)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    prompt: Optional[str] = field(default_factory=str)
    distribution: Optional["DistributionInput"] = field(default=None)


@dc
class TerrainEffectInput(CommonObject):
    effect: Optional["EffectInput"] = field(default=None)
    value: Optional[float] = field(default=0)


@dc
class TerrainInput(CommonObject):
    name: Optional[str] = field(default_factory=str)
    type: Optional[str] = field(default_factory=str)
    effects: Optional[List[Optional["TerrainEffectInput"]]] = field(default_factory=list)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)
    prompt: Optional[str] = field(default_factory=str)


@dc
class TransactionInput(CommonObject):
    currency: Optional[str] = field(default_factory=str)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)
    inventory_id: Optional[str] = field(default_factory=str)
    item: Optional[str] = field(default_factory=str)
    prompt: Optional[str] = field(default_factory=str)


@dc
class UserInput(CommonObject):
    email: Optional[str] = field(default_factory=str)
    first_name: Optional[str] = field(default_factory=str)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)
    last_name: Optional[str] = field(default_factory=str)
    prompt: Optional[str] = field(default_factory=str)


@dc
class WorldInput(CommonObject):
    type: Optional[str] = field(default_factory=str)
    name: Optional[str] = field(default_factory=str)
    characteristics: Optional[List[Optional["CharacteristicInput"]]] = field(default_factory=list)
    summary: Optional[str] = field(default=None)
    id: Optional[str] = field(default_factory=str)
    magic_level: Optional[MagicLevels] = field(default=None)
    prompt: Optional[str] = field(default_factory=str)
    races: Optional[List[Optional["RaceInput"]]] = field(default_factory=list)
    tech_level: Optional[TechLevels] = field(default=None)
    terrains: Optional[List[Optional["TerrainInput"]]] = field(default_factory=list)
