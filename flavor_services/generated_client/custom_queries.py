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
from .input_types import Options


class Query:
    @classmethod
    def find_creature(cls, *, options: Optional[Options] = None) -> CreatureFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "options": {"type": "Options", "value": options}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CreatureFields(field_name="findCreature", arguments=cleared_arguments)

    @classmethod
    def find_currency(cls, *, options: Optional[Options] = None) -> CurrencyFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "options": {"type": "Options", "value": options}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CurrencyFields(field_name="findCurrency", arguments=cleared_arguments)

    @classmethod
    def find_inventory(cls, *, options: Optional[Options] = None) -> InventoryFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "options": {"type": "Options", "value": options}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InventoryFields(field_name="findInventory", arguments=cleared_arguments)

    @classmethod
    def find_item(cls, *, options: Optional[Options] = None) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "options": {"type": "Options", "value": options}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="findItem", arguments=cleared_arguments)

    @classmethod
    def find_player(cls, *, options: Optional[Options] = None) -> PlayerFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "options": {"type": "Options", "value": options}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return PlayerFields(field_name="findPlayer", arguments=cleared_arguments)

    @classmethod
    def find_profession(cls, *, options: Optional[Options] = None) -> ProfessionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "options": {"type": "Options", "value": options}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProfessionFields(
            field_name="findProfession", arguments=cleared_arguments
        )

    @classmethod
    def find_race(cls, *, options: Optional[Options] = None) -> RaceFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "options": {"type": "Options", "value": options}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RaceFields(field_name="findRace", arguments=cleared_arguments)

    @classmethod
    def find_skill(cls, *, options: Optional[Options] = None) -> SkillFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "options": {"type": "Options", "value": options}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return SkillFields(field_name="findSkill", arguments=cleared_arguments)

    @classmethod
    def find_stat(cls, *, options: Optional[Options] = None) -> StatFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "options": {"type": "Options", "value": options}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return StatFields(field_name="findStat", arguments=cleared_arguments)

    @classmethod
    def find_terrain(cls, *, options: Optional[Options] = None) -> TerrainFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "options": {"type": "Options", "value": options}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TerrainFields(field_name="findTerrain", arguments=cleared_arguments)

    @classmethod
    def find_transaction(
        cls, *, options: Optional[Options] = None
    ) -> TransactionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "options": {"type": "Options", "value": options}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TransactionFields(
            field_name="findTransaction", arguments=cleared_arguments
        )

    @classmethod
    def find_user(cls, *, options: Optional[Options] = None) -> UserFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "options": {"type": "Options", "value": options}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields(field_name="findUser", arguments=cleared_arguments)

    @classmethod
    def find_world(cls, *, options: Optional[Options] = None) -> WorldFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "options": {"type": "Options", "value": options}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorldFields(field_name="findWorld", arguments=cleared_arguments)

    @classmethod
    def get_creature(cls, *, id: Optional[str] = None) -> CreatureFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CreatureFields(field_name="getCreature", arguments=cleared_arguments)

    @classmethod
    def get_currency(cls, *, id: Optional[str] = None) -> CurrencyFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CurrencyFields(field_name="getCurrency", arguments=cleared_arguments)

    @classmethod
    def get_inventory(cls, *, id: Optional[str] = None) -> InventoryFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InventoryFields(field_name="getInventory", arguments=cleared_arguments)

    @classmethod
    def get_item(cls, *, id: Optional[str] = None) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="getItem", arguments=cleared_arguments)

    @classmethod
    def get_player(cls, *, id: Optional[str] = None) -> PlayerFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return PlayerFields(field_name="getPlayer", arguments=cleared_arguments)

    @classmethod
    def get_profession(cls, *, id: Optional[str] = None) -> ProfessionFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProfessionFields(field_name="getProfession", arguments=cleared_arguments)

    @classmethod
    def get_race(cls, *, id: Optional[str] = None) -> RaceFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RaceFields(field_name="getRace", arguments=cleared_arguments)

    @classmethod
    def get_skill(cls, *, id: Optional[str] = None) -> SkillFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return SkillFields(field_name="getSkill", arguments=cleared_arguments)

    @classmethod
    def get_stat(cls, *, id: Optional[str] = None) -> StatFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return StatFields(field_name="getStat", arguments=cleared_arguments)

    @classmethod
    def get_terrain(cls, *, id: Optional[str] = None) -> TerrainFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TerrainFields(field_name="getTerrain", arguments=cleared_arguments)

    @classmethod
    def get_transaction(cls, *, id: Optional[str] = None) -> TransactionFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TransactionFields(
            field_name="getTransaction", arguments=cleared_arguments
        )

    @classmethod
    def get_user(cls, *, id: Optional[str] = None) -> UserFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields(field_name="getUser", arguments=cleared_arguments)

    @classmethod
    def get_world(cls, *, id: Optional[str] = None) -> WorldFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorldFields(field_name="getWorld", arguments=cleared_arguments)
