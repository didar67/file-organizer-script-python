# File Organizer – 2025 Edition

A clean, production-ready Python tool that automatically organizes files by extension.

## Features
- Modern Click CLI with `--directory`, `--config`, `--dry-run`, `--verbose`
- Fully configurable via `config.yaml` – no code changes required
- Structured logging + `.env` support for log level override
- Safe dry-run mode for preview
- Complete type hints, docstrings, and 2025 Python best practices

## Quick Start
```bash
# Organize current folder
python main.py

# Preview changes with verbose output
python main.py --dry-run -v

# Organize Downloads folder
python main.py -d ~/Downloads