# This Python file uses the following encoding: utf-8
import sys
from schedule import SchClass, checkTime
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QColor

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
        self.items= []
        self.addClass()
        #Connections
        self.ui.addClass.clicked.connect(self.addClass)
        self.ui.removeClass.clicked.connect(self.removeClass)
        self.ui.gen_button.clicked.connect(self.onGenClicked)
        self.ui.treeWidget.clicked.connect(self.onActiveItemChange)
        self.ui.dayOfTheWeekComboBox.activated.connect(self.onDayChange)
        self.ui.spinBox.valueChanged.connect(self.onBlockChange)
        self.ui.classNameLineEdit.textEdited.connect(self.onNameChange)
        self.ui.teacherLineEdit.textEdited.connect(self.onTeacherChange)
        self.ui.classroomLineEdit.textEdited.connect(self.onClassroomChange)
        self.ui.notesLineEdit.textEdited.connect(self.onNotesChange)
        self.ui.tableWidget.cellClicked.connect(self.onActiveTableItemChange)

    def redraw(self):
        self.ui.treeWidget.clear()
        self.ui.tableWidget.clearContents()
        check = 0
        for item in self.items:
            #Tree list
            it = QTreeWidgetItem()
            if check == self.activeClass:
                it.setCheckState(0,Qt.CheckState.Checked)
            else:
                it.setCheckState(0,Qt.CheckState.Unchecked)
            it.setText(1,item.name)
            it.setText(4,item.teacher)
            (day,block) = checkTime(item,True)
            it.setText(2,day)
            it.setText(3,str(block))
            it.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
            self.ui.treeWidget.addTopLevelItem(it)
            #Table
            (day,block) = checkTime(item,False)
            tb = QTableWidgetItem()
            tb.setText(item.name)
            tb.setBackground(QColor("orange"))
            self.ui.tableWidget.setItem(block-1,day-1,tb)
            check += 1
        self.ui.classNameLineEdit.setText(self.items[self.activeClass].name)
        self.ui.teacherLineEdit.setText(self.items[self.activeClass].teacher)
        self.ui.notesLineEdit.setText(self.items[self.activeClass].notes)
        self.ui.classroomLineEdit.setText(self.items[self.activeClass].classroom)
        self.ui.dayOfTheWeekComboBox.setCurrentIndex(self.items[self.activeClass].day-1)
        self.ui.spinBox.setValue(self.items[self.activeClass].block)

    #Slots    
    
    @Slot(int)
    def onActiveItemChange(self,index):
        self.activeClass = index.row()
        self.redraw()
    @Slot(int,int)
    def onActiveTableItemChange(self,row,column):
        check = 0
        for item in self.items:
            if checkTime(item,False) == (column+1,row+1):
                self.activeClass = check
                self.redraw()
                return
            check += 1

    def onGenClicked(self, item):
        QMessageBox.information(self, "Generated", "Your calendar file "+ self.ui.filenameLineEdit.text() + " has been generated successfully")

    @Slot()  
    def addClass(self):
        self.items.append(SchClass())
        self.activeClass = len(self.items)-1
        self.redraw()
    @Slot()
    def removeClass(self):
        if len(self.items) > 1:
            self.items.pop(self.activeClass)
            self.activeClass = len(self.items)-1
        self.redraw()
    @Slot(str)
    def onNameChange(self):
        self.items[self.activeClass].name = self.ui.classNameLineEdit.text()
        self.redraw()
    def onDayChange(self,day):
        self.items[self.activeClass].day = day+1
        self.redraw()
    @Slot(int)
    def onBlockChange(self,block):
        self.items[self.activeClass].block = block
        self.redraw()
    @Slot(str)
    def onTeacherChange(self,name):
        self.items[self.activeClass].teacher = name
        self.redraw()
    @Slot(str)
    def onNotesChange(self,notes):
        self.items[self.activeClass].notes = notes
        self.redraw()
    @Slot(str)
    def onClassroomChange(self,classroom):
        self.items[self.activeClass].classroom = classroom
        self.redraw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle("Class schedule generator")
    widget.show()
    sys.exit(app.exec())
