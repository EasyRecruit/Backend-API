from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from database.Models.BaseModel import BaseModel


class User(BaseModel):
    first_name = fields.CharField(max_length=225)
    last_name = fields.CharField(max_length=225)
    other_names = fields.CharField(max_length=225)
    username = fields.CharField(max_length=225, unique=True)
    email = fields.CharField(max_length=225, unique=True)
    mobile_number = fields.CharField(max_length=20, unique=True)
    password = fields.TextField()


user_resource = pydantic_model_creator(User, name='User')
user_form_request = pydantic_model_creator(User, name='User', exclude_readonly=True)






