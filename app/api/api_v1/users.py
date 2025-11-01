from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.security import HTTPBearer
from core.config import settings
from core.schemas.user import UserRead, UserUpdate
from .fastapi_users import fastapi_users

bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=settings.api.v1.users, tags=["Users"], dependencies=[Depends(bearer)]
)

router.include_router(
    fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    )
)
