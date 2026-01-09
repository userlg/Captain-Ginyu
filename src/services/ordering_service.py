"""Ordering service for folder organization."""

from src.config import get_config
from src.logger import get_logger

logger = get_logger(__name__)


def extract_digits(number: int) -> list[int]:
    """Extract individual digits from a number.

    Args:
        number: Integer to extract digits from.

    Returns:
        List[int]: List of digits in order.

    Examples:
        >>> extract_digits(23)
        [2, 3]
        >>> extract_digits(456)
        [4, 5, 6]
    """
    digits = []
    while number != 0:
        digit = int(number % 10)
        digits.append(digit)
        number = int(number / 10)
    digits.reverse()
    return digits


def identify_starting_index(folders: list[str]) -> int:
    """Identify the starting index from folder names.

    Args:
        folders: List of folder names.

    Returns:
        int: Starting index found in folder names.

    Examples:
        >>> identify_starting_index(["folder_Subsetup1", "folder_Subsetup2"])
        1
        >>> identify_starting_index(["folder_Subsetup15", "folder_Subsetup16"])
        15
    """
    config = get_config()
    index = 1

    while index < config.max_index:
        for folder in folders:
            size = len(folder)

            if index < 10:
                # Single digit index
                if size >= 2 and folder[size - 1] == str(index) and folder[size - 2] == "p":
                    logger.debug(f"Found starting index: {index}")
                    return index
            elif index < 100:
                # Double digit index
                digits = extract_digits(index)
                if (
                    size >= 3
                    and folder[size - 2] == str(digits[0])
                    and folder[size - 1] == str(digits[1])
                    and folder[size - 3] == "p"
                ):
                    logger.debug(f"Found starting index: {index}")
                    return index

        index += 1

    logger.warning(f"Starting index not found, returning {index}")
    return index


def order_folders(folders: list[str]) -> list[str]:
    """Order folders according to custom logic.

    Puts Malocclusion folder first if present, then orders by Subsetup number.

    Args:
        folders: List of folder names to order.

    Returns:
        List[str]: Ordered list of folders.

    Examples:
        >>> order_folders(["Patient_Subsetup2", "Patient_Subsetup1"])
        ["Patient_Subsetup1", "Patient_Subsetup2"]
    """
    config = get_config()
    folders_ordered = []

    # Check for Malocclusion folder first
    malocclusion_keyword = config.malocclusion_keyword
    has_malocclusion = False

    for folder in folders:
        if malocclusion_keyword in folder:
            folders_ordered.append(folder)
            has_malocclusion = True
            logger.debug(f"Found Malocclusion folder: {folder}")
            break

    # Determine starting index
    index = 1 if has_malocclusion else identify_starting_index(folders)

    # Order remaining folders by Subsetup index
    subsetup_pattern = config.subsetup_pattern
    limit = len(folders)
    j = 1

    while j <= limit:
        for folder in folders:
            if folder.endswith(f"{subsetup_pattern}{index}"):
                index += 1
                folders_ordered.append(folder)
                logger.debug(f"Added folder: {folder}")
                break
        j += 1

    logger.info(f"Ordered {len(folders_ordered)} folders")
    return folders_ordered
