from fastapi import APIRouter, Depends
from config.db import conn
from src.models.medias import medias
from src.schemas.medias import Media
from typing import List, Union
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select, and_
import json
from src.models.StatusEnum import StatusEnum

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

@router.get(
    "/{category}/{country}/{kind)",
    response_model=List[Media],
    description="Get all Media by category, kind and country",
)
def get_media_actif_by_categorie_kind_country(category: str, country: str, kind: str):
    if(category == "all" and country == "all" and kind == "all"):
        return conn.execute(medias.select()
                .where(medias.c.status == StatusEnum.ACTIVED.value)
                ).fetchall();
    elif(category != "all" and country == "all" and kind == "all") :
        return conn.execute(medias.select()
                .where(medias.c.category == category)
                .where(medias.c.status == StatusEnum.ACTIVED.value)
                ).fetchall()
    elif(category == "all" and country != "all" and kind == "all") :
        return conn.execute(medias.select()
                .where(medias.c.country == country)
                .where(medias.c.status == StatusEnum.ACTIVED.value)
                ).fetchall()
    elif(category == "all" and country == "all" and kind != "all") :
        return conn.execute(medias.select()
                .where(medias.c.kind == kind)
                .where(medias.c.status == StatusEnum.ACTIVED.value)
                ).fetchall()
    elif(category != "all" and country != "all" and kind == "all") :
        return conn.execute(medias.select()
                .where(medias.c.category == category)
                .where(medias.c.country == country)
                .where(medias.c.status == StatusEnum.ACTIVED.value)
                ).fetchall()
    elif(category == "all" and country != "all" and kind != "all") :
        return conn.execute(medias.select()
                .where(medias.c.country == country)
                .where(medias.c.kind == kind)
                .where(medias.c.status == StatusEnum.ACTIVED.value)
                ).fetchall()
    elif(category != "all" and country == "all" and kind != "all") :
        return conn.execute(medias.select()
                .where(medias.c.category == country)
                .where(medias.c.kind == kind)
                .where(medias.c.status == StatusEnum.ACTIVED.value)
                ).fetchall()
    else:
        return conn.execute(medias.select()
                .where(medias.c.category == category)
                .where(medias.c.country == country)
                .where(medias.c.kind == kind)
                .where(medias.c.status == StatusEnum.ACTIVED.value)
                ).fetchall()

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
        "country": media.country,
        "description" : media.description,
        "status": media.status,
        "id_poster": media.id_poster
        }
    result = conn.execute(medias.insert().values(new_media))
    return conn.execute(medias.select().where(medias.c.id == result.lastrowid)).first()

@router.put(
    "/{id}",
    response_model=Media, 
    description="Update a Media by Id"
)
def update_media(media: Media, id: int):
    conn.execute(
        medias.update()
        .values(
                title=media.title, 
                kind=media.kind,
                category=media.category,
                content=media.content,
                release_date=media.release_date,
                country=media.country,
                description=media.description,
                status=media.status,
                id_poster=media.id_poster
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
