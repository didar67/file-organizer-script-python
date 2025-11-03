# File Organizer Script

A professional, automation-ready Python tool that organizes files into folders by extension.
This project demonstrates **modular architecture, CLI integration, logging, and configuration via YAML** — making it a great example of DevOps automation scripting.

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/file_organizer.git
cd file_organizer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the script
python main.py --path /path/to/folder --verbose
```

---

## Features

* Organizes files by extension automatically
* CLI interface with `argparse`
* YAML-based configuration system
* Rotating log file support
* Dry-run mode for safe testing

---

## Project Structure

```
file_organizer/
├── cli/              # CLI argument parsing
├── core/             # Core logic & file operations
├── utils/            # Helper functions & YAML config loader
├── tests/            # Automated test scripts
├── docs/             # Documentation
└── main.py           # Entry point
```

---

## Author

**Didarul Islam** — DevOps & Cloud Automation Enthusiast
[GitHub Profile](https://github.com/<your-username>)
