from pydantic import BaseModel


class Package(BaseModel):
    id: str
    destination_address: str
    return_address: str


mem_db: list[Package] = []


def find_packages(
    id: str | None = None, return_address: str | None = None, destination_address: str | None = None
) -> list[Package]:
    def validate_id(p: Package) -> bool:
        return p.id == id

    def validate_return_address(p: Package) -> bool:
        return p.return_address == return_address

    def validate_destination_address(p: Package) -> bool:
        return p.destination_address == destination_address

    validations = []
    if id is not None:
        validations.append(validate_id)
    if return_address is not None:
        validations.append(validate_return_address)
    if destination_address is not None:
        validations.append(validate_destination_address)
    return [package for package in mem_db if all(validate(package) for validate in validations)]
