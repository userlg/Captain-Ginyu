from src import utils as u

import os


def test_get_folders_is_type_list() -> None:
    folders = u.get_folders()
    assert type(folders) == list


def test_get_folders_greater_than_zero() -> None:
    folders = u.get_folders()
    assert len(folders) > 0


def test_show_folders_with_list_of_elements() -> None:
    folders = ["f1", "f2", "f3"]
    assert u.show_folders(folders) == 3


def test_show_folders_with_list_of_zero_elements() -> None:
    folders = []
    assert u.show_folders(folders) == 0


def test_temporizer_using_one_second() -> None:
    assert u.temporizer(1) == 0


def test_phrases_works_properly() -> None:
    assert u.phrases() == True


def test_is_ordered_with_order_values() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert u.list_is_ordered_properly(numbers) == True


def test_is_ordered_with_not_order_values() -> None:
    numbers = [23, -2, 3, 4, 5, 6, 7, 89]
    assert u.list_is_ordered_properly(numbers) == False


def test_order_customizer() -> None:
    folders = [
        "Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup3",
        "Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup1",
        "Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Malocclusion",
        "Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup2",
    ]

    response = u.order_customizer(folders, len(folders) - 1)
    assert len(response) == 4
    assert u.list_is_ordered_properly(response) == True


def test_procesing_files() -> None:
    folders = []
    assert u.procesing_files(folders) == False


def test_procesing_files_maxillary_properly() -> None:

    newpath = "tmp/"
    maxillary = newpath + "Maxillary_fake_file.stl"

    os.makedirs(newpath)

    fmax = open(maxillary, "+w")
    fmax.close()

    response = u.procesing_files([newpath])

    os.remove("Maxillary0.stl")
    os.rmdir(newpath)

    assert response == True


def test_procesing_files_mandibular_properly() -> None:

    newpath = "tmp/"
    mandibular = newpath + "Mandibular_fake_file.stl"

    os.makedirs(newpath)

    fmax = open(mandibular, "+w")
    fmax.close()

    response = u.procesing_files([newpath])

    os.remove("Mandibular0.stl")
    os.rmdir(newpath)

    assert response == True
