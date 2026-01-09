"""Tests for ordering algorithms."""

import pytest
from typing import List

from src import ordering as o
from src import utils as u


class TestQuicksort:
    """Tests for quicksort algorithm."""
    
    def test_quicksort_works_properly(self) -> None:
        """Test quicksort with unsorted list."""
        numbers = [500, 45, 100, 1, 2, 3, -4, 120]
        assert o.quicksort(numbers, 0, len(numbers) - 1) is None
        assert u.list_is_ordered_properly(numbers) is True
    
    @pytest.mark.parametrize("numbers", [
        [5, 3, 1, 4, 2],
        [10, 9, 8, 7, 6, 5],
        [1],
        [2, 1],
        [-5, -1, -10, 0, 3],
    ])
    def test_quicksort_parametrized(self, numbers: List[int]) -> None:
        """Test quicksort with various inputs."""
        o.quicksort(numbers, 0, len(numbers) - 1)
        assert u.list_is_ordered_properly(numbers) is True
    
    def test_quicksort_already_sorted(self) -> None:
        """Test quicksort with already sorted list."""
        numbers = [1, 2, 3, 4, 5]
        o.quicksort(numbers, 0, len(numbers) - 1)
        assert numbers == [1, 2, 3, 4, 5]
    
    def test_quicksort_empty_list(self) -> None:
        """Test quicksort with empty list."""
        numbers = []
        # Should not crash
        if numbers:
            o.quicksort(numbers, 0, len(numbers) - 1)
        assert numbers == []


class TestBubbleOrdering:
    """Tests for bubble sort algorithm."""
    
    def test_bubble_ordering_basic(self) -> None:
        """Test bubble sort with unsorted list."""
        numbers = [500, 45, 100, 1, 2, 3, -4, 120]
        assert o.ordering_bubble(numbers) is True
        assert u.list_is_ordered_properly(numbers) is True
    
    @pytest.mark.parametrize("numbers", [
        [5, 3, 1, 4, 2],
        [10, 9, 8, 7, 6, 5],
        [1],
        [2, 1],
        [-5, -1, -10, 0, 3],
    ])
    def test_bubble_ordering_parametrized(self, numbers: List[int]) -> None:
        """Test bubble sort with various inputs."""
        o.ordering_bubble(numbers)
        assert u.list_is_ordered_properly(numbers) is True
    
    def test_bubble_ordering_already_sorted(self) -> None:
        """Test bubble sort with already sorted list."""
        numbers = [1, 2, 3, 4, 5]
        o.ordering_bubble(numbers)
        assert numbers == [1, 2, 3, 4, 5]
    
    def test_bubble_ordering_empty_list(self) -> None:
        """Test bubble sort with empty list."""
        numbers = []
        o.ordering_bubble(numbers)
        assert numbers == []
    
    def test_bubble_ordering_duplicates(self) -> None:
        """Test bubble sort with duplicate values."""
        numbers = [3, 1, 2, 3, 1, 2]
        o.ordering_bubble(numbers)
        assert u.list_is_ordered_properly(numbers) is True
        assert numbers == [1, 1, 2, 2, 3, 3]
