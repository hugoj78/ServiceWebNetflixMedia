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

project0api_url = os.environ['PROJECT_API_URL']

router = APIRouter(
    prefix="/gestion",
    tags=["gestion"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "",
    response_model=List[Media],
    description="Get a list of all posters",
)
def get_gestion_medias():
    medias = conn.execute(medias.select()).fetchall()
    print(medias)
