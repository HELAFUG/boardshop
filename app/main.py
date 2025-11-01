from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.config import settings
from core.models import db_helper
from api import api_router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
