from typing import Any, Dict, Optional

from .custom_fields import (
    CreatureFields,
    CurrencyFields,
    InventoryFields,
    ItemFields,
    PlayerFields,
    ProfessionFields,
    RaceFields,
    SkillFields,
    StatFields,
    TerrainFields,
    TransactionFields,
    UserFields,
    WorldFields,
)
from .custom_typing_fields import GraphQLField
from .input_types import (
    CreatureInput,
    CurrencyInput,
    InventoryInput,
    ItemInput,
    PlayerInput,
    ProfessionInput,
    RaceInput,
    SkillInput,
    StatInput,
    TerrainInput,
    TransactionInput,
    UserInput,
    WorldInput,
)


class Mutation:
    @classmethod
    def create_creature(
        cls, *, input: Optional[CreatureInput] = None
    ) -> CreatureFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CreatureInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CreatureFields(field_name="createCreature", arguments=cleared_arguments)

    @classmethod
    def create_currency(
        cls, *, input: Optional[CurrencyInput] = None
    ) -> CurrencyFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CurrencyInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CurrencyFields(field_name="createCurrency", arguments=cleared_arguments)

    @classmethod
    def create_inventory(
        cls, *, input: Optional[InventoryInput] = None
    ) -> InventoryFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "InventoryInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InventoryFields(
            field_name="createInventory", arguments=cleared_arguments
        )

    @classmethod
    def create_item(cls, *, input: Optional[ItemInput] = None) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ItemInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="createItem", arguments=cleared_arguments)

    @classmethod
    def create_player(cls, *, input: Optional[PlayerInput] = None) -> PlayerFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "PlayerInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return PlayerFields(field_name="createPlayer", arguments=cleared_arguments)

    @classmethod
    def create_profession(
        cls, *, input: Optional[ProfessionInput] = None
    ) -> ProfessionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ProfessionInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProfessionFields(
            field_name="createProfession", arguments=cleared_arguments
        )

    @classmethod
    def create_race(cls, *, input: Optional[RaceInput] = None) -> RaceFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "RaceInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RaceFields(field_name="createRace", arguments=cleared_arguments)

    @classmethod
    def create_skill(cls, *, input: Optional[SkillInput] = None) -> SkillFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "SkillInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return SkillFields(field_name="createSkill", arguments=cleared_arguments)

    @classmethod
    def create_stat(cls, *, input: Optional[StatInput] = None) -> StatFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "StatInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return StatFields(field_name="createStat", arguments=cleared_arguments)

    @classmethod
    def create_terrain(cls, *, input: Optional[TerrainInput] = None) -> TerrainFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TerrainInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TerrainFields(field_name="createTerrain", arguments=cleared_arguments)

    @classmethod
    def create_transaction(
        cls, *, input: Optional[TransactionInput] = None
    ) -> TransactionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TransactionInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TransactionFields(
            field_name="createTransaction", arguments=cleared_arguments
        )

    @classmethod
    def create_user(cls, *, input: Optional[UserInput] = None) -> UserFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "UserInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields(field_name="createUser", arguments=cleared_arguments)

    @classmethod
    def create_world(cls, *, input: Optional[WorldInput] = None) -> WorldFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "WorldInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorldFields(field_name="createWorld", arguments=cleared_arguments)

    @classmethod
    def delete_creature(cls, *, id: Optional[str] = None) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="deleteCreature", arguments=cleared_arguments)

    @classmethod
    def delete_currency(cls, *, id: Optional[str] = None) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="deleteCurrency", arguments=cleared_arguments)

    @classmethod
    def delete_inventory(cls, *, id: Optional[str] = None) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="deleteInventory", arguments=cleared_arguments)

    @classmethod
    def delete_item(cls, *, id: Optional[str] = None) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="deleteItem", arguments=cleared_arguments)

    @classmethod
    def delete_player(cls, *, id: Optional[str] = None) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="deletePlayer", arguments=cleared_arguments)

    @classmethod
    def delete_profession(cls, *, id: Optional[str] = None) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="deleteProfession", arguments=cleared_arguments)

    @classmethod
    def delete_race(cls, *, id: Optional[str] = None) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="deleteRace", arguments=cleared_arguments)

    @classmethod
    def delete_skill(cls, *, id: Optional[str] = None) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="deleteSkill", arguments=cleared_arguments)

    @classmethod
    def delete_stat(cls, *, id: Optional[str] = None) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="deleteStat", arguments=cleared_arguments)

    @classmethod
    def delete_terrain(cls, *, id: Optional[str] = None) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="deleteTerrain", arguments=cleared_arguments)

    @classmethod
    def delete_transaction(cls, *, id: Optional[str] = None) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="deleteTransaction", arguments=cleared_arguments)

    @classmethod
    def delete_user(cls, *, id: Optional[str] = None) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="deleteUser", arguments=cleared_arguments)

    @classmethod
    def delete_world(cls, *, id: Optional[str] = None) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="deleteWorld", arguments=cleared_arguments)

    @classmethod
    def flavor_creature(cls, *, id: Optional[str] = None) -> CreatureFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CreatureFields(field_name="flavorCreature", arguments=cleared_arguments)

    @classmethod
    def flavor_currency(cls, *, id: Optional[str] = None) -> CurrencyFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CurrencyFields(field_name="flavorCurrency", arguments=cleared_arguments)

    @classmethod
    def flavor_inventory(cls, *, id: Optional[str] = None) -> InventoryFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InventoryFields(
            field_name="flavorInventory", arguments=cleared_arguments
        )

    @classmethod
    def flavor_item(cls, *, id: Optional[str] = None) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="flavorItem", arguments=cleared_arguments)

    @classmethod
    def flavor_player(cls, *, id: Optional[str] = None) -> PlayerFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return PlayerFields(field_name="flavorPlayer", arguments=cleared_arguments)

    @classmethod
    def flavor_profession(cls, *, id: Optional[str] = None) -> ProfessionFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProfessionFields(
            field_name="flavorProfession", arguments=cleared_arguments
        )

    @classmethod
    def flavor_race(cls, *, id: Optional[str] = None) -> RaceFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RaceFields(field_name="flavorRace", arguments=cleared_arguments)

    @classmethod
    def flavor_skill(cls, *, id: Optional[str] = None) -> SkillFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return SkillFields(field_name="flavorSkill", arguments=cleared_arguments)

    @classmethod
    def flavor_stat(cls, *, id: Optional[str] = None) -> StatFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return StatFields(field_name="flavorStat", arguments=cleared_arguments)

    @classmethod
    def flavor_terrain(cls, *, id: Optional[str] = None) -> TerrainFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TerrainFields(field_name="flavorTerrain", arguments=cleared_arguments)

    @classmethod
    def flavor_transaction(cls, *, id: Optional[str] = None) -> TransactionFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TransactionFields(
            field_name="flavorTransaction", arguments=cleared_arguments
        )

    @classmethod
    def flavor_user(cls, *, id: Optional[str] = None) -> UserFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields(field_name="flavorUser", arguments=cleared_arguments)

    @classmethod
    def flavor_world(cls, *, id: Optional[str] = None) -> WorldFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorldFields(field_name="flavorWorld", arguments=cleared_arguments)

    @classmethod
    def update_creature(
        cls, *, input: Optional[CreatureInput] = None
    ) -> CreatureFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CreatureInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CreatureFields(field_name="updateCreature", arguments=cleared_arguments)

    @classmethod
    def update_currency(
        cls, *, input: Optional[CurrencyInput] = None
    ) -> CurrencyFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CurrencyInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CurrencyFields(field_name="updateCurrency", arguments=cleared_arguments)

    @classmethod
    def update_inventory(
        cls, *, input: Optional[InventoryInput] = None
    ) -> InventoryFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "InventoryInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InventoryFields(
            field_name="updateInventory", arguments=cleared_arguments
        )

    @classmethod
    def update_item(cls, *, input: Optional[ItemInput] = None) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ItemInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="updateItem", arguments=cleared_arguments)

    @classmethod
    def update_player(cls, *, input: PlayerInput) -> PlayerFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "PlayerInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return PlayerFields(field_name="updatePlayer", arguments=cleared_arguments)

    @classmethod
    def update_profession(
        cls, *, input: Optional[ProfessionInput] = None
    ) -> ProfessionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ProfessionInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProfessionFields(
            field_name="updateProfession", arguments=cleared_arguments
        )

    @classmethod
    def update_race(cls, *, input: Optional[RaceInput] = None) -> RaceFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "RaceInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RaceFields(field_name="updateRace", arguments=cleared_arguments)

    @classmethod
    def update_skill(cls, *, input: Optional[SkillInput] = None) -> SkillFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "SkillInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return SkillFields(field_name="updateSkill", arguments=cleared_arguments)

    @classmethod
    def update_stat(cls, *, input: Optional[StatInput] = None) -> StatFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "StatInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return StatFields(field_name="updateStat", arguments=cleared_arguments)

    @classmethod
    def update_terrain(cls, *, input: Optional[TerrainInput] = None) -> TerrainFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TerrainInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TerrainFields(field_name="updateTerrain", arguments=cleared_arguments)

    @classmethod
    def update_transaction(
        cls, *, input: Optional[TransactionInput] = None
    ) -> TransactionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TransactionInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TransactionFields(
            field_name="updateTransaction", arguments=cleared_arguments
        )

    @classmethod
    def update_user(cls, *, input: Optional[UserInput] = None) -> UserFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "UserInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields(field_name="updateUser", arguments=cleared_arguments)

    @classmethod
    def update_world(cls, *, input: Optional[WorldInput] = None) -> WorldFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "WorldInput", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorldFields(field_name="updateWorld", arguments=cleared_arguments)
