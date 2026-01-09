"""Pytest configuration and shared fixtures."""

import os
from pathlib import Path
from typing import Generator, List

import pytest

from src.config import Config, set_config


@pytest.fixture
def temp_root(tmp_path: Path) -> Path:
    """Provide a temporary root directory for tests.
    
    Args:
        tmp_path: pytest's temporary directory fixture.
    
    Returns:
        Path: Temporary root directory.
    """
    return tmp_path


@pytest.fixture
def sample_folders(temp_root: Path) -> List[str]:
    """Create sample folder structure for testing.
    
    Args:
        temp_root: Temporary root directory.
    
    Returns:
        List[str]: List of created folder names.
    """
    folder_names = [
        "Patient_Name_Date_Subsetup1",
        "Patient_Name_Date_Subsetup2",
        "Patient_Name_Date_Subsetup3",
    ]
    
    for folder_name in folder_names:
        folder_path = temp_root / folder_name
        folder_path.mkdir()
    
    return folder_names


@pytest.fixture
def sample_folders_with_malocclusion(temp_root: Path) -> List[str]:
    """Create sample folder structure with Malocclusion for testing.
    
    Args:
        temp_root: Temporary root directory.
    
    Returns:
        List[str]: List of created folder names.
    """
    folder_names = [
        "Patient_Name_Date_Malocclusion",
        "Patient_Name_Date_Subsetup1",
        "Patient_Name_Date_Subsetup2",
    ]
    
    for folder_name in folder_names:
        folder_path = temp_root / folder_name
        folder_path.mkdir()
    
    return folder_names


@pytest.fixture
def sample_stl_files(temp_root: Path, sample_folders: List[str]) -> None:
    """Create sample STL files in folders.
    
    Args:
        temp_root: Temporary root directory.
        sample_folders: List of folder names.
    """
    for folder_name in sample_folders:
        folder_path = temp_root / folder_name
        
        # Create Maxillary file
        maxillary_file = folder_path / "Maxillary_test.stl"
        maxillary_file.write_text("STL content")
        
        # Create Mandibular file
        mandibular_file = folder_path / "Mandibular_test.stl"
        mandibular_file.write_text("STL content")


@pytest.fixture
def test_config() -> Generator[Config, None, None]:
    """Provide a test configuration.
    
    Yields:
        Config: Test configuration instance.
    """
    original_config = Config()
    test_cfg = Config(
        log_level="DEBUG",
        log_file="test_captain_ginyu.log"
    )
    set_config(test_cfg)
    
    yield test_cfg
    
    # Restore original config
    set_config(original_config)
    
    # Clean up log file if exists
    if os.path.exists(test_cfg.log_file):
        try:
            os.remove(test_cfg.log_file)
        except OSError:
            pass
