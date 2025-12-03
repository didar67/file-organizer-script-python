"""
Entry point for the File Organizer project.

This script integrates all modules:
- Core Organizer class for file operations
- CLI handler for user input
- Configuration and logging setup

It ensures professional, recruiter-friendly code with docstrings,
inline comments, and proper logging.
"""

import logging
from cli.cli_handler import parse_arguments
from core.file_operations import Organizer
from core.logger import setup_logger
from utils.helper import load_config

def main():
    """
    Main function to orchestrate the File Organizer execution.

    Steps:
    1. Parse CLI arguments
    2. Load configuration from YAML
    3. Setup logging based on CLI args and config
    4. Initialize Organizer and run file operations
    """
    
    # Parse CLI arguments
    args = parse_arguments()

    # Load configuration
    config_path = args.config
    config = load_config(config_path)

    # Setup Logger
    log_level = getattr(logging, args.log_level.upper(), logging.INFO)
    log_file = config.get("logging", {}).get("log_file", "file_organizer.log")
    setup_logger(log_level=log_level, verbose=args.verbose, log_file=log_file)

    # Initialize Organizer and run operations
    organizer = Organizer(
        base_path=args.path or config.get("paths", {}).get("default_folder"),
        dry_run=args.dry_run,
        config=config
    )

    organizer.run()

if __name__ == "__main__":
    main()
