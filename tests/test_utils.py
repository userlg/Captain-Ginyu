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


def test_order_customizer_with_malocclusion() -> None:
    folders = [
        "Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup3",
        "Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup1",
        "Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Malocclusion",
        "Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup2",
    ]

    response = u.order_customizer(folders, len(folders) - 1)
    assert len(response) == 4
    assert u.list_is_ordered_properly(response) == True


def test_order_customizer_without_malocclusion() -> None:
    folders = [
        "Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup3",
        "Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup2",
        "Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup1",
    ]

    response = u.order_customizer(folders, len(folders))
    assert len(response) == 3
    assert u.list_is_ordered_properly(response) == True


def test_procesing_files_with_zero_directories() -> None:
    folders = []
    assert u.procesing_files(folders) == False


def test_identify_index_works_properly() -> None:
    directories = [
        "tmp/Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup1",
        "tmp/Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup2",
        "tmp/Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup3",
    ]
    assert (u.identify_index(directories)) == 1


def test_identify_index_not_found_index_code_101_return() -> None:
    directories = [
        "tmp/Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup150",
    ]
    assert (u.identify_index(directories)) == 101


def test_procesing_files_maxillary_properly() -> None:

    newpath = "tmp/"

    directories = [
        "tmp/Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup1",
        "tmp/Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup2",
        "tmp/Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup3",
    ]

    for directory in directories:
        os.makedirs(directory)
        maxillary = directory + "/" + "Maxillary_fake_file.stl"
        fmax = open(maxillary, "+w")
        fmax.close()

    response = u.procesing_files(directories)

    os.remove("Maxillary1.stl")
    os.remove("Maxillary2.stl")
    os.remove("Maxillary3.stl")

    for directory in directories:
        os.rmdir(directory)

    os.rmdir(newpath)

    assert True == True


def test_procesing_files_mandibular_properly() -> None:

    newpath = "tmp/"

    directories = [
        "tmp/Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup1",
        "tmp/Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup2",
        "tmp/Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup3",
    ]

    for directory in directories:
        os.makedirs(directory)
        mandibular = directory + "/" + "Mandibular_fake_file.stl"
        fmax = open(mandibular, "+w")
        fmax.close()

    response = u.procesing_files(directories)

    os.remove("Mandibular1.stl")
    os.remove("Mandibular2.stl")
    os.remove("Mandibular3.stl")

    for directory in directories:
        os.rmdir(directory)

    os.rmdir(newpath)

    assert True == True


def test_procesing_files_malocclusion_properly() -> None:

    newpath = "tmp/"

    directories = [
        "tmp/Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Malocclusion",
        "tmp/Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup1",
        "tmp/Francini Jimenez Alpizar_Francini Jimenez Alpizar_9-9-2024_10-43-03_Subsetup2",
    ]

    for directory in directories:
        os.makedirs(directory)
        mandibular = directory + "/" + "Mandibular_fake_file.stl"
        fmax = open(mandibular, "+w")
        fmax.close()

    response = u.procesing_files(directories)

    i = 0
    for directory in directories:
        os.remove("Mandibular" + str(i) + ".stl")
        os.rmdir(directory)
        i += 1

    os.rmdir(newpath)

    assert len(directories) == 3

    assert response == True
