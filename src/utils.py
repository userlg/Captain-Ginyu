import os

from colorama import Fore


def show_folders() -> list:
    root = os.getcwd()

    content = os.listdir(root)

    files = []

    for file in content:
        if os.path.isdir(file) and not file.startswith("."):
            files.append(file)

    return files

'''
    if len(files) > 0:
        i = 1

        for file in files:
            os.rename(file, "new_name_" + str(i))
            i += 1
        print(Fore.GREEN + "Operation Successfull")
    else:
        print(Fore.RED + "No folders detected")
'''