from fastapi import FastAPI, APIRouter
from router import auth
from database import connection


app = FastAPI()
app.include_router(auth.router)

connection.connect(app)



