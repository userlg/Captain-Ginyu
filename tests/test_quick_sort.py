
from src import quick_sort as q

def test_quicksort_works_properly() -> None:
    numbers = [500, 45, 100, 1, 2, 3, -4, 120]
    assert q.quicksort(numbers, 0, len(numbers) - 1) == None
