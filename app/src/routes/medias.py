from fastapi import APIRouter, Depends
from config.db import conn
from src.models.medias import medias
from src.schemas.medias import Media
from typing import List, Union
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select, and_
import json

router = APIRouter(
    prefix="/medias",
    tags=["medias"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "",
    response_model=List[Media],
    description="Get a list of all posters",
)
def get_medias():
    return conn.execute(medias.select()).fetchall()

@router.get(
    "/{id}",
    response_model=Media,
    description="Get a single Media by Id",
)
def get_media(id: str):
    return conn.execute(medias.select().where(medias.c.id == id)).first()



    Column("title", Text),
    Column("kind", Text),
    Column("category", Text),
    Column("content", Text),
    Column("release_date", Text),
    Column("id_poster", Text)

@router.post(
    "",
    response_model=Media, 
    description="Create a new Media")
def create_media(media: Media):
    new_media = {
        "title": media.title, 
        "kind": media.kind,
        "category": media.category,
        "content": media.content,
        "release_date": media.release_date,
        "id_poster": media.id_poster
        }
    result = conn.execute(medias.insert().values(new_media))
    return conn.execute(medias.select().where(medias.c.id == result.lastrowid)).first()

@router.put(
    "/{id}",
    response_model=Media, 
    description="Update a Media by Id"
)
def update_media(poster: Media, id: int):
    conn.execute(
        medias.update()
        .values(
                title=medias.title, 
                kind=medias.kind,
                category=medias.category,
                content=medias.content,
                release_date=medias.release_date,
                id_poster=medias.id_poster
                )
        .where(medias.c.id == id)
    )
    return conn.execute(medias.select().where(medias.c.id == id)).first()

@router.delete(
    "/{id}",
    status_code=HTTP_204_NO_CONTENT
)
def delete_media(id: int):
    conn.execute(medias.delete().where(medias.c.id == id))
    return conn.execute(medias.select().where(medias.c.id == id)).first()
