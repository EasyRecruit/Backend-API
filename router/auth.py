from fastapi import APIRouter, Depends, HTTPException, status
from database.Models.User import user_form_request, user_resource
from services import UserService
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import jwt
from utilities.response import success_response
from utilities.dependencies import auth_middleware
from settings.env import Env


router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
    responses={
        404: {'description': 'API Resource not found'},
    }
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')


@router.post('/register', response_model=user_resource)
async def register(request: user_form_request):
    user = await UserService.store_user(request=request)
    return user[1]


@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends()):
    user = await UserService.authentic_user(request.username, request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid credentials'
        )
    user_res = await user_resource.from_tortoise_orm(user)
    token = jwt.encode(user.encryptable_fields(), Env().APP_KEY)
    return {
        'access_token': token,
        'token_type': 'bearer',
    }


@router.get('/test-login')
async def let_test(request=Depends(auth_middleware)):
    return success_response("success passed")


