# North Sussex Judo Fee Calculator

A small Python 3 desktop application for the Pearson Higher Nationals Unit 1 programming assignment.

The program calculates monthly training fees, competition costs, private coaching costs, total monthly cost, and compares an athlete's weight against a chosen competition category.

## Features

- Tkinter desktop interface
- Object-oriented and procedural code structure
- Event-driven button and selection handlers
- Input validation with clear error messages
- Itemised monthly cost breakdown
- Weight category comparison
- Unit tests for calculation logic

## Requirements

- Python 3.10 or later
- Standard library only
- Tkinter support in your Python installation

On macOS, the Homebrew Python build may not include `_tkinter`. If the app fails with `ModuleNotFoundError: No module named '_tkinter'`, use a Python installation that includes Tk support, such as the official python.org installer.

## How to Run

Run the application from the project root:

```bash
python3 main.py
```

## How to Run Tests

```bash
python3 -m unittest discover tests
```

## Windows Executable

From a Windows machine in the project root, run:

```bat
build_windows.bat
```

Or, in PowerShell:

```powershell
.\build_windows.ps1
```

The resulting executable will be created at:

```text
dist\NorthSussexJudoFeeCalculator.exe
```

## Docker

Build and run the container:

```bash
docker compose up --build
```

Open the app in your browser at:

```text
http://localhost:6080/vnc.html
```

The container starts a small virtual desktop, runs the Tkinter app inside it, and exposes it through noVNC. Port `5900` is also available if you want to connect with a VNC client.

## Project Structure

```text
north-sussex-judo/
├── main.py
├── app.py
├── calculator.py
├── models.py
├── validation.py
├── tests/
│   └── test_calculator.py
├── docs/
│   ├── algorithm.md
│   ├── coding-standards.md
│   ├── debugging-notes.md
│   ├── presentation-notes.md
│   └── testing-notes.md
├── Dockerfile
└── docker-compose.yml
```

## Programming Paradigms Used

- Procedural programming is used in helper functions such as validation and formatting.
- Object-oriented programming is used in the `Athlete` model and `CostCalculator` class.
- Event-driven programming is used in the Tkinter GUI through button clicks and selection events.
