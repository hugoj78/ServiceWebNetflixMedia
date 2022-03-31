from typing import Optional
from pydantic import BaseModel

class Media(BaseModel):
    id: Optional[int]
    title: str
    kind: str
    category: str
    content: str
    release_date: str
    id_poster: int