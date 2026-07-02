from contextlib import asynccontextmanager

from fastapi import FastAPI


from app.core.exception_handler import app_exception_handler
from app.core.exceptions import AppException

app = FastAPI()
# app.include_router(router)
app.add_exception_handler(AppException, app_exception_handler)
