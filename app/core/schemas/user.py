from fastapi_users import schemas


from core.types import UserIDType


class UserRead(schemas.BaseUser[UserIDType]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
