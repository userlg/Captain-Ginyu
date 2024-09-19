import os

import time as t

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
            print(Fore.YELLOW + "\t" + folder)
    else:
        print(Fore.RED + "No folders detected")
    print("\n")
    return len(folders)


def temporizer(seconds: int) -> int:
    i = seconds
    while i:
        print("\tWait " + str(i) + " seconds", end="\r")
        i -= 1
        t.sleep(1)

    print(Fore.GREEN + "\n\t Closing Script \n")
    return i
