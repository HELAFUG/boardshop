from fastapi import APIRouter
from core.config import settings

v1_router = APIRouter(prefix=settings.api.v1.prefix)
