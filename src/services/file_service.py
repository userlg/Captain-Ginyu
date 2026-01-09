"""File service for file operations."""

import os
from pathlib import Path
from typing import List

from src.config import get_config
from src.exceptions import FileProcessingError, FolderNotFoundError
from src.logger import get_logger
from src.models import ProcessingResult
from src.services.ordering_service import identify_starting_index


logger = get_logger(__name__)


def get_folders(root_path: Path) -> List[str]:
    """Get list of folders in the specified directory.
    
    Args:
        root_path: Root directory to scan for folders.
    
    Returns:
        List[str]: List of folder names (excluding hidden folders).
    
    Raises:
        FolderNotFoundError: If root_path doesn't exist or is not a directory.
    
    Examples:
        >>> get_folders(Path("/some/path"))
        ["folder1", "folder2", "folder3"]
    """
    if not root_path.exists():
        raise FolderNotFoundError(f"Path does not exist: {root_path}")
    
    if not root_path.is_dir():
        raise FolderNotFoundError(f"Path is not a directory: {root_path}")
    
    config = get_config()
    excluded = config.get_excluded_folders()
    
    try:
        content = os.listdir(root_path)
        folders = [
            item for item in content
            if os.path.isdir(root_path / item)
            and not item.startswith(".")
            and item not in excluded
        ]
        
        logger.info(f"Found {len(folders)} folders in {root_path}")
        return folders
    
    except PermissionError as e:
        raise FolderNotFoundError(f"Permission denied accessing {root_path}") from e
    except OSError as e:
        raise FolderNotFoundError(f"Error reading directory {root_path}: {e}") from e


def process_files(folders: List[str], root_path: Path) -> ProcessingResult:
    """Process STL files in the given folders.
    
    Renames and moves Maxillary and Mandibular STL files to root directory
    with sequential numbering.
    
    Args:
        folders: List of folder names to process (should be pre-ordered).
        root_path: Root directory containing the folders.
    
    Returns:
        ProcessingResult: Result of the processing operation.
    
    Examples:
        >>> process_files(["Patient_Subsetup1"], Path("/path"))
        ProcessingResult(success=True, folders_processed=1, files_moved=2)
    """
    result = ProcessingResult(success=True)
    config = get_config()
    
    if not folders:
        logger.warning("No folders to process")
        result.success = False
        result.add_error("No folders provided for processing")
        return result
    
    # Determine starting index
    if config.malocclusion_keyword in folders[0]:
        index = 0
    else:
        index = identify_starting_index(folders)
    
    logger.info(f"Starting file processing with index {index}")
    
    for folder in folders:
        try:
            folder_path = root_path / folder
            
            if not folder_path.exists():
                error_msg = f"Folder not found: {folder}"
                logger.error(error_msg)
                result.add_error(error_msg)
                continue
            
            files = os.listdir(folder_path)
            folder_files_moved = 0
            
            for file in files:
                file_path = folder_path / file
                
                # Process Maxillary files
                if (file.endswith(config.file_extension)
                    and file.startswith(config.maxillary_pattern)
                    and config.backup_keyword not in file):
                    
                    new_name = f"{config.maxillary_pattern}{index}{config.file_extension}"
                    new_path = root_path / new_name
                    
                    try:
                        os.rename(file_path, new_path)
                        logger.debug(f"Moved {file} -> {new_name}")
                        folder_files_moved += 1
                    except OSError as e:
                        error_msg = f"Failed to move {file}: {e}"
                        logger.error(error_msg)
                        result.add_error(error_msg)
                
                # Process Mandibular files
                if (file.endswith(config.file_extension)
                    and file.startswith(config.mandibular_pattern)
                    and config.backup_keyword not in file):
                    
                    new_name = f"{config.mandibular_pattern}{index}{config.file_extension}"
                    new_path = root_path / new_name
                    
                    try:
                        os.rename(file_path, new_path)
                        logger.debug(f"Moved {file} -> {new_name}")
                        folder_files_moved += 1
                    except OSError as e:
                        error_msg = f"Failed to move {file}: {e}"
                        logger.error(error_msg)
                        result.add_error(error_msg)
            
            result.files_moved += folder_files_moved
            result.folders_processed += 1
            index += 1
            
        except Exception as e:
            error_msg = f"Unexpected error processing folder {folder}: {e}"
            logger.error(error_msg)
            result.add_error(error_msg)
    
    if result.errors:
        result.success = False
        logger.warning(f"Processing completed with {len(result.errors)} errors")
    else:
        logger.info(
            f"Successfully processed {result.folders_processed} folders, "
            f"moved {result.files_moved} files"
        )
    
    return result
