

from colorama import init, Fore

from src import utils as u

init()

if __name__ == "__main__":
    print(Fore.GREEN + "\n\t\t\t Welcome to Ginyu Script \n")
    print(Fore.GREEN + "\t <<---Working -- We recommend go for a cup of coffe :) --->>")
    folders = u.get_folders()
    u.show_folders(folders)
    u.temporize(5)