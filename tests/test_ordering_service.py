"""Tests for ordering service."""

from typing import List

import pytest

from src.services.ordering_service import (
    extract_digits,
    identify_starting_index,
    order_folders,
)


class TestExtractDigits:
    """Tests for extract_digits function."""
    
    @pytest.mark.parametrize("number,expected", [
        (23, [2, 3]),
        (456, [4, 5, 6]),
        (1, [1]),
        (99, [9, 9]),
        (100, [1, 0, 0]),
    ])
    def test_extract_digits_various_numbers(self, number: int, expected: List[int]) -> None:
        """Test digit extraction for various numbers."""
        assert extract_digits(number) == expected


class TestIdentifyStartingIndex:
    """Tests for identify_starting_index function."""
    
    def test_identify_index_single_digit(self) -> None:
        """Test identifying single digit index."""
        folders = [
            "Patient_Name_Subsetup1",
            "Patient_Name_Subsetup2",
            "Patient_Name_Subsetup3",
        ]
        assert identify_starting_index(folders) == 1
    
    def test_identify_index_double_digit(self) -> None:
        """Test identifying double digit index."""
        folders = [
            "Patient_Name_Subsetup15",
            "Patient_Name_Subsetup16",
            "Patient_Name_Subsetup17",
        ]
        assert identify_starting_index(folders) == 15
    
    def test_identify_index_starting_from_5(self) -> None:
        """Test identifying index starting from 5."""
        folders = [
            "Patient_Name_Subsetup5",
            "Patient_Name_Subsetup6",
        ]
        assert identify_starting_index(folders) == 5
    
    @pytest.mark.parametrize("folders,expected_index", [
        (["Test_Subsetup1"], 1),
        (["Test_Subsetup10"], 10),
        (["Test_Subsetup25"], 25),
        (["Test_Subsetup99"], 99),
    ])
    def test_identify_index_parametrized(
        self, folders: List[str], expected_index: int
    ) -> None:
        """Test index identification with various starting points."""
        assert identify_starting_index(folders) == expected_index


class TestOrderFolders:
    """Tests for order_folders function."""
    
    def test_order_folders_without_malocclusion(self) -> None:
        """Test ordering folders without Malocclusion."""
        folders = [
            "Patient_Subsetup3",
            "Patient_Subsetup1",
            "Patient_Subsetup2",
        ]
        ordered = order_folders(folders)
        
        assert len(ordered) == 3
        assert ordered[0].endswith("Subsetup1")
        assert ordered[1].endswith("Subsetup2")
        assert ordered[2].endswith("Subsetup3")
    
    def test_order_folders_with_malocclusion(self) -> None:
        """Test ordering folders with Malocclusion first."""
        folders = [
            "Patient_Subsetup2",
            "Patient_Malocclusion",
            "Patient_Subsetup1",
        ]
        ordered = order_folders(folders)
        
        assert len(ordered) == 3
        assert "Malocclusion" in ordered[0]
        assert ordered[1].endswith("Subsetup1")
        assert ordered[2].endswith("Subsetup2")
    
    def test_order_folders_double_digit_indices(self) -> None:
        """Test ordering folders with double digit indices."""
        folders = [
            "Patient_Subsetup12",
            "Patient_Subsetup10",
            "Patient_Subsetup11",
        ]
        ordered = order_folders(folders)
        
        assert len(ordered) == 3
        assert ordered[0].endswith("Subsetup10")
        assert ordered[1].endswith("Subsetup11")
        assert ordered[2].endswith("Subsetup12")
    
    def test_order_folders_empty_list(self) -> None:
        """Test ordering empty list."""
        folders = []
        ordered = order_folders(folders)
        
        assert ordered == []
    
    def test_order_folders_single_folder(self) -> None:
        """Test ordering single folder."""
        folders = ["Patient_Subsetup1"]
        ordered = order_folders(folders)
        
        assert len(ordered) == 1
        assert ordered[0] == "Patient_Subsetup1"
    
    def test_order_folders_maintains_all_folders(self) -> None:
        """Test that all folders are included in result."""
        folders = [
            "Francini Jimenez_Subsetup3",
            "Francini Jimenez_Subsetup1",
            "Francini Jimenez_Malocclusion",
            "Francini Jimenez_Subsetup2",
        ]
        ordered = order_folders(folders)
        
        assert len(ordered) == 4
        # Check all folders are present
        assert all(folder in ordered for folder in folders)
