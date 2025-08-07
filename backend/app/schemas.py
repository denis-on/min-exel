from pydantic import BaseModel
from typing import Optional, Dict

class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class SheetCreate(BaseModel):
    name: str

class RowUpdate(BaseModel):
    data: Dict[str, str]
    version: int
