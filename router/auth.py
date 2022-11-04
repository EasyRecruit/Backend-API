from fastapi import APIRouter
from database.Models.User import User, user_form_request
from services import UserService

router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
    responses={404: {'description': 'API Resource not found'}}
)


@router.post('/register')
async def register(request: user_form_request):
    user = await UserService.store_user(request=request)
    return user[1]


@router.post('/login')
async def login():
    pass

