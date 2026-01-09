"""Sorting algorithms for Captain Ginyu Script.

This module provides various sorting algorithms for ordering folders.
"""

from typing import TypeVar

T = TypeVar("T")


def ordering_bubble(items: list[T]) -> bool:
    """Sort a list using bubble sort algorithm (in-place).

    Args:
        items: List to sort.

    Returns:
        bool: Always returns True for backward compatibility.

    Examples:
        >>> items = [3, 1, 2]
        >>> ordering_bubble(items)
        True
        >>> items
        [1, 2, 3]
    """
    limit = len(items)
    for i in range(limit - 1):
        for j in range(limit - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return True


def quicksort(items: list[T], left: int, right: int) -> None:
    """Sort a list using quicksort algorithm (in-place).

    Args:
        items: List to sort.
        left: Left boundary index.
        right: Right boundary index.

    Examples:
        >>> items = [500, 45, 100, 1]
        >>> quicksort(items, 0, len(items) - 1)
        >>> items
        [1, 45, 100, 500]
    """
    if left < right:
        partition_index = partition(items, left, right)
        quicksort(items, left, partition_index)
        quicksort(items, partition_index + 1, right)


def partition(items: list[T], left: int, right: int) -> int:
    """Partition function for quicksort algorithm.

    Args:
        items: List to partition.
        left: Left boundary index.
        right: Right boundary index.

    Returns:
        int: Partition index.
    """
    pivot = items[left]

    while True:
        while items[left] < pivot:
            left += 1

        while items[right] > pivot:
            right -= 1

        if left >= right:
            return right
        else:
            items[left], items[right] = items[right], items[left]
            left += 1
            right -= 1


__all__ = ["ordering_bubble", "quicksort", "partition"]
