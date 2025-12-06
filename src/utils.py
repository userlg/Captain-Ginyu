import os

import time as t

from colorama import Fore, init

from src.phrases_list import PHRASES

from src import ordering as q

import random as r

import emoji as e

init()


def get_emojis() -> str:
    emojis = [
        "\U0001f602",
        "\U0001f605",
        "\U0001f60d",
        "\U0001f92d",
        "\U0001f92b",
        "\U0001f914",
        "\U0001f62a",
        "\U0001f922",
        "\U0001f976",
        "\U0001f92f",
        "\U0001f60d",
    ]

    return r.choice(emojis)


def get_folders() -> list:
    root = os.getcwd()

    content = os.listdir(root)

    files = []

    for file in content:
        if os.path.isdir(file) and not file.startswith("."):
            files.append(file)
    return files


def show_folders(folders: list) -> int:

    size = len(folders)

    if size > 0:
        print(Fore.YELLOW + "\t\t<<--- Lista de Directorios a procesar --->>\n")
        print(
            Fore.YELLOW + "\t\t<<--- Cantidad de Elementos: " + str(size) + " --->>\n"
        )
        for folder in folders:
            print(Fore.YELLOW + "\t" + folder)
    else:
        print(Fore.RED + "\tNo se detectaron directorios")
    print("\n")
    return size


def temporizer(seconds: int) -> int:
    i = seconds
    while i:
        print("\tEspere " + str(i) + " segundos", end="\r")
        i -= 1
        t.sleep(1)

    print(Fore.GREEN + "\n\n\tCerrando Script \n")
    t.sleep(1)
    return i


def phrases() -> bool:

    print(Fore.GREEN + "\n\t\t\t\t Bienvenido al capitan Ginyu Script \n")
    print(
        Fore.GREEN
        + "\t <<---Debido a la complejidad de la operacion la tarea tardara unos minutos, --->>"
    )
    print(
        Fore.GREEN
        + "\t <<---Asi que recomendamos hacer la siguiente actividad para aprovechar su tiempo --->>"
    )

    emoji = e.emojize(get_emojis())

    print(Fore.MAGENTA + "\n\t" + r.choice(PHRASES) + " " + emoji + "\n")

    return True


def list_is_ordered_properly(folders: list) -> bool:
    ordered = True
    for i in range(1, len(folders)):
        if folders[i] < folders[i - 1]:
            ordered = False
            break
    return ordered


def extract_digits(number: int) -> list:
    numbers = []
    while number != 0:
        digit = int(number % 10)
        numbers.append(digit)
        number = int(number / 10)
    numbers.reverse()
    return numbers


def order_customizer(folders: list[str], limit: int) -> list:

    folders_ordered = []

    malocclusion = "Malocclusion"
    exists_malocclusion = False

    for folder in folders:
        if malocclusion in folder:
            folders_ordered.append(folder)
            exists_malocclusion = True
            break

    if exists_malocclusion:
        index = 1
    else:
        index = identify_index(folders)

    j = 1

    while j <= limit:
        for folder in folders:
            if folder.endswith("Subsetup" + str(index)):
                index += 1
                folders_ordered.append(folder)
                break
        j += 1

    return folders_ordered


def identify_index(folders: list[str]) -> int:
    index = 1
    numbers = []
    while index < 100:
        for folder in folders:
            size = len(folder)
            if index < 10:
                if folder[size - 1] == str(index) and folder[size - 2] == "p":
                    return index
            if index > 9 and index < 100:
                numbers = extract_digits(index)
                if (
                    folder[size - 2] == str(numbers[0])
                    and folder[size - 1] == str(numbers[1])
                    and folder[size - 3] == "p"
                ):
                    return index

        index += 1
    return index


def procesing_files(folders: list[str]) -> bool:

    if len(folders) == 0:
        return False
    else:
        root = os.getcwd()

        if "Malocclusion" in folders[0]:
            index = 0
        else:
            index = identify_index(folders)

        for folder in folders:

            dir = root + "/" + folder + "/"
            files = os.listdir(dir)

            for file in files:
                if (
                    file.endswith(".stl")
                    and file.startswith("Maxillary")
                    and not "backup" in file
                ):
                    new_name_maxillary = "Maxillary" + str(index) + ".stl"
                    os.rename(dir + file, root + "/" + new_name_maxillary)
                if (
                    file.endswith(".stl")
                    and file.startswith("Mandibular")
                    and not "backup" in file
                ):
                    new_name_mandibular = "Mandibular" + str(index) + ".stl"
                    os.rename(dir + file, root + "/" + new_name_mandibular)
            index += 1
        return True
