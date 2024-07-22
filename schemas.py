from datetime import datetime
from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: str


class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    id: int