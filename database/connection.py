from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


def connect(app: FastAPI):
    register_tortoise(
        app,
        db_url="sqlite://database/db.sqlite3",
        modules={
            'models': ['database.Models.User']
        },
        generate_schemas=True,
        add_exception_handlers=True
    )




