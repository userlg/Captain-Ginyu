from src import ordering as o

from src import utils as u


def test_quicksort_works_properly() -> None:
    numbers = [500, 45, 100, 1, 2, 3, -4, 120]
    assert o.quicksort(numbers, 0, len(numbers) - 1) == None
    assert u.list_is_ordered_properly(numbers) == True


def test_bubble_ordering() -> None:
    numbers = [500, 45, 100, 1, 2, 3, -4, 120]
    assert o.ordering_bubble(numbers) == True
    assert u.list_is_ordered_properly(numbers) == True
