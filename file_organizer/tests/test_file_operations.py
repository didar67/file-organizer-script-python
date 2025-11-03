"""
Unit tests for the Organizer class in core/file_operations.py.
"""

import os
import shutil
import pytest
from core.file_operations import Organizer
from utils.helper import load_config

@pytest.fixture
def mock_folder(tmp_path):
    """Create a temporary folder with sample files."""
    folder = tmp_path / "sample_folder"
    folder.mkdir()
    (folder / "test1.txt").write_text("File 1 content")
    (folder / "test2.jpg").write_text("File 2 content")
    return folder

def test_organize_files_creates_folders_and_moves_files(mock_folder):
    """Test that files are correctly organized by extension."""
    config = {"paths": {"default_folder": str(mock_folder)}}
    organizer = Organizer(base_path=str(mock_folder), dry_run=False, config=config)

    organized_count = organizer.organize_files()
    assert organized_count == 2

    # Check target folders were created
    assert os.path.exists(mock_folder / "TXT Files")
    assert os.path.exists(mock_folder / "JPG Files")

def test_organize_files_handles_empty_folder(tmp_path):
    """Test behavior when folder is empty."""
    empty_folder = tmp_path / "empty_folder"
    empty_folder.mkdir()
    config = {"paths": {"default_folder": str(empty_folder)}}

    organizer = Organizer(base_path=str(empty_folder), dry_run=False, config=config)
    organized_count = organizer.organize_files()
    assert organized_count == 0

def test_organize_files_dry_run_does_not_move_files(mock_folder):
    """Test that dry-run mode does not move files."""
    config = {"paths": {"default_folder": str(mock_folder)}}
    organizer = Organizer(base_path=str(mock_folder), dry_run=True, config=config)

    organizer.organize_files()
    assert os.path.exists(mock_folder / "test1.txt")
    assert os.path.exists(mock_folder / "test2.jpg")
