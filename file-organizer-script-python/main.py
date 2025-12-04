#!/usr/bin/env python3
"""
File Organizer – Final 2025 Production-Ready Version
Clean, typed, documented, and optimized file organization tool.
"""

from __future__ import annotations
from logging.handlers import RotatingFileHandler

import os
import logging
import shutil
from pathlib import Path
from typing import Dict

import click
import yaml
from dotenv import load_dotenv


# Load environment variables early
load_dotenv()


def setup_logging(level: str = "INFO", log_file: str = "logs/file_organizer.log") -> None:
    """Configure structured logging with console + rotating file output."""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(getattr(logging, level.upper()))
    logger.handlers.clear()  # prevent duplicate handlers in reloads

    # Rotating file handler – 5 MB per file, keep 5 backups
    file_handler = RotatingFileHandler(log_file, maxBytes=5_000_000, backupCount=5)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s | %(message)s"
    ))
    logger.addHandler(file_handler)

    # Clean console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(levelname)-8s | %(message)s"))
    logger.addHandler(console_handler)


def load_config(config_path: Path = Path("config.yaml")) -> Dict:
    """Load YAML config safely – returns empty dict if missing."""
    if not config_path.is_file():
        logging.warning(f"Config not found: {config_path} → using defaults")
        return {}
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def build_extension_map(config: Dict) -> Dict[str, str]:
    """Create lowercase extension → folder mapping from config groups."""
    mapping: Dict[str, str] = {}
    for folder, extensions in config.get("extension_groups", {}).items():
        for ext in extensions:
            mapping[ext.lower()] = folder
    return mapping


def organize_directory(target: Path, mapping: Dict[str, str], dry_run: bool = False) -> int:
    """Core logic – moves files to correct folders. Returns processed count."""
    target = target.expanduser().resolve()
    if not target.is_dir():
        raise NotADirectoryError(f"Target directory does not exist: {target}")

    moved = 0
    for file_path in target.iterdir():
        if not file_path.is_file():
            continue

        ext = file_path.suffix[1:].lower()
        dest_folder = mapping.get(ext, "Others")
        dest_dir = target / dest_folder
        dest_dir.mkdir(exist_ok=True)
        dest_path = dest_dir / file_path.name

        if file_path.parent != dest_dir:
            if dry_run:
                logging.info(f"[DRY-RUN] {file_path.name} → {dest_folder}/")
            else:
                if dest_path.exists():
                    logging.warning(f"Skipped (already exists): {file_path.name}")
                else:
                    shutil.move(str(file_path), str(dest_path))
                    logging.info(f"Moved: {file_path.name} → {dest_folder}/")
            moved += 1

    return moved


@click.command()
@click.option("-d", "--directory", default=".", help="Directory to organize")
@click.option("-c", "--config", default="config.yaml", help="Path to config file")
@click.option("--dry-run", is_flag=True, help="Preview changes without moving files")
@click.option("-v", "--verbose", is_flag=True, help="Enable detailed DEBUG output")
def main(directory: str, config: str, dry_run: bool, verbose: bool) -> None:
    """Production-ready CLI – clean, typed, and fully documented."""
    log_level = "DEBUG" if verbose else load_dotenv().get("LOG_LEVEL", "INFO")
    setup_logging(log_level)

    logging.info("File Organizer v2025 – starting")
    cfg = load_config(Path(config))
    mapping = build_extension_map(cfg)

    try:
        count = organize_directory(Path(directory), mapping, dry_run)
        mode = " (dry-run)" if dry_run else ""
        logging.info(f"Completed{mode} – {count} file(s) processed successfully")
    except Exception as exc:
        logging.error(f"Operation failed: {exc}")
        raise click.Abort() from exc


if __name__ == "__main__":
    main()