"""
Integration tests for the File Organizer's main entry point (main.py).

These tests verify:
- CLI integration works end-to-end
- Main function executes without runtime errors
- Organizer and config loading integrate correctly

Author: Didarul Islam
Date: 2025-11-03
"""

import pytest
import sys
from unittest.mock import patch, MagicMock
import main


@pytest.fixture
def mock_args(tmp_path):
    """Simulate CLI arguments for testing."""
    test_dir = tmp_path / "test_files"
    test_dir.mkdir()
    (test_dir / "sample.txt").write_text("sample content")

    args = [
        "main.py",
        "--path", str(test_dir),
        "--config", "config/config.yaml",
        "--dry-run",
        "--log-level", "INFO"
    ]
    return args


@patch("main.parse_arguments")
@patch("main.load_config", return_value={"paths": {"default_folder": "test_path"}})
@patch("main.setup_logger")
@patch("main.Organizer")
def test_main_runs_successfully(mock_organizer, mock_logger, mock_config, mock_parse_args, mock_args):
    """Ensure main() runs successfully and calls Organizer.run()."""
    mock_args_obj = MagicMock()
    mock_args_obj.path = "test_path"
    mock_args_obj.config = "config/config.yaml"
    mock_args_obj.dry_run = True
    mock_args_obj.verbose = False
    mock_args_obj.log_level = "INFO"

    mock_parse_args.return_value = mock_args_obj
    instance = MagicMock()
    mock_organizer.return_value = instance

    main.main()

    # Assertions: ensure methods are called
    mock_parse_args.assert_called_once()
    mock_config.assert_called_once_with("config/config.yaml")
    mock_logger.assert_called_once()
    mock_organizer.assert_called_once_with(
        base_path="test_path",
        dry_run=True,
        config={"paths": {"default_folder": "test_path"}}
    )
    instance.run.assert_called_once()


def test_main_cli_execution(monkeypatch, mock_args):
    """
    Simulate running main.py directly through CLI argument patching.
    Ensures no crash occurs when calling main.main().
    """
    with patch.object(sys, "argv", mock_args):
        with patch("main.load_config", return_value={"paths": {"default_folder": "test_path"}}):
            with patch("main.setup_logger"):
                with patch("main.Organizer") as mock_org:
                    instance = mock_org.return_value
                    main.main()
                    instance.run.assert_called_once()
