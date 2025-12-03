#!/usr/bin/env python3
"""
File Organizer – 2025 Production-Ready Edition
Organizes files by extension using configurable groups with CLI, logging and dry-run support.
"""

import logging
import shutil
from pathlib import Path
from typing import Dict, List

import click
import yaml
from dotenv import load_dotenv


# Load environment variables (supports LOG_LEVEL override)
load_dotenv()


def setup_logging(level: str = "INFO") -> None:
    """Configure structured logging for consistent output."""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def load_config(path: Path = Path("config.yaml")) -> Dict:
    """Load YAML configuration with safe fallback."""
    if not path.exists():
        logging.warning(f"Config file {path} not found – using defaults")
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def get_extension_mapping(config: Dict) -> Dict[str, List[str]]:
    """Build extension → folder mapping from config."""
    groups = config.get("extension_groups", {})
    mapping = {}
    for folder, extensions in groups.items():
        for ext in extensions:
            mapping[ext.lower()] = folder
    return mapping


def organize_files(target_dir: Path, mapping: Dict[str, str], dry_run: bool = False) -> int:
    """Move files to corresponding folders. Returns number of moved files."""
    moved = 0
    target_dir = target_dir.expanduser().resolve()

    if not target_dir.is_dir():
        raise NotADirectoryError(f"Directory not found: {target_dir}")

    for item in target_dir.iterdir():
        if not item.is_file():
            continue

        ext = item.suffix[1:].lower()  # without dot
        dest_folder = mapping.get(ext, "Others")

        dest_dir = target_dir / dest_folder
        dest_dir.mkdir(exist_ok=True)

        dest_path = dest_dir / item.name

        if item.parent != dest_dir:
            if dry_run:
                logging.info(f"[DRY-RUN] Would move: {item.name} → {dest_folder}/")
            else:
                if dest_path.exists():
                    logging.warning(f"Skipped (exists): {item.name}")
                else:
                    shutil.move(str(item), str(dest_path))
                    logging.info(f"Moved: {item.name} → {dest_folder}/")
            moved += 1

    return moved


@click.command()
@click.option("--directory", "-d", default=".", help="Target directory (default: current)")
@click.option("--config", "-c", default="config.yaml", help="Path to config file")
@click.option("--dry-run", is_flag=True, help="Show what would be moved without doing it")
@click.option("--verbose", "-v", is_flag=True, help="Enable DEBUG logging")
def cli(directory: str, config: str, dry_run: bool, verbose: bool) -> None:
    """File Organizer CLI – production-ready entry point."""
    log_level = "DEBUG" if verbose else (load_dotenv().get("LOG_LEVEL", "INFO"))
    setup_logging(log_level)

    logging.info("File Organizer started")
    config_data = load_config(Path(config))
    target = Path(directory)
    mapping = get_extension_mapping(config_data)

    try:
        count = organize_files(target, mapping, dry_run)
        logging.info(f"Finished – {'(dry-run) ' if dry_run else ''}{count} file(s) processed")
    except Exception as e:
        logging.error(f"Failed: {e}")
        raise click.Abort()


if __name__ == "__main__":
    cli()