import os

import time as t

from colorama import Fore, init

from src import ordering as q

from src import ordering as q

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

    size = len(folders)

    if size > 0:
        print(Fore.YELLOW + "\t\t<<--- Lista de Directorios a procesar --->>\n")
        print(
            Fore.YELLOW + "\t\t<<--- Cantidad de Elementos: " + str(size) + " --->>\n"
        )
        for folder in folders:
            print(Fore.YELLOW + "\t" + folder)
    else:
        print(Fore.RED + "No se detectaron directorios")
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
        "Regar las margaritas del jardin",
        "Promulgar leyes antiveganos",
        "Redactar un poema dedicado a la persona mas cercana",
        "Buscar evidencia de la existencia del monstruo del lago ness",
        "Dar una vuelta al mundo",
        "Meditar con los monjes tibetanos sobre el significado de la vida",
        "Infitrarse en la comunidad vegana",
        "Dar click en me gusta en la publicacion de iphone es mejor que android",
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
    limit = len(folders)
    print("Elementos: " + str(limit))
    show_folders(folders)
    while index <= 100:
        for folder in folders:
            size = len(folder)
            if folder[size - 1] == str(index) and folder[size - 2] == "p":
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
