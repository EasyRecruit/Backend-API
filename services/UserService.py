from database.Models.User import User, user_form_request, user_resource
from passlib.hash import bcrypt


async def store_user(request: user_form_request):
    user = User(
        first_name=request.first_name,
        last_name=request.last_name,
        other_names=request.other_names,
        username=request.username,
        email=request.email,
        mobile_number=request.mobile_number,
        account_type=request.account_type,
        password_hash=bcrypt.hash(request.password_hash),
    )
    await user.save()
    resource = await user_resource.from_tortoise_orm(user)
    return [user, resource]


async def authentic_user(username: str, password: str):
    user = await User.get(username=username)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user




