from fastapi import APIRouter
from .queryV3 import queryRouter as queryRouterV3
from .queryV1 import queryRouter as queryRouterV1
from .queryV2 import queryRouter as queryRouterV2

appRouter = APIRouter()

appRouter.include_router(queryRouterV1,prefix='/v1')
appRouter.include_router(queryRouterV2,prefix='/v2')
appRouter.include_router(queryRouterV3,prefix='/v3')