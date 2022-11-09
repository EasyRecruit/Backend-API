from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
import jwt
from database.Models.User import User
from settings.env import Env

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')


async def auth_middleware(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, Env().APP_KEY, algorithms=['HS256'])
        user = await User.get(id=payload.get('id'))
        return user
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Unauthorized'
        )


