# File Organizer Project — Architecture

This document provides a high-level overview of the architecture and folder structure of the File Organizer project.

## Project Structure

```
file_organizer/
│
├── config/
│   └── config.yaml                 # Configuration file for default paths and logging
│
├── core/
│   ├── __init__.py
│   ├── logger.py                   # Logging setup module
│   └── file_operations.py          # Core logic for scanning, moving, and organizing files
│
├── cli/
│   ├── __init__.py
│   └── cli_handler.py              # CLI parser and runtime argument handling
│
├── utils/
│   ├── __init__.py
│   └── helper.py                   # Helper functions for loading config and validation
│
├── tests/
│   ├── __init__.py
│   ├── test_file_operations.py
│   ├── test_cli_handler.py
│   ├── test_logger.py
│   └── test_main.py                # Tests for main.py orchestration
│
├── docs/
│   ├── README.md
│   └── architecture.md             # This architecture overview file
│
├── main.py                         # Entry point for executing the organizer
└── requirements.txt                # Dependency list
```

## Architecture Overview

1. **CLI Layer (`cli/`)**

   * Handles parsing command-line arguments using `argparse`.
   * Supports flags like `--path`, `--config`, `--dry-run`, `--verbose`, and `--log-level`.
   * Passes runtime arguments to the Organizer.

2. **Core Layer (`core/`)**

   * `file_operations.py`: Handles scanning directories, categorizing files by extension, creating folders, and moving files.
   * `logger.py`: Provides consistent logging with rotating file support.

3. **Utilities (`utils/`)**

   * `helper.py`: Loads configuration from YAML, provides helper functions for validations, and other small utilities.

4. **Testing (`tests/`)**

   * Contains unit tests for CLI, core functionalities, logger, and main orchestration.
   * Ensures code correctness, type safety, and proper integration.

5. **Configuration (`config/`)**

   * `config.yaml` defines default paths, logging file location, and other customizable options.

6. **Documentation (`docs/`)**

   * `README.md`: Project overview and instructions.
   * `architecture.md`: High-level design and file structure.

7. **Entry Point (`main.py`)**

   * Integrates CLI, core, utils, and logging.
   * Initializes and runs the Organizer based on configuration and CLI arguments.

## Notes

* Each module follows professional industry standards with type hints, docstrings, and structured logging.
* The project is modular to support future enhancements or additional CLI commands, logging options, or file operations.
* Unit tests ensure maintainability and reliability of the automation process.
