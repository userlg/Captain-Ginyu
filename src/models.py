"""Data models for Captain Ginyu Script."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class FolderInfo:
    """Information about a folder to be processed."""

    name: str
    path: Path
    is_malocclusion: bool = False
    index: int | None = None

    def __post_init__(self) -> None:
        """Determine if folder is malocclusion type."""
        self.is_malocclusion = "Malocclusion" in self.name


@dataclass
class FileInfo:
    """Information about an STL file."""

    name: str
    path: Path
    is_maxillary: bool = False
    is_mandibular: bool = False

    def __post_init__(self) -> None:
        """Determine file type from name."""
        self.is_maxillary = "Maxillary" in self.name
        self.is_mandibular = "Mandibular" in self.name


@dataclass
class ProcessingResult:
    """Result of file processing operation."""

    success: bool
    folders_processed: int = 0
    files_moved: int = 0
    errors: list[str] = field(default_factory=list)

    def add_error(self, error: str) -> None:
        """Add an error message to the result."""
        self.errors.append(error)
        self.success = False
