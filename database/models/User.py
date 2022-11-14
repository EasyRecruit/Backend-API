from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from database.Models.BaseModel import BaseModel
from passlib.hash import bcrypt


class User(BaseModel):
    first_name = fields.CharField(max_length=225)
    last_name = fields.CharField(max_length=225)
    other_names = fields.CharField(max_length=225)
    username = fields.CharField(max_length=225, unique=True)
    email = fields.CharField(max_length=225, unique=True)
    mobile_number = fields.CharField(max_length=20, unique=True)
    password_hash = fields.CharField(128)
    account_type = fields.CharField(128)  # superadmin or user

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)

    def encryptable_fields(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'other_names': self.other_names,
            'username': self.username,
            'email': self.email,
            'mobile_number': self.mobile_number,
        }


user_resource = pydantic_model_creator(User, name='UserResource')
user_form_request = pydantic_model_creator(User, name='UserFormRequest', exclude_readonly=True)
