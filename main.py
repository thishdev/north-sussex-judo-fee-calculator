"""Entry point for the North Sussex Judo fee calculator."""

import sys


def _load_run_app():
    try:
        from app import run_app
    except ModuleNotFoundError as error:
        if error.name == "_tkinter":
            sys.stderr.write(
                "Tkinter is not available in this Python installation.\n"
                "On this Mac, run the app with: /usr/bin/python3 main.py\n"
                "or install a Python build that includes Tk support.\n"
            )
            raise SystemExit(1) from error
        raise

    return run_app


if __name__ == "__main__":
    _load_run_app()()
