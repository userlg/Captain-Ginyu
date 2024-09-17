import time as t

from colorama import init,Fore

from src import utils as u

init()

if __name__ == '__main__':
    print(Fore.GREEN + 'Working')
    u.show_folders()
    t.sleep(10)
    