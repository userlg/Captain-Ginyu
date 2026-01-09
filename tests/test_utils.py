"""Tests for utils module - backward compatibility layer."""

import os
from pathlib import Path
from typing import List

import pytest

from src import utils as u


class TestListIsOrderedProperly:
    """Tests for list_is_ordered_properly function."""
    
    def test_is_ordered_with_ordered_values(self) -> None:
        """Test with properly ordered list."""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert u.list_is_ordered_properly(numbers) is True
    
    def test_is_ordered_with_unordered_values(self) -> None:
        """Test with unordered list."""
        numbers = [23, -2, 3, 4, 5, 6, 7, 89]
        assert u.list_is_ordered_properly(numbers) is False
    
    @pytest.mark.parametrize("items,expected", [
        ([1, 2, 3], True),
        ([3, 2, 1], False),
        ([1], True),
        ([], True),
        ([1, 1, 1], True),
        ([1, 2, 2, 3], True),
    ])
    def test_is_ordered_parametrized(self, items: List, expected: bool) -> None:
        """Test ordering check with various inputs."""
        assert u.list_is_ordered_properly(items) == expected


class TestExtractDigits:
    """Tests for extract_digits function."""
    
    def test_extract_digits_works_properly(self) -> None:
        """Test basic digit extraction."""
        assert u.extract_digits(23) == [2, 3]
    
    @pytest.mark.parametrize("number,expected", [
        (1, [1]),
        (99, [9, 9]),
        (123, [1, 2, 3]),
        (456, [4, 5, 6]),
    ])
    def test_extract_digits_parametrized(self, number: int, expected: List[int]) -> None:
        """Test digit extraction with various numbers."""
        assert u.extract_digits(number) == expected


class TestGetFolders:
    """Tests for get_folders function (backward compatibility)."""
    
    def test_get_folders_is_type_list(self, temp_root: Path) -> None:
        """Test that get_folders returns a list."""
        original_cwd = Path(os.getcwd())
        os.chdir(temp_root)
        
        try:
            folders = u.get_folders(temp_root)
            assert isinstance(folders, list)
        finally:
            os.chdir(original_cwd)
    
    def test_get_folders_with_sample_data(
        self, temp_root: Path, sample_folders: List[str]
    ) -> None:
        """Test get_folders with sample data."""
        folders = u.get_folders(temp_root)
        assert len(folders) == 3


class TestShowFolders:
    """Tests for show_folders function."""
    
    def test_show_folders_with_list_of_elements(self, capsys) -> None:
        """Test showing folders with elements."""
        folders = ["f1", "f2", "f3"]
        u.show_folders(folders)
        captured = capsys.readouterr()
        
        assert "3" in captured.out
    
    def test_show_folders_with_empty_list(self, capsys) -> None:
        """Test showing empty folder list."""
        folders = []
        u.show_folders(folders)  
        captured = capsys.readouterr()
        
        assert "No se detectaron" in captured.out


class TestTemporizer:
    """Tests for temporizer function."""
    
    def test_temporizer_completes(self) -> None:
        """Test temporizer countdown completes without crashing."""
        # Just test it doesn't crash - avoid strict timing assertions
        # as they're unreliable in CI environments
        import time
        start = time.time()
        u.temporizer(1)
        elapsed = time.time() - start
        
        # Should take at least 1 second, at most 3 (with system overhead)
        assert 0.9 < elapsed < 3.0


class TestPhrases:
    """Tests for phrases function."""
    
    def test_phrases_works_properly(self, capsys) -> None:
        """Test that phrases function returns True and prints."""
        result = u.phrases()
        assert result is True
        
        captured = capsys.readouterr()
        assert len(captured.out) > 0


class TestGetEmojis:
    """Tests for get_emojis function."""
    
    def test_get_emojis_works_properly(self) -> None:
        """Test that get_emojis returns a string."""
        assert isinstance(u.get_emojis(), str)


class TestOrderCustomizer:
    """Tests for order_customizer function (backward compatibility)."""
    
    def test_order_customizer_with_malocclusion(self) -> None:
        """Test ordering with Malocclusion folder."""
        folders = [
            "Francini Jimenez Alpizar_Subsetup3",
            "Francini Jimenez Alpizar_Subsetup1",
            "Francini Jimenez Alpizar_Malocclusion",
            "Francini Jimenez Alpizar_Subsetup2",
        ]
        
        response = u.order_customizer(folders, len(folders) - 1)
        assert len(response) == 4
        assert u.list_is_ordered_properly(response) is True
        assert "Malocclusion" in response[0]
    
    def test_order_customizer_without_malocclusion(self) -> None:
        """Test ordering without Malocclusion folder."""
        folders = [
            "Francini Jimenez Alpizar_Subsetup3",
            "Francini Jimenez Alpizar_Subsetup2",
            "Francini Jimenez Alpizar_Subsetup1",
        ]
        
        response = u.order_customizer(folders, len(folders))
        assert len(response) == 3
        assert u.list_is_ordered_properly(response) is True


class TestIdentifyIndex:
    """Tests for identify_index function."""
    
    def test_identify_index_less_than_nine(self) -> None:
        """Test identifying index less than 9."""
        directories = [
            "Francini Jimenez Alpizar_Subsetup1",
            "Francini Jimenez Alpizar_Subsetup2",
            "Francini Jimenez Alpizar_Subsetup3",
        ]
        assert u.identify_index(directories) == 1
    
    def test_identify_index_greater_than_nine(self) -> None:
        """Test identifying index greater than 9."""
        directories = [
            "Francini Jimenez Alpizar_Subsetup15",
            "Francini Jimenez Alpizar_Subsetup16",
            "Francini Jimenez Alpizar_Subsetup17",
        ]
        assert u.identify_index(directories) == 15
    
    def test_identify_index_not_found(self) -> None:
        """Test when index is not found returns 100."""
        directories = [
            "Francini Jimenez Alpizar_Subsetup100",
        ]
        assert u.identify_index(directories) == 100


class TestProcesingFiles:
    """Tests for procesing_files function."""
    
    def test_procesing_files_with_zero_directories(self) -> None:
        """Test processing with no directories."""
        folders = []
        assert u.procesing_files(folders) is False
    
    def test_procesing_files_with_valid_structure(
        self, temp_root: Path, sample_folders: List[str], sample_stl_files: None
    ) -> None:
        """Test file processing with valid structure."""
        original_cwd = Path(os.getcwd())
        os.chdir(temp_root)
        
        try:
            result = u.procesing_files(sample_folders)
            assert result is True
            
            # Verify files were created
            assert (temp_root / "Maxillary1.stl").exists()
            assert (temp_root / "Mandibular1.stl").exists()
        finally:
            os.chdir(original_cwd)
