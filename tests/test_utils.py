from src.utils import get_folders, show_folders


def test_get_folders_is_type_list() -> None:
    folders = get_folders()
    assert type(folders) == list


def test_get_folders_greater_than_zero() -> None:
    folders = get_folders()
    assert len(folders) > 0


def test_show_folders_with_list_of_elements() -> None:
    folders = ["f1", "f2", "f3"]
    assert show_folders(folders) == 3


def test_show_folders_with_list_of_zero_elements() -> None:
    folders = []
    assert show_folders(folders) == 0
