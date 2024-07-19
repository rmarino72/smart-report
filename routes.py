from fastapi import APIRouter, status as s

from models.api_model import MessageModel

routes = APIRouter(prefix="", tags=["home"])


@routes.get('/',
            response_model=MessageModel,
            status_code=s.HTTP_200_OK,
            name="Root api")
async def root():
    """
    This is a test api
    """
    return {'message': 'ok'}
