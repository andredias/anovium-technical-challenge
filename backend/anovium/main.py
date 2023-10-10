from fastapi import FastAPI

from . import config
from .resources import lifespan
from .routers import hello, packages

app = FastAPI(
    title='Anovium Techinical Challenge',
    debug=config.DEBUG,
    lifespan=lifespan,
)

routers = (hello.router, packages.router)

for router in routers:
    app.include_router(router)
