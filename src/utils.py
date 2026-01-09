"""Utility functions for Captain Ginyu Script.

This module contains pure utility functions that don't fit into
specific service layers.
"""

from typing import List


def list_is_ordered_properly(items: List) -> bool:
    """Check if a list is properly ordered (ascending).
    
    Args:
        items: List to check ordering.
    
    Returns:
        bool: True if list is ordered, False otherwise.
    
    Examples:
        >>> list_is_ordered_properly([1, 2, 3, 4])
        True
        >>> list_is_ordered_properly([1, 3, 2])
        False
    """
    for i in range(1, len(items)):
        if items[i] < items[i - 1]:
            return False
    return True


def extract_digits(number: int) -> List[int]:
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


# Legacy compatibility layer - importing from new locations
from src.services.file_service import get_folders, process_files
from src.services.ordering_service import (
    identify_starting_index as identify_index,
    order_folders,
)
from src.ui.console import (
    display_countdown as temporizer,
    display_folders as show_folders,
    display_welcome as phrases,
    get_random_emoji as get_emojis,
)

# For backward compatibility, create wrapper for order_customizer
def order_customizer(folders: List[str], limit: int) -> List[str]:
    """Legacy wrapper for order_folders.
    
    Args:
        folders: List of folder names.
        limit: Ignored for backward compatibility.
    
    Returns:
        List[str]: Ordered folders.
    """
    return order_folders(folders)

# For backward compatibility, create wrapper for procesing_files
def procesing_files(folders: List[str]) -> bool:
    """Legacy wrapper for process_files.
    
    Args:
        folders: List of folder names.
    
    Returns:
        bool: True if processing succeeded, False otherwise.
    """
    import os
    from pathlib import Path
    
    if not folders:
        return False
    
    root = Path(os.getcwd())
    result = process_files(folders, root)
    return result.success


__all__ = [
    "list_is_ordered_properly",
    "extract_digits",
    "get_folders",
    "process_files",
    "identify_index",
    "order_customizer",
    "temporizer",
    "show_folders",
    "phrases",
    "get_emojis",
    "procesing_files",
]
