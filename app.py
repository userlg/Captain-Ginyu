from src import utils as u, quick_sort as q

if __name__ == "__main__":
    u.phrases()
    folders = u.get_folders()
    new_directories = u.order_customizer(folders, len(folders) - 1)
    u.show_folders(new_directories)
    u.procesing_files(new_directories)
    u.temporizer(3)
