"""Tests for console UI."""

from io import StringIO
from typing import List
from unittest.mock import patch

import pytest

from src.models import ProcessingResult
from src.ui.console import (
    display_countdown,
    display_error,
    display_folders,
    display_result,
    display_welcome,
    get_random_emoji,
)


class TestGetRandomEmoji:
    """Tests for get_random_emoji function."""
    
    def test_get_random_emoji_returns_string(self) -> None:
        """Test that get_random_emoji returns a string."""
        emoji = get_random_emoji()
        assert isinstance(emoji, str)
    
    def test_get_random_emoji_not_empty(self) -> None:
        """Test that emoji is not empty."""
        emoji = get_random_emoji()
        assert len(emoji) > 0


class TestDisplayWelcome:
    """Tests for display_welcome function."""
    
    def test_display_welcome_prints_output(self, capsys) -> None:
        """Test that welcome message is printed."""
        display_welcome()
        captured = capsys.readouterr()
        
        assert "Capitán Ginyu" in captured.out or "Captain Ginyu" in captured.out
        assert "Bienvenido" in captured.out


class TestDisplayFolders:
    """Tests for display_folders function."""
    
    def test_display_folders_with_items(self, capsys) -> None:
        """Test displaying folders with items."""
        folders = ["folder1", "folder2", "folder3"]
        display_folders(folders)
        captured = capsys.readouterr()
        
        assert "folder1" in captured.out
        assert "folder2" in captured.out
        assert "folder3" in captured.out
        assert "3" in captured.out
    
    def test_display_folders_empty_list(self, capsys) -> None:
        """Test displaying empty folder list."""
        display_folders([])
        captured = capsys.readouterr()
        
        assert "No se detectaron" in captured.out


class TestDisplayResult:
    """Tests for display_result function."""
    
    def test_display_result_success(self, capsys) -> None:
        """Test displaying successful result."""
        result = ProcessingResult(
            success=True,
            folders_processed=5,
            files_moved=10
        )
        display_result(result)
        captured = capsys.readouterr()
        
        assert "5" in captured.out
        assert "10" in captured.out
    
    def test_display_result_with_errors(self, capsys) -> None:
        """Test displaying result with errors."""
        result = ProcessingResult(success=False)
        result.add_error("Test error 1")
        result.add_error("Test error 2")
        
        display_result(result)
        captured = capsys.readouterr()
        
        assert "Test error 1" in captured.out
        assert "Test error 2" in captured.out


class TestDisplayError:
    """Tests for display_error function."""
    
    def test_display_error_prints_message(self, capsys) -> None:
        """Test that error message is printed."""
        display_error("Test error message")
        captured = capsys.readouterr()
        
        assert "Test error message" in captured.out
        assert "Error" in captured.out


class TestDisplayCountdown:
    """Tests for display_countdown function."""
    
    @patch('time.sleep')
    def test_display_countdown_calls_sleep(self, mock_sleep, capsys) -> None:
        """Test that countdown calls sleep."""
        display_countdown(2)
        
        # Should call sleep 2 times for countdown + 1 time at end
        assert mock_sleep.call_count == 3
