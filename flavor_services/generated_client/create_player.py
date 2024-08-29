from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class CreatePlayer(BaseModel):
    create_player: Optional["CreatePlayerCreatePlayer"] = Field(alias="createPlayer")


class CreatePlayerCreatePlayer(BaseModel):
    id: Optional[str]
    name: Optional[str]
    stats: Optional[List[Optional["CreatePlayerCreatePlayerStats"]]]


class CreatePlayerCreatePlayerStats(BaseModel):
    stat: "CreatePlayerCreatePlayerStatsStat"
    value: float


class CreatePlayerCreatePlayerStatsStat(BaseModel):
    id: Optional[str]
    name: Optional[str]


CreatePlayer.model_rebuild()
CreatePlayerCreatePlayer.model_rebuild()
CreatePlayerCreatePlayerStats.model_rebuild()
