from fastapi import APIRouter, HTTPException, status

from ..models import Package, find_packages, mem_db

router = APIRouter()

OptStr = str | None


@router.post('/packages', status_code=status.HTTP_201_CREATED)
async def create_package(package: Package) -> None:
    if find_packages(id=package.id):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Package already exists')
    mem_db.append(package)


@router.get('/packages')
async def list_packages(
    id: OptStr = None, return_address: OptStr = None, destination_address: OptStr = None
) -> list[Package]:
    return find_packages(id, return_address, destination_address)
