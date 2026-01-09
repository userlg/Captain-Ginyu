"""Tests for file service."""

from pathlib import Path

import pytest

from src.exceptions import FolderNotFoundError
from src.services.file_service import get_folders, process_files


class TestGetFolders:
    """Tests for get_folders function."""

    def test_get_folders_returns_list(self, temp_root: Path, sample_folders: list[str]) -> None:
        """Test that get_folders returns a list."""
        folders = get_folders(temp_root)
        assert isinstance(folders, list)

    def test_get_folders_finds_all_folders(
        self, temp_root: Path, sample_folders: list[str]
    ) -> None:
        """Test that get_folders finds all created folders."""
        folders = get_folders(temp_root)
        assert len(folders) == len(sample_folders)
        assert set(folders) == set(sample_folders)

    def test_get_folders_excludes_hidden_folders(self, temp_root: Path) -> None:
        """Test that hidden folders are excluded."""
        (temp_root / ".hidden").mkdir()
        (temp_root / "visible").mkdir()

        folders = get_folders(temp_root)
        assert ".hidden" not in folders
        assert "visible" in folders

    def test_get_folders_raises_on_nonexistent_path(self) -> None:
        """Test that FolderNotFoundError is raised for non-existent path."""
        with pytest.raises(FolderNotFoundError):
            get_folders(Path("/nonexistent/path"))

    def test_get_folders_raises_on_file_path(self, temp_root: Path) -> None:
        """Test that FolderNotFoundError is raised when path is a file."""
        file_path = temp_root / "test.txt"
        file_path.write_text("test")

        with pytest.raises(FolderNotFoundError):
            get_folders(file_path)


class TestProcessFiles:
    """Tests for process_files function."""

    def test_process_files_with_empty_list(self, temp_root: Path) -> None:
        """Test processing with empty folder list."""
        result = process_files([], temp_root)
        assert result.success is False
        assert result.folders_processed == 0
        assert result.files_moved == 0
        assert len(result.errors) > 0

    def test_process_files_moves_maxillary_files(
        self, temp_root: Path, sample_folders: list[str], sample_stl_files: None
    ) -> None:
        """Test that Maxillary files are moved and renamed correctly."""
        # Change to temp directory for processing
        import os

        original_cwd = Path(os.getcwd())
        os.chdir(temp_root)

        try:
            result = process_files(sample_folders, temp_root)

            assert result.success is True
            assert result.folders_processed == 3

            # Check that files were created with correct names
            assert (temp_root / "Maxillary1.stl").exists()
            assert (temp_root / "Maxillary2.stl").exists()
            assert (temp_root / "Maxillary3.stl").exists()
        finally:
            os.chdir(original_cwd)

    def test_process_files_moves_mandibular_files(
        self, temp_root: Path, sample_folders: list[str], sample_stl_files: None
    ) -> None:
        """Test that Mandibular files are moved and renamed correctly."""
        import os

        original_cwd = Path(os.getcwd())
        os.chdir(temp_root)

        try:
            result = process_files(sample_folders, temp_root)

            assert result.success is True

            # Check that files were created with correct names
            assert (temp_root / "Mandibular1.stl").exists()
            assert (temp_root / "Mandibular2.stl").exists()
            assert (temp_root / "Mandibular3.stl").exists()
        finally:
            os.chdir(original_cwd)

    def test_process_files_handles_missing_folder(self, temp_root: Path) -> None:
        """Test that missing folders are handled gracefully."""
        result = process_files(["NonexistentFolder"], temp_root)

        assert result.success is False
        assert len(result.errors) > 0
        assert "not found" in result.errors[0].lower()

    def test_process_files_counts_files_correctly(
        self, temp_root: Path, sample_folders: list[str], sample_stl_files: None
    ) -> None:
        """Test that file count is correct."""
        import os

        original_cwd = Path(os.getcwd())
        os.chdir(temp_root)

        try:
            result = process_files(sample_folders, temp_root)

            # 3 folders * 2 files each (Maxillary + Mandibular)
            assert result.files_moved == 6
        finally:
            os.chdir(original_cwd)
