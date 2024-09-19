
from src.utils import show_folders

def test_show_folders() -> None:
    folders = show_folders()
    assert folders == list