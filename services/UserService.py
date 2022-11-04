from database.Models.User import User, user_form_request, user_resource


async def store_user(request: user_form_request):
    user_object = await User.create(
        first_name=request.first_name,
        last_name=request.last_name,
        other_names=request.other_names,
        username=request.username,
        email=request.email,
        mobile_number=request.mobile_number,
        password=request.password,
    )
    resource = await user_resource.from_tortoise_orm(user_object)
    return [user_object, resource]





