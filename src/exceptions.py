"""Custom exceptions for Captain Ginyu Script."""


class CaptainGinyuError(Exception):
    """Base exception for Captain Ginyu Script."""

    pass


class FolderNotFoundError(CaptainGinyuError):
    """Raised when required folders are not found."""

    pass


class InvalidFolderStructureError(CaptainGinyuError):
    """Raised when folder structure doesn't match expected pattern."""

    pass


class FileProcessingError(CaptainGinyuError):
    """Raised when file processing fails."""

    pass


class ConfigurationError(CaptainGinyuError):
    """Raised when configuration is invalid."""

    pass
