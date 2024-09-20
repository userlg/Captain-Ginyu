import os

import time as t

from colorama import Fore, init

from src import quick_sort as q

import random as r

init()


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
        print(Fore.YELLOW + "\t\t<<--- Lista de Directorios a procesar --->>\n")
        for folder in folders:
            print(Fore.YELLOW + "\t" + folder)
    else:
        print(Fore.RED + "No se detectaron directorios")
    print("\n")
    return len(folders)


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

    phrases = [
        "Ir por una taza de cafe",
        "Jugar dos partidas de Fortnite",
        "Enviar fax a Maduro",
        "Escribir en tu diario personal",
        "Retocar tu maquillaje",
        "Caminar dos cuadras y volver",
        "Jugar un par de partidas de DBD",
        "Ver una pelicula masculina como Titanic",
        "Ir a comer un helado",
        "Leer tu libro favorito",
        "Darle un beso a la persona mas cercana",
        "Comer una hamburguesa vegana",
        "Buscar en google como hacer del numero dos correctamente",
        "Preparar una parrillada con todo",
        "Escribir todas las groserias conocidas en papel",
        "Colocar un rollo de papel nuevo en el baño",
        "Escribir tu carta a Santa Claus",
        "Participar en la encuesta para ilegalizar el regueton",
    ]

    print(Fore.GREEN + "\n\t\t\t\t Bienvenido al capitan Ginyu Script \n")
    print(
        Fore.GREEN
        + "\t <<---Debido a la complejidad de la operacion la tarea tardara unos minutos, --->>"
    )
    print(
        Fore.GREEN
        + "\t <<---Asi que recomendamos hacer la siguiente actividad para aprovechar su tiempo --->>"
    )
    print(Fore.MAGENTA + "\n\t" + r.choice(phrases) + "\n")

    return True


def list_is_ordered_properly(folders: list) -> bool:
    ordered = True
    for i in range(1, len(folders)):
        if folders[i] < folders[i - 1]:
            ordered = False
            break
    return ordered


def order_customizer(folders: list[str], limit: int) -> list:

    folders_ordered = []

    malocclusion = "Malocclusion"

    for folder in folders:
        if malocclusion in folder:
            folders_ordered.append(folder)
            break

    i = 1

    while i <= limit:
        for folder in folders:
            if folder.endswith("Subsetup" + str(i)):
                folders_ordered.append(folder)
                break
        i += 1

    return folders_ordered


def procesing_files(folders: list[str]) -> bool:

    root = os.getcwd()

    i = 0
    if len(folders) > 0:
        for folder in folders:
            dir = root + "/" + folder + "/"
            files = os.listdir(dir)

            for file in files:
                if (
                    file.endswith(".stl")
                    and file.startswith("Maxillary")
                    and not "backup" in file
                ):
                    new_name_maxillary = "Maxillary" + str(i) + ".stl"
                    os.rename(dir + file, root + "/" + new_name_maxillary)

                if (
                    file.endswith(".stl")
                    and file.startswith("Mandibular")
                    and not "backup" in file
                ):
                    new_name_mandibular = "Mandibular" + str(i) + ".stl"
                    os.rename(dir + file, root + "/" + new_name_mandibular)

            i += 1
        return True
    else:
        return False
