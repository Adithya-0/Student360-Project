# Student360 — Student Academic & Career Analytics System

Student360 is a pure-Python, menu-driven application for tracking and analyzing
student academic performance, assignments, progress, and placement readiness.

## Features

- Student Performance Analyzer
- Assignment Performance Analyzer
- Student Progress Tracker
- Placement Readiness Analyzer
- Student Profile
- Overall Student Report
- JSON-based data persistence
- Input validation and exception handling
- Modular project structure
- Object-oriented domain models

## Technologies

- Python 3
- Object-Oriented Programming
- JSON
- pathlib / file handling
- datetime
- Lists, dictionaries and sorting
- Modular programming

## Project Structure

```text
Student360/
├── main.py
├── models/
├── modules/
├── utils/
└── data/
```

## How to Run

Make sure Python 3 is installed.

From the Student360 directory:

```bash
python3 main.py
```

No third-party Python packages are required.

## Important Design Note

This version deliberately does not use a database or external API.
JSON files are used for persistence so the project remains focused on
Python programming, OOP, file handling, validation and analytics.

## Sample Credentials

No login is required. The application starts with sample student data.

## Future Enhancements

- Add a graphical interface
- Add automated unit tests
- Add charts and visual reports
- Add multiple student profiles
- Add CSV import/export
- Add a database in a future version
