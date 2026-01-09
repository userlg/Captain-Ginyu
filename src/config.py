"""Configuration management for Captain Ginyu Script."""

import os
from dataclasses import dataclass
from pathlib import Path
from typing import List

from src.exceptions import ConfigurationError


@dataclass
class Config:
    """Configuration for Captain Ginyu Script."""
    
    # File patterns
    maxillary_pattern: str = "Maxillary"
    mandibular_pattern: str = "Mandibular"
    file_extension: str = ".stl"
    backup_keyword: str = "backup"
    
    # Folder patterns
    subsetup_pattern: str = "Subsetup"
    malocclusion_keyword: str = "Malocclusion"
    
    # Processing limits
    max_index: int = 100
    
    # Logging
    log_level: str = "INFO"
    log_file: str = "captain_ginyu.log"
    log_max_bytes: int = 10_485_760  # 10 MB
    log_backup_count: int = 5
    
    @classmethod
    def from_env(cls) -> "Config":
        """Create configuration from environment variables.
        
        Returns:
            Config: Configuration instance with values from environment.
        """
        try:
            return cls(
                maxillary_pattern=os.getenv("MAXILLARY_PATTERN", "Maxillary"),
                mandibular_pattern=os.getenv("MANDIBULAR_PATTERN", "Mandibular"),
                file_extension=os.getenv("FILE_EXTENSION", ".stl"),
                backup_keyword=os.getenv("BACKUP_KEYWORD", "backup"),
                subsetup_pattern=os.getenv("SUBSETUP_PATTERN", "Subsetup"),
                malocclusion_keyword=os.getenv("MALOCCLUSION_KEYWORD", "Malocclusion"),
                max_index=int(os.getenv("MAX_INDEX", "100")),
                log_level=os.getenv("LOG_LEVEL", "INFO"),
                log_file=os.getenv("LOG_FILE", "captain_ginyu.log"),
                log_max_bytes=int(os.getenv("LOG_MAX_BYTES", "10485760")),
                log_backup_count=int(os.getenv("LOG_BACKUP_COUNT", "5")),
            )
        except (ValueError, TypeError) as e:
            raise ConfigurationError(f"Invalid configuration: {e}") from e
    
    def get_excluded_folders(self) -> List[str]:
        """Get list of folders to exclude from processing.
        
        Returns:
            List[str]: Folders to exclude (hidden folders starting with .)
        """
        return [".git", ".venv", ".pytest_cache", "__pycache__"]


# Global configuration instance
_config: Config = Config()


def get_config() -> Config:
    """Get the global configuration instance.
    
    Returns:
        Config: Global configuration instance.
    """
    return _config


def set_config(config: Config) -> None:
    """Set the global configuration instance.
    
    Args:
        config: New configuration instance.
    """
    global _config
    _config = config
