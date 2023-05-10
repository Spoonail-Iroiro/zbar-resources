import sys
from pathlib import Path


if getattr(sys, 'frozen', False):
    application_dir = Path(sys._MEIPASS).parent
else:
    application_dir = Path(__file__).parent.parent.parent
