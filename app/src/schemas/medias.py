from typing import Optional
from pydantic import BaseModel
from src.models.StatusEnum import StatusEnum

class Media(BaseModel):
    id: Optional[int]
    title: str
    kind: str
    category: str
    content: str
    release_date: str
    country: str
    description: str
    status: StatusEnum
    id_poster: int

class MediaUpdateDescription(BaseModel):
    id: Optional[int]
    title: Optional[str]
    kind: Optional[str]
    category: Optional[str]
    content: Optional[str]
    release_date: Optional[str]
    country: Optional[str]
    description: str
    status: Optional[StatusEnum]
    id_poster: Optional[int]
