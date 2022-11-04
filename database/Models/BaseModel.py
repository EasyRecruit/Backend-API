from tortoise.models import Model
from tortoise import fields


class BaseModel(Model):
    id: Option[int] = fields.IntField(pk=True, generated=True)
    created_at = fields.DatetimeField(auto_now_add=True, null=True, generated=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True, generated=True)

    class Meta:
        abstract = True




