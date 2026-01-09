"""Captain Ginyu Script - Main application entry point.

Organizes STL files from multiple folders into a structured format.
"""

import os
import sys
import time
from pathlib import Path

from src.config import Config, set_config
from src.exceptions import CaptainGinyuError
from src.logger import setup_logger
from src.services.file_service import get_folders, process_files
from src.services.ordering_service import order_folders
from src.ui.console import (
    display_countdown,
    display_error,
    display_folders,
    display_result,
    display_welcome,
)


def main() -> int:
    """Main application entry point.

    Returns:
        int: Exit code (0 for success, 1 for error).
    """
    # Initialize configuration and logging
    try:
        config = Config.from_env()
        set_config(config)
        logger = setup_logger()
        logger.info("=" * 50)
        logger.info("Captain Ginyu Script started")
        logger.info("=" * 50)
    except Exception as e:
        print(f"Failed to initialize application: {e}")
        return 1

    try:
        # Display welcome message
        display_welcome()
        time.sleep(2)

        # Get current working directory
        root_path = Path(os.getcwd())
        logger.info(f"Working directory: {root_path}")

        # Get folders from current directory
        folders = get_folders(root_path)

        if not folders:
            display_error("No se encontraron directorios para procesar")
            logger.warning("No folders found to process")
            display_countdown(2)
            return 0

        # Order folders according to custom logic
        ordered_folders = order_folders(folders)
        logger.info(f"Ordered {len(ordered_folders)} folders")

        # Display folders to be processed
        display_folders(ordered_folders)

        # Process files
        result = process_files(ordered_folders, root_path)

        # Display result
        display_result(result)

        # Countdown before exit
        display_countdown(2)

        logger.info("Captain Ginyu Script completed successfully")
        return 0 if result.success else 1

    except CaptainGinyuError as e:
        display_error(str(e))
        logger.error(f"Application error: {e}", exc_info=True)
        display_countdown(2)
        return 1

    except KeyboardInterrupt:
        display_error("Operación cancelada por el usuario")
        logger.info("Application interrupted by user")
        return 1

    except Exception as e:
        display_error(f"Error inesperado: {e}")
        logger.critical(f"Unexpected error: {e}", exc_info=True)
        display_countdown(2)
        return 1


if __name__ == "__main__":
    sys.exit(main())
