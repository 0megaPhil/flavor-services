from typing import Union

from .base_operation import GraphQLField
from .custom_typing_fields import (
    AttributeGraphQLField,
    CharacteristicGraphQLField,
    CommonEntityGraphQLField,
    CommonObjectGraphQLField,
    CommonValueGraphQLField,
    CreatureGraphQLField,
    CurrencyGraphQLField,
    DimensionGraphQLField,
    EffectGraphQLField,
    ErrorGraphQLField,
    FlavorGraphQLField,
    InventoryCurrencyGraphQLField,
    InventoryGraphQLField,
    InventoryItemGraphQLField,
    ItemGraphQLField,
    PlayerAttributeGraphQLField,
    PlayerEffectGraphQLField,
    PlayerGraphQLField,
    PlayerSkillGraphQLField,
    PlayerStatGraphQLField,
    ProfessionGraphQLField,
    RaceGraphQLField,
    SkillGraphQLField,
    StatGraphQLField,
    TerrainEffectGraphQLField,
    TerrainGraphQLField,
    TransactionGraphQLField,
    UserGraphQLField,
    WorldGraphQLField,
)


class AttributeFields(GraphQLField):
    created: "AttributeGraphQLField" = AttributeGraphQLField("created")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "AttributeGraphQLField" = AttributeGraphQLField("id")
    name: "AttributeGraphQLField" = AttributeGraphQLField("name")
    prompt: "AttributeGraphQLField" = AttributeGraphQLField("prompt")
    type: "AttributeGraphQLField" = AttributeGraphQLField("type")
    updated: "AttributeGraphQLField" = AttributeGraphQLField("updated")
    version: "AttributeGraphQLField" = AttributeGraphQLField("version")

    def fields(
            self, *subfields: Union[AttributeGraphQLField, "ErrorFields", "FlavorFields"]
    ) -> "AttributeFields":
        """Subfields should come from the AttributeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AttributeFields":
        self._alias = alias
        return self


class CharacteristicFields(GraphQLField):
    description: "CharacteristicGraphQLField" = CharacteristicGraphQLField(
        "description"
    )
    title: "CharacteristicGraphQLField" = CharacteristicGraphQLField("title")
    value: "CharacteristicGraphQLField" = CharacteristicGraphQLField("value")

    def fields(self, *subfields: CharacteristicGraphQLField) -> "CharacteristicFields":
        """Subfields should come from the CharacteristicFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CharacteristicFields":
        self._alias = alias
        return self


class CommonEntityInterface(GraphQLField):
    created: "CommonEntityGraphQLField" = CommonEntityGraphQLField("created")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "CommonEntityGraphQLField" = CommonEntityGraphQLField("id")
    prompt: "CommonEntityGraphQLField" = CommonEntityGraphQLField("prompt")
    updated: "CommonEntityGraphQLField" = CommonEntityGraphQLField("updated")
    version: "CommonEntityGraphQLField" = CommonEntityGraphQLField("version")

    def fields(
            self, *subfields: Union[CommonEntityGraphQLField, "ErrorFields", "FlavorFields"]
    ) -> "CommonEntityInterface":
        """Subfields should come from the CommonEntityInterface class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CommonEntityInterface":
        self._alias = alias
        return self

    def on(self, type_name: str, *subfields: GraphQLField) -> "CommonEntityInterface":
        self._inline_fragments[type_name] = subfields
        return self


class CommonObjectInterface(GraphQLField):
    object_type: "CommonObjectGraphQLField" = CommonObjectGraphQLField("objectType")

    def fields(self, *subfields: CommonObjectGraphQLField) -> "CommonObjectInterface":
        """Subfields should come from the CommonObjectInterface class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CommonObjectInterface":
        self._alias = alias
        return self

    def on(self, type_name: str, *subfields: GraphQLField) -> "CommonObjectInterface":
        self._inline_fragments[type_name] = subfields
        return self


class CommonValueInterface(GraphQLField):
    value: "CommonValueGraphQLField" = CommonValueGraphQLField("value")

    def fields(self, *subfields: CommonValueGraphQLField) -> "CommonValueInterface":
        """Subfields should come from the CommonValueInterface class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CommonValueInterface":
        self._alias = alias
        return self

    def on(self, type_name: str, *subfields: GraphQLField) -> "CommonValueInterface":
        self._inline_fragments[type_name] = subfields
        return self


class CreatureFields(GraphQLField):
    @classmethod
    def attributes(cls) -> "PlayerAttributeFields":
        return PlayerAttributeFields("attributes")

    created: "CreatureGraphQLField" = CreatureGraphQLField("created")

    @classmethod
    def dimensions(cls) -> "DimensionFields":
        return DimensionFields("dimensions")

    @classmethod
    def effects(cls) -> "PlayerEffectFields":
        return PlayerEffectFields("effects")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "CreatureGraphQLField" = CreatureGraphQLField("id")

    @classmethod
    def inventory(cls) -> "InventoryFields":
        return InventoryFields("inventory")

    name: "CreatureGraphQLField" = CreatureGraphQLField("name")

    @classmethod
    def profession(cls) -> "ProfessionFields":
        return ProfessionFields("profession")

    prompt: "CreatureGraphQLField" = CreatureGraphQLField("prompt")
    sex: "CreatureGraphQLField" = CreatureGraphQLField("sex")

    @classmethod
    def skills(cls) -> "PlayerSkillFields":
        return PlayerSkillFields("skills")

    @classmethod
    def stats(cls) -> "PlayerStatFields":
        return PlayerStatFields("stats")

    type: "CreatureGraphQLField" = CreatureGraphQLField("type")
    updated: "CreatureGraphQLField" = CreatureGraphQLField("updated")
    version: "CreatureGraphQLField" = CreatureGraphQLField("version")

    def fields(
            self,
            *subfields: Union[
                CreatureGraphQLField,
                "DimensionFields",
                "ErrorFields",
                "FlavorFields",
                "InventoryFields",
                "PlayerAttributeFields",
                "PlayerEffectFields",
                "PlayerSkillFields",
                "PlayerStatFields",
                "ProfessionFields",
            ]
    ) -> "CreatureFields":
        """Subfields should come from the CreatureFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CreatureFields":
        self._alias = alias
        return self


class CurrencyFields(GraphQLField):
    created: "CurrencyGraphQLField" = CurrencyGraphQLField("created")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "CurrencyGraphQLField" = CurrencyGraphQLField("id")
    name: "CurrencyGraphQLField" = CurrencyGraphQLField("name")
    prompt: "CurrencyGraphQLField" = CurrencyGraphQLField("prompt")
    updated: "CurrencyGraphQLField" = CurrencyGraphQLField("updated")
    version: "CurrencyGraphQLField" = CurrencyGraphQLField("version")

    def fields(
            self, *subfields: Union[CurrencyGraphQLField, "ErrorFields", "FlavorFields"]
    ) -> "CurrencyFields":
        """Subfields should come from the CurrencyFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CurrencyFields":
        self._alias = alias
        return self


class DimensionFields(GraphQLField):
    title: "DimensionGraphQLField" = DimensionGraphQLField("title")
    unit_type: "DimensionGraphQLField" = DimensionGraphQLField("unitType")
    value: "DimensionGraphQLField" = DimensionGraphQLField("value")

    def fields(self, *subfields: DimensionGraphQLField) -> "DimensionFields":
        """Subfields should come from the DimensionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DimensionFields":
        self._alias = alias
        return self


class EffectFields(GraphQLField):
    created: "EffectGraphQLField" = EffectGraphQLField("created")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "EffectGraphQLField" = EffectGraphQLField("id")
    name: "EffectGraphQLField" = EffectGraphQLField("name")
    prompt: "EffectGraphQLField" = EffectGraphQLField("prompt")
    type: "EffectGraphQLField" = EffectGraphQLField("type")
    updated: "EffectGraphQLField" = EffectGraphQLField("updated")
    version: "EffectGraphQLField" = EffectGraphQLField("version")

    def fields(
            self, *subfields: Union[EffectGraphQLField, "ErrorFields", "FlavorFields"]
    ) -> "EffectFields":
        """Subfields should come from the EffectFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EffectFields":
        self._alias = alias
        return self


class ErrorFields(GraphQLField):
    data: "ErrorGraphQLField" = ErrorGraphQLField("data")
    error_code: "ErrorGraphQLField" = ErrorGraphQLField("errorCode")
    headers: "ErrorGraphQLField" = ErrorGraphQLField("headers")
    message: "ErrorGraphQLField" = ErrorGraphQLField("message")
    object_type: "ErrorGraphQLField" = ErrorGraphQLField("objectType")
    params: "ErrorGraphQLField" = ErrorGraphQLField("params")
    path: "ErrorGraphQLField" = ErrorGraphQLField("path")
    title: "ErrorGraphQLField" = ErrorGraphQLField("title")
    type: "ErrorGraphQLField" = ErrorGraphQLField("type")

    def fields(self, *subfields: ErrorGraphQLField) -> "ErrorFields":
        """Subfields should come from the ErrorFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ErrorFields":
        self._alias = alias
        return self


class FlavorFields(GraphQLField):
    @classmethod
    def characteristics(cls) -> "CharacteristicFields":
        return CharacteristicFields("characteristics")

    object_type: "FlavorGraphQLField" = FlavorGraphQLField("objectType")
    summary: "FlavorGraphQLField" = FlavorGraphQLField("summary")
    target: "FlavorGraphQLField" = FlavorGraphQLField("targetId")

    def fields(
            self, *subfields: Union[FlavorGraphQLField, "CharacteristicFields"]
    ) -> "FlavorFields":
        """Subfields should come from the FlavorFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "FlavorFields":
        self._alias = alias
        return self


class InventoryFields(GraphQLField):
    created: "InventoryGraphQLField" = InventoryGraphQLField("created")

    @classmethod
    def currencies(cls) -> "InventoryCurrencyFields":
        return InventoryCurrencyFields("currencies")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "InventoryGraphQLField" = InventoryGraphQLField("id")

    @classmethod
    def items(cls) -> "InventoryItemFields":
        return InventoryItemFields("items")

    prompt: "InventoryGraphQLField" = InventoryGraphQLField("prompt")
    updated: "InventoryGraphQLField" = InventoryGraphQLField("updated")
    version: "InventoryGraphQLField" = InventoryGraphQLField("version")

    def fields(
            self,
            *subfields: Union[
                InventoryGraphQLField,
                "ErrorFields",
                "FlavorFields",
                "InventoryCurrencyFields",
                "InventoryItemFields",
            ]
    ) -> "InventoryFields":
        """Subfields should come from the InventoryFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "InventoryFields":
        self._alias = alias
        return self


class InventoryCurrencyFields(GraphQLField):
    @classmethod
    def currency(cls) -> "CurrencyFields":
        return CurrencyFields("currency")

    value: "InventoryCurrencyGraphQLField" = InventoryCurrencyGraphQLField("value")

    def fields(
            self, *subfields: Union[InventoryCurrencyGraphQLField, "CurrencyFields"]
    ) -> "InventoryCurrencyFields":
        """Subfields should come from the InventoryCurrencyFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "InventoryCurrencyFields":
        self._alias = alias
        return self


class InventoryItemFields(GraphQLField):
    @classmethod
    def item(cls) -> "ItemFields":
        return ItemFields("item")

    value: "InventoryItemGraphQLField" = InventoryItemGraphQLField("value")

    def fields(
            self, *subfields: Union[InventoryItemGraphQLField, "ItemFields"]
    ) -> "InventoryItemFields":
        """Subfields should come from the InventoryItemFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "InventoryItemFields":
        self._alias = alias
        return self


class ItemFields(GraphQLField):
    created: "ItemGraphQLField" = ItemGraphQLField("created")

    @classmethod
    def dimensions(cls) -> "DimensionFields":
        return DimensionFields("dimensions")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "ItemGraphQLField" = ItemGraphQLField("id")
    name: "ItemGraphQLField" = ItemGraphQLField("name")
    prompt: "ItemGraphQLField" = ItemGraphQLField("prompt")
    updated: "ItemGraphQLField" = ItemGraphQLField("updated")
    version: "ItemGraphQLField" = ItemGraphQLField("version")

    def fields(
            self,
            *subfields: Union[
                ItemGraphQLField, "DimensionFields", "ErrorFields", "FlavorFields"
            ]
    ) -> "ItemFields":
        """Subfields should come from the ItemFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ItemFields":
        self._alias = alias
        return self


class PlayerFields(GraphQLField):
    @classmethod
    def attributes(cls) -> "PlayerAttributeFields":
        return PlayerAttributeFields("attributes")

    created: "PlayerGraphQLField" = PlayerGraphQLField("created")

    @classmethod
    def dimensions(cls) -> "DimensionFields":
        return DimensionFields("dimensions")

    @classmethod
    def effects(cls) -> "PlayerEffectFields":
        return PlayerEffectFields("effects")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "PlayerGraphQLField" = PlayerGraphQLField("id")

    @classmethod
    def inventory(cls) -> "InventoryFields":
        return InventoryFields("inventory")

    name: "PlayerGraphQLField" = PlayerGraphQLField("name")

    @classmethod
    def profession(cls) -> "ProfessionFields":
        return ProfessionFields("profession")

    prompt: "PlayerGraphQLField" = PlayerGraphQLField("prompt")

    @classmethod
    def race(cls) -> "RaceFields":
        return RaceFields("race")

    sex: "PlayerGraphQLField" = PlayerGraphQLField("sex")

    @classmethod
    def skills(cls) -> "PlayerSkillFields":
        return PlayerSkillFields("skills")

    @classmethod
    def stats(cls) -> "PlayerStatFields":
        return PlayerStatFields("stats")

    updated: "PlayerGraphQLField" = PlayerGraphQLField("updated")

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    version: "PlayerGraphQLField" = PlayerGraphQLField("version")

    def fields(
            self,
            *subfields: Union[
                PlayerGraphQLField,
                "DimensionFields",
                "ErrorFields",
                "FlavorFields",
                "InventoryFields",
                "PlayerAttributeFields",
                "PlayerEffectFields",
                "PlayerSkillFields",
                "PlayerStatFields",
                "ProfessionFields",
                "RaceFields",
                "UserFields",
            ]
    ) -> "PlayerFields":
        """Subfields should come from the PlayerFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "PlayerFields":
        self._alias = alias
        return self


class PlayerAttributeFields(GraphQLField):
    @classmethod
    def attribute(cls) -> "AttributeFields":
        return AttributeFields("attribute")

    value: "PlayerAttributeGraphQLField" = PlayerAttributeGraphQLField("value")

    def fields(
            self, *subfields: Union[PlayerAttributeGraphQLField, "AttributeFields"]
    ) -> "PlayerAttributeFields":
        """Subfields should come from the PlayerAttributeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "PlayerAttributeFields":
        self._alias = alias
        return self


class PlayerEffectFields(GraphQLField):
    @classmethod
    def effect(cls) -> "EffectFields":
        return EffectFields("effect")

    value: "PlayerEffectGraphQLField" = PlayerEffectGraphQLField("value")

    def fields(
            self, *subfields: Union[PlayerEffectGraphQLField, "EffectFields"]
    ) -> "PlayerEffectFields":
        """Subfields should come from the PlayerEffectFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "PlayerEffectFields":
        self._alias = alias
        return self


class PlayerSkillFields(GraphQLField):
    @classmethod
    def skill(cls) -> "SkillFields":
        return SkillFields("skill")

    value: "PlayerSkillGraphQLField" = PlayerSkillGraphQLField("value")

    def fields(
            self, *subfields: Union[PlayerSkillGraphQLField, "SkillFields"]
    ) -> "PlayerSkillFields":
        """Subfields should come from the PlayerSkillFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "PlayerSkillFields":
        self._alias = alias
        return self


class PlayerStatFields(GraphQLField):
    @classmethod
    def stat(cls) -> "StatFields":
        return StatFields("stat")

    value: "PlayerStatGraphQLField" = PlayerStatGraphQLField("value")

    def fields(
            self, *subfields: Union[PlayerStatGraphQLField, "StatFields"]
    ) -> "PlayerStatFields":
        """Subfields should come from the PlayerStatFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "PlayerStatFields":
        self._alias = alias
        return self


class ProfessionFields(GraphQLField):
    @classmethod
    def attributes(cls) -> "PlayerAttributeFields":
        return PlayerAttributeFields("attributes")

    created: "ProfessionGraphQLField" = ProfessionGraphQLField("created")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "ProfessionGraphQLField" = ProfessionGraphQLField("id")
    name: "ProfessionGraphQLField" = ProfessionGraphQLField("name")
    prompt: "ProfessionGraphQLField" = ProfessionGraphQLField("prompt")

    @classmethod
    def skills(cls) -> "PlayerSkillFields":
        return PlayerSkillFields("skills")

    @classmethod
    def stats(cls) -> "PlayerStatFields":
        return PlayerStatFields("stats")

    type: "ProfessionGraphQLField" = ProfessionGraphQLField("type")
    updated: "ProfessionGraphQLField" = ProfessionGraphQLField("updated")
    version: "ProfessionGraphQLField" = ProfessionGraphQLField("version")

    def fields(
            self,
            *subfields: Union[
                ProfessionGraphQLField,
                "ErrorFields",
                "FlavorFields",
                "PlayerAttributeFields",
                "PlayerSkillFields",
                "PlayerStatFields",
            ]
    ) -> "ProfessionFields":
        """Subfields should come from the ProfessionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProfessionFields":
        self._alias = alias
        return self


class RaceFields(GraphQLField):
    created: "RaceGraphQLField" = RaceGraphQLField("created")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "RaceGraphQLField" = RaceGraphQLField("id")
    name: "RaceGraphQLField" = RaceGraphQLField("name")
    prompt: "RaceGraphQLField" = RaceGraphQLField("prompt")
    type: "RaceGraphQLField" = RaceGraphQLField("type")
    updated: "RaceGraphQLField" = RaceGraphQLField("updated")
    version: "RaceGraphQLField" = RaceGraphQLField("version")

    def fields(
            self, *subfields: Union[RaceGraphQLField, "ErrorFields", "FlavorFields"]
    ) -> "RaceFields":
        """Subfields should come from the RaceFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RaceFields":
        self._alias = alias
        return self


class SkillFields(GraphQLField):
    created: "SkillGraphQLField" = SkillGraphQLField("created")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "SkillGraphQLField" = SkillGraphQLField("id")
    name: "SkillGraphQLField" = SkillGraphQLField("name")
    prompt: "SkillGraphQLField" = SkillGraphQLField("prompt")
    type: "SkillGraphQLField" = SkillGraphQLField("type")
    updated: "SkillGraphQLField" = SkillGraphQLField("updated")
    version: "SkillGraphQLField" = SkillGraphQLField("version")

    def fields(
            self, *subfields: Union[SkillGraphQLField, "ErrorFields", "FlavorFields"]
    ) -> "SkillFields":
        """Subfields should come from the SkillFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "SkillFields":
        self._alias = alias
        return self


class StatFields(GraphQLField):
    created: "StatGraphQLField" = StatGraphQLField("created")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "StatGraphQLField" = StatGraphQLField("id")
    name: "StatGraphQLField" = StatGraphQLField("name")
    prompt: "StatGraphQLField" = StatGraphQLField("prompt")
    type: "StatGraphQLField" = StatGraphQLField("type")
    updated: "StatGraphQLField" = StatGraphQLField("updated")
    version: "StatGraphQLField" = StatGraphQLField("version")

    def fields(
            self, *subfields: Union[StatGraphQLField, "ErrorFields", "FlavorFields"]
    ) -> "StatFields":
        """Subfields should come from the StatFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "StatFields":
        self._alias = alias
        return self


class TerrainFields(GraphQLField):
    created: "TerrainGraphQLField" = TerrainGraphQLField("created")

    @classmethod
    def effects(cls) -> "TerrainEffectFields":
        return TerrainEffectFields("effects")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "TerrainGraphQLField" = TerrainGraphQLField("id")
    name: "TerrainGraphQLField" = TerrainGraphQLField("name")
    prompt: "TerrainGraphQLField" = TerrainGraphQLField("prompt")
    type: "TerrainGraphQLField" = TerrainGraphQLField("type")
    updated: "TerrainGraphQLField" = TerrainGraphQLField("updated")
    version: "TerrainGraphQLField" = TerrainGraphQLField("version")

    def fields(
            self,
            *subfields: Union[
                TerrainGraphQLField, "ErrorFields", "FlavorFields", "TerrainEffectFields"
            ]
    ) -> "TerrainFields":
        """Subfields should come from the TerrainFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TerrainFields":
        self._alias = alias
        return self


class TerrainEffectFields(GraphQLField):
    @classmethod
    def effect(cls) -> "EffectFields":
        return EffectFields("effect")

    value: "TerrainEffectGraphQLField" = TerrainEffectGraphQLField("value")

    def fields(
            self, *subfields: Union[TerrainEffectGraphQLField, "EffectFields"]
    ) -> "TerrainEffectFields":
        """Subfields should come from the TerrainEffectFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TerrainEffectFields":
        self._alias = alias
        return self


class TransactionFields(GraphQLField):
    created: "TransactionGraphQLField" = TransactionGraphQLField("created")
    currency: "TransactionGraphQLField" = TransactionGraphQLField("currency")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "TransactionGraphQLField" = TransactionGraphQLField("id")
    inventory_id: "TransactionGraphQLField" = TransactionGraphQLField("inventoryId")
    item: "TransactionGraphQLField" = TransactionGraphQLField("item")
    prompt: "TransactionGraphQLField" = TransactionGraphQLField("prompt")
    updated: "TransactionGraphQLField" = TransactionGraphQLField("updated")
    version: "TransactionGraphQLField" = TransactionGraphQLField("version")

    def fields(
            self, *subfields: Union[TransactionGraphQLField, "ErrorFields", "FlavorFields"]
    ) -> "TransactionFields":
        """Subfields should come from the TransactionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TransactionFields":
        self._alias = alias
        return self


class UserFields(GraphQLField):
    created: "UserGraphQLField" = UserGraphQLField("created")
    email: "UserGraphQLField" = UserGraphQLField("email")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    first_name: "UserGraphQLField" = UserGraphQLField("firstName")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "UserGraphQLField" = UserGraphQLField("id")
    last_name: "UserGraphQLField" = UserGraphQLField("lastName")
    prompt: "UserGraphQLField" = UserGraphQLField("prompt")
    updated: "UserGraphQLField" = UserGraphQLField("updated")
    version: "UserGraphQLField" = UserGraphQLField("version")

    def fields(
            self, *subfields: Union[UserGraphQLField, "ErrorFields", "FlavorFields"]
    ) -> "UserFields":
        """Subfields should come from the UserFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UserFields":
        self._alias = alias
        return self


class WorldFields(GraphQLField):
    created: "WorldGraphQLField" = WorldGraphQLField("created")

    @classmethod
    def error(cls) -> "ErrorFields":
        return ErrorFields("error")

    @classmethod
    def flavor(cls) -> "FlavorFields":
        return FlavorFields("flavor")

    id: "WorldGraphQLField" = WorldGraphQLField("id")
    magic_level: "WorldGraphQLField" = WorldGraphQLField("magicLevel")
    name: "WorldGraphQLField" = WorldGraphQLField("name")
    prompt: "WorldGraphQLField" = WorldGraphQLField("prompt")

    @classmethod
    def races(cls) -> "RaceFields":
        return RaceFields("races")

    tech_level: "WorldGraphQLField" = WorldGraphQLField("techLevel")

    @classmethod
    def terrains(cls) -> "TerrainFields":
        return TerrainFields("terrains")

    type: "WorldGraphQLField" = WorldGraphQLField("type")
    updated: "WorldGraphQLField" = WorldGraphQLField("updated")
    version: "WorldGraphQLField" = WorldGraphQLField("version")

    def fields(
            self,
            *subfields: Union[
                WorldGraphQLField,
                "ErrorFields",
                "FlavorFields",
                "RaceFields",
                "TerrainFields",
            ]
    ) -> "WorldFields":
        """Subfields should come from the WorldFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WorldFields":
        self._alias = alias
        return self
