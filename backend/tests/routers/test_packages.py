from httpx import AsyncClient
from pydantic import TypeAdapter

from anovium.models import Package, find_packages


async def test_create_package(client: AsyncClient) -> None:
    package = Package(id='10', return_address='Test Package', destination_address='Test Package')
    response = await client.post('/packages', json=package.model_dump())
    assert response.status_code == 201
    assert find_packages(id='10') == [package]

    # Test duplicate package
    response = await client.post('/packages', json=package.model_dump())
    assert response.status_code == 409


async def test_list_packages(client: AsyncClient, populate_packages: list[Package]) -> None:
    response = await client.get('/packages')
    assert response.status_code == 200
    packages = TypeAdapter(list[Package]).validate_python(response.json())
    assert packages == populate_packages

    # Test filtering by id
    response = await client.get('/packages', params={'id': '1'})
    assert response.status_code == 200
    packages = TypeAdapter(list[Package]).validate_python(response.json())
    assert packages == [populate_packages[0]]

    # Test filtering by return_address
    response = await client.get('/packages', params={'return_address': 'Address 3'})
    assert response.status_code == 200
    packages = TypeAdapter(list[Package]).validate_python(response.json())
    assert len(packages) == 2

    # Test filtering by destination_address
    response = await client.get('/packages', params={'destination_address': 'Address 2'})
    assert response.status_code == 200
    packages = TypeAdapter(list[Package]).validate_python(response.json())
    assert len(packages) == 2

    # Test filtering by id and return_address
    response = await client.get('/packages', params={'id': '1', 'return_address': 'Address 1'})
    assert response.status_code == 200
    packages = TypeAdapter(list[Package]).validate_python(response.json())
    assert packages == [populate_packages[0]]

    # empty result
    response = await client.get('/packages', params={'id': '1', 'return_address': 'tralala'})
    assert response.status_code == 200
    packages = TypeAdapter(list[Package]).validate_python(response.json())
    assert packages == []
