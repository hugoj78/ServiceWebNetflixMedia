from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.db import meta, engine

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
    Column("id_poster", Text)
)

meta.create_all(engine)