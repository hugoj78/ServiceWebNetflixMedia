from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text, Boolean, Enum
from config.db import meta, engine
from src.models.StatusEnum import StatusEnum

medias = Table(
    "medias",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", Text),
    Column("kind", Text),
    Column("category", Text),
    Column("content", Text),
    Column("release_date", Text),
    Column("country", Text),
    Column("description", Text),
    Column("status", Enum(StatusEnum)),
    Column("id_poster", String(70), unique=True)
)

meta.create_all(engine)