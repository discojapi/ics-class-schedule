# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QMessageBox

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
        self.activeClass = 0
        #Connections
        self.ui.addClass.clicked.connect(self.addClass)
        self.items= []
        for i in range(0, 10):
            self.items.append(QTreeWidgetItem())
        self.ui.treeWidget.insertTopLevelItems(0, self.items)
        self.ui.gen_button.clicked.connect(self.onGenClicked)

    def onGenClicked(self, item):
        QMessageBox.information(self, "Generated", "Your calendar file "+ self.ui.filenameLineEdit.text() + " has been generated successfully")

    
    #Slots
    @Slot()
    def addClass(self):
        self.items.append(QTreeWidgetItem())
    @Slot()
    def removeClass(self):
        if self.ui.treeWidget.count > 1:
            pass
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle("Class schedule generator")
    widget.show()
    sys.exit(app.exec())
