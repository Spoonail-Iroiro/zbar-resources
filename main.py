from PySide6.QtWidgets import QApplication
from qrsend.forms.select_form import SelectForm
import sys
import logging
logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

def main():
    app = QApplication(sys.argv)
    form = SelectForm()
    form.show()
    code = app.exec()

    sys.exit(code)

if __name__ == "__main__":
    main()