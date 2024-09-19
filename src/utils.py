import os

from colorama import Fore


def get_folders() -> list:
    root = os.getcwd()

    content = os.listdir(root)

    files = []

    for file in content:
        if os.path.isdir(file) and not file.startswith("."):
            files.append(file)

    return files


def show_folders(folders: list) -> int:
    if len(folders) > 0:
        for folder in folders:
            print(Fore.YELLOW + folder + "\n")
    else:
        print(Fore.RED + "No folders detected")
    return len(folders)
