# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.addClass.clicked.connect(self.addClass)
        self.ui.removeClass.clicked.connect(self.removeClass)
    
    @Slot()
    def addClass(self):
        self.ui.listWidget.addItem(QListWidgetItem())

    @Slot()
    def removeClass(self):
        if self.ui.listWidget.count > 1:
            pass
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle("Ics class schedule generator")
    widget.show()
    sys.exit(app.exec())
