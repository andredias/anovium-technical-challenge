from anovium.models import Package, find_packages


def test_find_packages(populate_packages: list[Package]) -> None:
    assert find_packages() == populate_packages
    assert find_packages(id='1') == [populate_packages[0]]
    assert find_packages(id='1', return_address='Address 1') == [populate_packages[0]]
    assert find_packages(id='1', return_address='Address 1', destination_address='Address 2') == [
        populate_packages[0]
    ]
    assert find_packages(id='1', return_address='Address 1', destination_address='Address 3') == []
    assert len(find_packages(return_address='Address 3')) == 2
    assert len(find_packages(destination_address='Address 2')) == 2
