from fastapi import APIRouter, Depends
import requests
from config.db import conn
from src.models.medias import medias
from src.schemas.medias import Media
from typing import List, Union
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select, and_
import json
import os

router = APIRouter(
    prefix="/gestion",
    tags=["gestion"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "/{id}",
    description="Get a list of all Media and Poster for a defined User",
)
def get_gestion_medias(id: int):

    headers = {'accept': 'application/json'}
    url = os.environ['COMPTE_URL']
    base_url = f"{url}/users/{id}"
    print(base_url)
    try:
        request = requests.get(url=base_url, headers=headers)
        print(request.status_code)
        print("ICI")
        print(request.text)
    except Exception as e:
        print(e)
    
    return {}

