from fastapi_users.authentication import AuthenticationBackend
from core.authentication.transport import bearer_transport
from .strategy import get_db_strategy

auth_backend = AuthenticationBackend(
    name="access-token", transport=bearer_transport, get_strategy=get_db_strategy
)
