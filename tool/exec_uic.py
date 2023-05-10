from pathlib import Path
import subprocess
import os

module_name = "qrsend"

forms_dir = Path(__file__).parent.parent / "src" / module_name / "forms"

ui_paths = list(forms_dir.glob("*.ui"))

form_template = """
from PySide6.QtWidgets import QDialog, QWidget
from .{} import Ui_

class ClassName(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_
        self.ui.setupUi(self)
"""

# for path in ui_paths:
for root_dir, dirs, files in os.walk(forms_dir):
    for filename in files:
        path = Path(root_dir + "\\" + filename)
        if path.suffix != ".ui":
            continue
        print(path)
        export_path = path.with_name(path.stem + "_ui").with_suffix(".py")
        cmd = f'pyside6-uic "{path}" -o "{export_path}" '
        print(cmd)
        subprocess.run(cmd)
        text = export_path.read_text(encoding="utf-8")
        text = f"from {module_name}.dirs import application_dir\n" + text
        # text = text.replace("u\"../../Resource", "application_dir / u\"Resource")
        # text = text.replace("u\"../../Resource", "u\"Resource")
        import re
        pattern = r"u\"../../(data/[^\"]*)\""
        repl = r"str(application_dir / u'\1')"
        text = re.sub(pattern, repl, text)
        export_path.write_text(text)
        logic_py_path = path.with_suffix(".py")
        if logic_py_path.exists() is False:
            logic_py_path.write_text(form_template.format(export_path.stem),encoding="utf-8")


