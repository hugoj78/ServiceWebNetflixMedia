from fastapi import APIRouter, Depends, HTTPException, status, FastAPI
import requests
from config.db import conn
from src.models.medias import medias
from src.schemas.medias import Media, MediaUpdateDescription
from src.routes.medias import get_medias, get_media_actif_by_categorie_kind_country
from typing import List, Union
from starlette.status import HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from sqlalchemy import func, select, and_
import json
import os
from src.models.StatusEnum import StatusEnum

router = APIRouter(
    prefix="/gestion",
    tags=["gestion"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/{id}/{category}/{moment}/{kind}",
    description="Get a list of all Media and Poster for a defined User by",
)
def get_gestion_medias(id: int, category: str, moment: str, kind: str):

    headers = {'accept': 'application/json'}
    url = os.environ['COMPTE_URL']
    base_url = f"{url}/users/{id}"

    try:
        request = requests.get(url=base_url, headers=headers).json()

        if (request['status'] == 'ACTIF'):
            myData = []
            
            myMediaToReturn = get_media_actif_by_categorie_kind_country(category, request['country'], kind)
            urlOSPoster = os.environ['POSTER_URL']

            print("1")

            for media in myMediaToReturn:

                urlPoster = f"{urlOSPoster}/posters/{media['id']}/{moment}"

                myPoster = requests.get(url=urlPoster, headers=headers).json()

                toAppend = {
                    "id": media['id'],
                    "title": media['title'],
                    "kind": media['kind'],
                    "category": media['category'],
                    "content": media['content'],
                    "release_date": media['release_date'],
                    "country": media['country'],
                    "description": media['description'],
                    "status": media['status'],
                    "id_poster": media['id_poster'],
                    "poster": myPoster[f"{moment}_poster"]
                }

                myData.append(toAppend)

            return myData

        else:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Incorrect User Statut"
            )
    except Exception as e:
        print(e)


@router.put(
    "/{id}/{admin}",
    description="Update a Media by Id if Admin"
)
def update_media_description(media: MediaUpdateDescription, id: str, admin: str):

    headers = {'accept': 'application/json'}
    url = os.environ['COMPTE_URL']
    base_url = f"{url}/users/{admin}"

    try:
        request = requests.get(url=base_url, headers=headers).json()

        print(request['admin'])

        if (request['admin']):

            conn.execute(
                medias.update()
                .values( 
                    description=media.description
                )
                .where(medias.c.id == id)
            )
            return "Update success"
        else:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Incorrect User Admin statut"
            )
    except Exception as e:
        print(e)

@router.delete(
    "/{id}/{admin}",
    description="Update a Media by Id if Admin"
)
def delete_media_description(id: str, admin: str):

    headers = {'accept': 'application/json'}
    url = os.environ['COMPTE_URL']
    base_url = f"{url}/users/{admin}"

    try:
        request = requests.get(url=base_url, headers=headers).json()

        print(request['admin'])

        if (request['admin']):

            conn.execute(
                medias.update()
                .values( 
                    status=StatusEnum.DELETED.value
                )
                .where(medias.c.id == id)
            )
            return "Delete success"
        else:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Incorrect User Admin statut"
            )
    except Exception as e:
        print(e)