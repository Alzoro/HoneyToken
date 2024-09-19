Dynamic Honeytoken Monitoring System (Linux)

Overview:

The Dynamic Honeytoken Monitoring System is a command-line tool built for Linux that deploys, monitors, and tracks honeytokens (decoy files) in the file system. If an unauthorized user accesses, modifies, or deletes these files, the system sends real-time alerts via a Telegram bot.

Features:

- File Access Monitoring: Detects unauthorized access to honeytokens.
- File Modification/Deletion Alerts: Tracks file modifications or deletions and triggers alerts.
- Telegram Bot Integration: Sends real-time alert messages directly to a configured Telegram bot.
- Background Monitoring: The monitoring script runs in the background, ensuring continuous tracking.
- CLI Interface: Simple and intuitive command-line interface for deployment and monitoring.

Requirements:

- Linux Operating System
- Python 3.x
- The following Python modules:
    - typer
    - art
    - termcolor
    - os
    - pathlib
    - docx
    - docx2txt
    - python-telegram-bot
    - watchdog
      
Future Enhancements:

- Additional alert channels (e.g., email).
- More customizable monitoring options.
- Support for other operating systems.
