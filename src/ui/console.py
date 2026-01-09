"""Console UI for Captain Ginyu Script."""

import random
import time
from typing import List

import emoji as e
from colorama import Fore, init

from src.logger import get_logger
from src.models import ProcessingResult
from src.phrases_list import PHRASES


# Initialize colorama
init()

logger = get_logger(__name__)


def get_random_emoji() -> str:
    """Get a random emoji from a predefined list.
    
    Returns:
        str: Random emoji character.
    """
    emojis = [
        "\U0001f602",  # 😂
        "\U0001f605",  # 😅
        "\U0001f60d",  # 😍
        "\U0001f92d",  # 🤭
        "\U0001f92b",  # 🤫
        "\U0001f914",  # 🤔
        "\U0001f62a",  # 😪
        "\U0001f922",  # 🤢
        "\U0001f976",  # 🥶
        "\U0001f92f",  # 🤯
        "\U0001f60d",  # 😍
    ]
    return random.choice(emojis)


def display_welcome() -> bool:
    """Display welcome message and random phrase.
    
    Returns:
        bool: Always returns True for backward compatibility.
    """
    print(Fore.GREEN + "\n\t\t\t\t Bienvenido al Capitán Ginyu Script \n")
    print(
        Fore.GREEN
        + "\t <<---Debido a la complejidad de la operación la tarea tardará unos minutos, ----->>"
    )
    print(
        Fore.GREEN
        + "\t <<---Así que recomendamos hacer la siguiente actividad para aprovechar su tiempo --->>"
    )
    
    emoji_char = e.emojize(get_random_emoji())
    phrase = random.choice(PHRASES)
    
    print(Fore.MAGENTA + f"\n\t{phrase} {emoji_char}\n")
    logger.info("Welcome message displayed")
    return True


def display_folders(folders: List[str]) -> None:
    """Display list of folders to be processed.
    
    Args:
        folders: List of folder names.
    """
    size = len(folders)
    
    if size > 0:
        print(Fore.YELLOW + "\t\t<<--- Lista de Directorios a procesar --->>\n")
        print(Fore.YELLOW + f"\t\t<<--- Cantidad de Elementos: {size} --->>\n")
        
        for folder in folders:
            print(Fore.YELLOW + f"\t{folder}")
    else:
        print(Fore.RED + "\tNo se detectaron directorios")
    
    print("\n")
    logger.info(f"Displayed {size} folders")


def display_progress(message: str) -> None:
    """Display a progress message.
    
    Args:
        message: Progress message to display.
    """
    print(Fore.CYAN + f"\t{message}")
    logger.debug(f"Progress: {message}")


def display_countdown(seconds: int) -> None:
    """Display a countdown timer.
    
    Args:
        seconds: Number of seconds to count down.
    """
    i = seconds
    while i > 0:
        print(f"\tEspere {i} segundos", end="\r")
        i -= 1
        time.sleep(1)
    
    print(Fore.GREEN + "\n\n\tCerrando Script \n")
    time.sleep(1)


def display_result(result: ProcessingResult) -> None:
    """Display processing result.
    
    Args:
        result: Processing result to display.
    """
    if result.success:
        print(Fore.GREEN + "\n\t✓ Procesamiento completado exitosamente!")
        print(Fore.GREEN + f"\tCarpetas procesadas: {result.folders_processed}")
        print(Fore.GREEN + f"\tArchivos movidos: {result.files_moved}")
    else:
        print(Fore.RED + "\n\t✗ Procesamiento completado con errores:")
        print(Fore.YELLOW + f"\tCarpetas procesadas: {result.folders_processed}")
        print(Fore.YELLOW + f"\tArchivos movidos: {result.files_moved}")
        
        if result.errors:
            print(Fore.RED + "\n\tErrores encontrados:")
            for error in result.errors[:5]:  # Show max 5 errors
                print(Fore.RED + f"\t  - {error}")
            
            if len(result.errors) > 5:
                print(Fore.RED + f"\t  ... y {len(result.errors) - 5} errores más")
    
    print()


def display_error(message: str) -> None:
    """Display an error message.
    
    Args:
        message: Error message to display.
    """
    print(Fore.RED + f"\n\t✗ Error: {message}\n")
    logger.error(message)
