from fastapi import APIRouter
from core.config import settings
from core.schemas.user import UserCreate, UserRead
from api.dependencies.authentication import auth_backend
from .fastapi_users import fastapi_users


router = APIRouter(prefix=settings.api.v1.auth, tags=["Auth"])
router.include_router(
    fastapi_users.get_auth_router(backend=auth_backend),
)
router.include_router(
    fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    )
)
