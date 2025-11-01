from fastapi_users.authentication import AuthenticationBackend
from core.authentication.transport import bearer_transport

auth_backend = AuthenticationBackend(
    name="access-token",
    transport=bearer_transport,
)
