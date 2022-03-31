from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.medias import router as media
from config.openapi import tags_metadata
import os

app = FastAPI(
    title="WebServiceNetflix - Media",
    description="a REST API using python and mysql",
    version="0.0.1",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(media)
