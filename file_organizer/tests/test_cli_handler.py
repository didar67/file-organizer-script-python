"""
Tests for CLI argument parsing in cli/cli_handler.py.
"""

import argparse
from cli.cli_handler import build_parser

def test_build_parser_returns_argparse_instance():
    """Ensure build_parser() returns an ArgumentParser object."""
    parser = build_parser()
    assert isinstance(parser, argparse.ArgumentParser)

def test_parser_accepts_valid_arguments(monkeypatch):
    """Test CLI parsing with sample arguments."""
    parser = build_parser()
    args = parser.parse_args([
        "--path", "/tmp/test",
        "--config", "config/config.yaml",
        "--dry-run",
        "--verbose",
        "--log-level", "DEBUG"
    ])
    assert args.path == "/tmp/test"
    assert args.config == "config/config.yaml"
    assert args.dry_run is True
    assert args.verbose is True
    assert args.log_level == "DEBUG"
