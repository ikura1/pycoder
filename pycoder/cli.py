import sys

import fire

from .pycoder import show_age

def main():
    """Console script for pycoder."""
    fire.Fire(show_age)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover