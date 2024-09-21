from src import utils as u, quick_sort as q

import time as t


def main() -> None:
    u.phrases()
    t.sleep(2)
    folders = u.get_folders()
    new_directories = u.order_customizer(folders, len(folders))
    u.show_folders(new_directories)
    # u.procesing_files(new_directories)
    u.temporizer(15)


if __name__ == "__main__":
    main()
