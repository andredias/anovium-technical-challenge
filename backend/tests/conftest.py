import os
from collections.abc import AsyncIterable, Generator
from unittest.mock import patch

from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient
from pytest import fixture

os.environ['ENV'] = 'testing'

from anovium.main import app as _app  # noqa: E402
from anovium.models import Package  # noqa: E402


@fixture
async def app() -> AsyncIterable[FastAPI]:
    """
    Create a FastAPI instance.
    """
    async with LifespanManager(_app):
        yield _app


@fixture
async def client(app: FastAPI) -> AsyncIterable[AsyncClient]:
    async with AsyncClient(app=app, base_url='http://testserver') as client:
        yield client


@fixture
def populate_packages() -> Generator[list[Package], None, None]:
    packages = [
        Package(id='1', return_address='Address 1', destination_address='Address 2'),
        Package(id='2', return_address='Address 3', destination_address='Address 4'),
        Package(id='3', return_address='Address 5', destination_address='Address 6'),
        Package(id='4', return_address='Address 1', destination_address='Address 8'),
        Package(id='5', return_address='Address 3', destination_address='Address 2'),
    ]
    with patch('anovium.models.mem_db', packages):
        yield packages
