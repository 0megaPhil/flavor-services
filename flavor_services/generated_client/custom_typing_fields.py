from .base_operation import GraphQLField


class CommonEntityGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "CommonEntityGraphQLField":
        self._alias = alias
        return self


class CommonObjectGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "CommonObjectGraphQLField":
        self._alias = alias
        return self


class CommonValueGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "CommonValueGraphQLField":
        self._alias = alias
        return self


class AttributeGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "AttributeGraphQLField":
        self._alias = alias
        return self


class CharacteristicGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "CharacteristicGraphQLField":
        self._alias = alias
        return self


class CreatureGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "CreatureGraphQLField":
        self._alias = alias
        return self


class CurrencyGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "CurrencyGraphQLField":
        self._alias = alias
        return self


class DimensionGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "DimensionGraphQLField":
        self._alias = alias
        return self


class EffectGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "EffectGraphQLField":
        self._alias = alias
        return self


class ErrorGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "ErrorGraphQLField":
        self._alias = alias
        return self


class ErrorResponseGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "ErrorResponseGraphQLField":
        self._alias = alias
        return self


class FlavorGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "FlavorGraphQLField":
        self._alias = alias
        return self


class InventoryGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "InventoryGraphQLField":
        self._alias = alias
        return self


class InventoryCurrencyGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "InventoryCurrencyGraphQLField":
        self._alias = alias
        return self


class InventoryItemGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "InventoryItemGraphQLField":
        self._alias = alias
        return self


class ItemGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "ItemGraphQLField":
        self._alias = alias
        return self


class NPCGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "NPCGraphQLField":
        self._alias = alias
        return self


class PlayerGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "PlayerGraphQLField":
        self._alias = alias
        return self


class PlayerAttributeGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "PlayerAttributeGraphQLField":
        self._alias = alias
        return self


class PlayerEffectGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "PlayerEffectGraphQLField":
        self._alias = alias
        return self


class PlayerSkillGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "PlayerSkillGraphQLField":
        self._alias = alias
        return self


class PlayerStatGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "PlayerStatGraphQLField":
        self._alias = alias
        return self


class ProfessionGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "ProfessionGraphQLField":
        self._alias = alias
        return self


class RaceGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "RaceGraphQLField":
        self._alias = alias
        return self


class SkillGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "SkillGraphQLField":
        self._alias = alias
        return self


class StatGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "StatGraphQLField":
        self._alias = alias
        return self


class TerrainGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "TerrainGraphQLField":
        self._alias = alias
        return self


class TerrainEffectGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "TerrainEffectGraphQLField":
        self._alias = alias
        return self


class TransactionGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "TransactionGraphQLField":
        self._alias = alias
        return self


class UserGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "UserGraphQLField":
        self._alias = alias
        return self


class WorldGraphQLField(GraphQLField):
    def alias(self, alias: str) -> "WorldGraphQLField":
        self._alias = alias
        return self
