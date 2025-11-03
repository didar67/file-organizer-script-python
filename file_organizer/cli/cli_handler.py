"""
This module defines the Command-Line Interface (CLI) for the File Organizer project.

It uses argparse to handle user input, parse commands, and pass runtime arguments to
the main Organizer class. The CLI supports configuration files, logging control,
and various operational flags for flexible automation.

"""

import argparse
import logging

def build_parser() -> argparse.ArgumentParser:
    """
    Build and configure the argument parser for the CLI interface.

    Returns:
        argparse.ArgumentParser: Configured parser with all command-line options.
    """
    description = (
        "File Organizer CLI — Automate and organize files using configuration and logging."
    )
    epilog = (
        "Example usage:\n"
        "  python main.py --path /path/to/organize --config config/config.yaml --verbose\n"
        "  python main.py --dry-run --log-level DEBUG\n\n"
        "Developed by Didarul Islam | Professional DevOps Automation Project"
    )

    parser = argparse.ArgumentParser(
        prog="FileOrganizer",
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "--path",
        type=str,
        help="Directory path to organize. If not provided, default will be used from config.",
    )

    parser.add_argument(
        "--config",
        type=str,
        default="config/config.yaml",
        help="Path to configuration YAML file (default: config/config.yaml).",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate the operations without making any actual changes.",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable detailed logging output for debugging and transparency.",
    )

    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Set custom logging level (default: INFO).",
    )

    return parser


def parse_arguments():
    """
    Parse and return CLI arguments for runtime use.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = build_parser()
    args = parser.parse_args()

    # Set logging level dynamically based on CLI options
    log_level = getattr(logging, args.log_level.upper(), logging.INFO)
    logging.basicConfig(level=log_level)

    if args.verbose:
        print("Verbose mode enabled")
        print(f"Arguments received: {vars(args)}")

    return args


if __name__ == "__main__":
    # Allow standalone CLI testing
    args = parse_arguments()
    print(f"CLI Arguments Parsed: {args}")
