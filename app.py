from src import ordering as q, utils as u

import time as t


def main() -> None:
    u.phrases()
    t.sleep(2)
    folders = u.get_folders()
    new_directories = u.order_customizer(folders, len(folders))
    u.show_folders(new_directories)
    u.procesing_files(new_directories)
    u.temporizer(4)


if __name__ == "__main__":
    main()
