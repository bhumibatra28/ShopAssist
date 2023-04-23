from fastapi import APIRouter
from .query import queryRouter

appRouter = APIRouter()

appRouter.include_router(queryRouter)