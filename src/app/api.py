import logging
import os

from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from fastapi.logger import logger as fastAPI_logger

from app.routes import customers, orders #, items


APP_LOG_LEVEL = os.getenv("APP_LOG_LEVEL", "INFO")
ENV = os.getenv("ENV", "preprod")

fastAPI_logger.handlers = logging.getLogger('uvicorn').handlers
main_router = APIRouter(tags=["main"])

@main_router.get("/")
async def root():
    return {"message": "Hello World"}

@main_router.get('/health')
async def health():
    """
    Determine if the container is working and healthy
    """
    status = 200
    result = {
        'status': 200,
        'api_version': 42,  # TODO
    }

    return JSONResponse(content=result, status_code=status)

async def on_start_up() -> None:
    fastAPI_logger.info("on_start_up")

async def on_shutdown() -> None:
    fastAPI_logger.info("on_shutdown")


def create_app() -> FastAPI:
    """
    Main function to create the FastAPI app and settings
    :return:
        fastapi: FastAPI Object
    """
    fastAPI_logger.setLevel(APP_LOG_LEVEL)

    fastapi = FastAPI(docs_url="/",                             # set the swagger at homePage of the api
                      title=f"ecommerce-app {ENV}",             # title of the app
                      description=f"""                          
# Description :

a HTTP REST-API to access data TODO

""",
                      on_startup=[on_start_up],                 # tasks on startup
                      on_shutdown=[on_shutdown])                # tasks on shutdown

    fastapi.include_router(customers.router, prefix="/ecommerce-app")
    fastapi.include_router(orders.router, prefix="/ecommerce-app")
    #fastapi.include_router(items.router, prefix="/ecommerce-app")
    fastapi.include_router(main_router)

    return fastapi

if __name__ == '__main__':  # local dev
    import uvicorn
    #import pyroscope

    # pyroscope.configure(
    #     application_name="my.python.app",
    #     server_address="http://localhost:4040",
    # )

    os.environ["ENV"] = "dev"                                           #used for using the right db settings

    # For being able to use the app you must run the docker-compose to create the db
    uvicorn.run(create_app(), host="0.0.0.0", port=8000)