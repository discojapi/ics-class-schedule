# This Python file uses the following encoding: utf-8
import sys
from schedule import SchClass, checkTime, Configs, checkDiff, checkZero, getShowName
from PySide6.QtCore import Qt, Slot, QDate
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QMessageBox, QTableWidgetItem, QFileDialog
from PySide6.QtGui import QColor
import math

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from file_tools import process, save, load

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Setup
        self.colorSet=["red","orange","yellow","green","blue","purple","brown","black","white"]
        self.activeClass = 0
        self.openFile = ""
        self.items= []
        self.configs = Configs()
        self.onNewSchedule()
        #Connections
        self.ui.actionNew.triggered.connect(self.onNewSchedule)
        self.ui.actionsaveas.triggered.connect(self.onSaveAsFile)
        self.ui.actionSave.triggered.connect(self.onSaveFile)
        self.ui.actionLoad.triggered.connect(self.onLoadFile)
        self.ui.actionabout.triggered.connect(self.onAbout)
        self.ui.actionAboutQT.triggered.connect(self.onAboutQT)
        self.ui.actionAdd_class.triggered.connect(self.addClass)
        self.ui.actionDuplicate_class.triggered.connect(self.onCloneClicked)
        self.ui.actionRemove_class.triggered.connect(self.removeClass)
        self.ui.action_gen.triggered.connect(self.onGenClicked)
        self.ui.treeWidget.clicked.connect(self.onActiveItemChange)
        self.ui.dayOfTheWeekComboBox.activated.connect(self.onDayChange)
        self.ui.spinBox.valueChanged.connect(self.onBlockChange)
        self.ui.classNameLineEdit.textEdited.connect(self.onNameChange)
        self.ui.classIDLineEdit.textEdited.connect(self.onIDChange)
        self.ui.teacherLineEdit.textEdited.connect(self.onTeacherChange)
        self.ui.classroomLineEdit.textEdited.connect(self.onClassroomChange)
        self.ui.notesLineEdit.textEdited.connect(self.onNotesChange)
        self.ui.tableWidget.cellClicked.connect(self.onActiveTableItemChange)
        self.ui.colorComboBox.activated.connect(self.onColorChange)
        self.ui.sectionSpinBox.valueChanged.connect(self.onSectionChange)

        self.ui.blockTimeMinutesSpinBox.valueChanged.connect(self.onBlockTimeChange)
        self.ui.timeBetweenBlockSpinBox.valueChanged.connect(self.onBreakTimeChange)
        self.ui.lunchStartSpinBox.valueChanged.connect(self.onLunchStartChange)
        self.ui.lunchTimeSpinBox.valueChanged.connect(self.onLunchTimeChange)
        self.ui.scheduleLineEdit.textEdited.connect(self.onScheduleChange)
        self.ui.dayStartTimeEdit.timeChanged.connect(self.onDayStartChange)
        self.ui.periodEndDateEdit.userDateChanged.connect(self.onPeriodEndChange)
        self.ui.periodStartDateEdit.userDateChanged.connect(self.onPeriodStartChange)
        self.ui.formatComboBox.activated.connect(self.onLayoutChange)
        self.ui.eventDescriptionComboBox.activated.connect(self.onDescChange)

    def redraw(self):
        self.ui.treeWidget.clear()
        self.ui.tableWidget.clearContents()
        check = 0
        #Vertical header setup
        cBlock = 1
        headers = []
        cTime = (self.configs.dStart[0],self.configs.dStart[1])
        for block in range(0,12):
            nTabItem = QTableWidgetItem()
            if block+1 == self.configs.lStart:
                nTabItem.setText("Lunch")
                cTime = checkDiff(*(cTime),self.configs.lTime)
            else:
                nLabel = f"{cBlock}-({cTime[0]}:{checkZero(cTime[1])}-"
                cTime = checkDiff(*(cTime),self.configs.blockTime)
                nLabel += f"{cTime[0]}:{checkZero(cTime[1])})"
                nTabItem.setText(nLabel)
                headers.append(nLabel)
                cBlock += 1
                if block+2 != self.configs.lStart:
                    cTime = checkDiff(*(cTime),self.configs.breakT)
            self.ui.tableWidget.setVerticalHeaderItem(block,nTabItem)
        for item in self.items:
            #Tree list
            it = QTreeWidgetItem()
            if check == self.activeClass:
                it.setCheckState(0,Qt.CheckState.Checked)
            else:
                it.setCheckState(0,Qt.CheckState.Unchecked)
            it.setText(1,str(item.name))
            it.setText(0,str(item.id))
            it.setBackground(1,QColor(self.colorSet[item.color]))
            it.setBackground(0,QColor(self.colorSet[item.color]))
            if self.colorSet[item.color] == "pink" or self.colorSet[item.color] == "yellow" or self.colorSet[item.color] == "orange" or self.colorSet[item.color] == "white":
                it.setForeground(1,QColor("black"))
                it.setForeground(0,QColor("black"))
            it.setText(5,item.teacher)
            it.setText(2,str(item.section))
            (day,block) = checkTime(item,True)
            it.setText(3,str(day))
            it.setText(4,headers[item.block - 1])
            it.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
            self.ui.treeWidget.addTopLevelItem(it)
            #Table
            (day,block) = checkTime(item,False)
            tb = QTableWidgetItem()
            tb.setText(getShowName(self.configs.layout, item.id, item.name, item.color))
            tb.setBackground(QColor(self.colorSet[item.color]))
            if self.colorSet[item.color] == "pink" or self.colorSet[item.color] == "yellow" or self.colorSet[item.color] == "orange" or self.colorSet[item.color] == "white":
                tb.setForeground(QColor("black"))
            if item.block >= self.configs.lStart :
                self.ui.tableWidget.setItem(block,day-1,tb)
            else:
                self.ui.tableWidget.setItem(block-1,day-1,tb)
            check += 1
        
        
        self.ui.classNameLineEdit.setText(self.items[self.activeClass].name)
        self.ui.classIDLineEdit.setText(self.items[self.activeClass].id)
        self.ui.teacherLineEdit.setText(self.items[self.activeClass].teacher)
        self.ui.notesLineEdit.setText(self.items[self.activeClass].notes)
        self.ui.classroomLineEdit.setText(self.items[self.activeClass].classroom)
        self.ui.dayOfTheWeekComboBox.setCurrentIndex(self.items[self.activeClass].day-1)
        self.ui.spinBox.setValue(self.items[self.activeClass].block)
        self.ui.colorComboBox.setCurrentIndex(self.items[self.activeClass].color)
        self.ui.sectionSpinBox.setValue(self.items[self.activeClass].section)

        self.ui.blockTimeMinutesSpinBox.setValue(self.configs.blockTime)
        self.ui.timeBetweenBlockSpinBox.setValue(self.configs.breakT)
        self.ui.lunchStartSpinBox.setValue(self.configs.lStart)
        self.ui.lunchTimeSpinBox.setValue(self.configs.lTime)

        self.ui.scheduleLineEdit.setText(self.configs.schedule)
        self.ui.periodStartDateEdit.setDate(QDate(*(self.configs.pStart)))
        self.ui.periodEndDateEdit.setDate(QDate(*(self.configs.pEnd)))
        self.ui.formatComboBox.setCurrentIndex(self.configs.layout)
        self.ui.eventDescriptionComboBox.setCurrentIndex(self.configs.desclayout)

    #Slots   
    @Slot(int)
    def onActiveItemChange(self,index):
        self.activeClass = index.row()
        self.redraw()
    @Slot(int,int)
    def onActiveTableItemChange(self,row,column):
        check = 0
        if row+1 == self.configs.lStart:
            row = -1
        elif row+1 > self.configs.lStart:
            row -= 1
        for item in self.items:
            if checkTime(item,False) == (column+1,row+1):
                self.activeClass = check
                self.redraw()
                return
            check += 1

    def onSaveAsFile(self):
        newFile = QFileDialog.getSaveFileName(self, ("Save Schedule"),"schedule.txt",("Text file (*.txt)"))
        if newFile != ('', ''):
            self.openFile = newFile[0]
            self.onSaveFile()

    def onSaveFile(self):
        if self.openFile == "":
            self.onSaveAsFile()
        else:
            try:
                save(self.items, self.configs, self.openFile)
                title = self.openFile.split("/")
                self.setWindowTitle(f"Class Schedule Maker - {title[len(title)-1]}")
            except:
                QMessageBox.warning(self,"Error","Couldn't save your file, please check your configurations")

    def onLoadFile(self):
        fileName = QFileDialog.getOpenFileName(self, ("Open Schedule"), "schedule.txt", ("Text file (*.txt)"))
        if fileName != ('', ''):
            try:
                self.openFile = fileName[0]
                self.activeClass = 0
                (correct, configs) = load(self.items, self.openFile)
                if correct:
                    self.configs = configs
                    self.redraw()
                    title = self.openFile.split("/")
                    self.setWindowTitle(f"Class Schedule Maker - {title[len(title)-1]}")
                else:
                    QMessageBox.warning(self,"Error","Incorrect file")
            except:
                QMessageBox.warning(self,"Error","Couldn't load your file")

    def onNewSchedule(self):
        #if self.openFile != "":
        #    pass
        #else:
            self.setWindowTitle(f"Class Schedule Maker")
            self.openFile = ""
            self.items.clear()
            self.configs = Configs()
            self.addClass()
            self.redraw()


    def onGenClicked(self):
        newFile = QFileDialog.getSaveFileName(self, ("Export Schedule"),"schedule.ics",("iCalendar file (*.ics)"))
        if newFile != ('', ''):
            #try :
                process(self.items, self.configs, newFile[0])
                QMessageBox.information(self, "Generated", "Your calendar file "+ newFile[0] + " has been generated successfully")
            #except : 
            #    QMessageBox.warning(self,"Error","Couldn't generate .ics file, please check your configurations")
    def onCloneClicked(self):
        clone = self.items[self.activeClass]
        self.items.append(SchClass(clone.id, clone.name,  clone.day, clone.block, clone.teacher, clone.notes, clone.classroom, clone.color, clone.section))
        self.activeClass = len(self.items)-1
        self.redraw()
    @Slot()  
    def addClass(self):
        self.items.append(SchClass())
        self.activeClass = len(self.items)-1
        self.redraw()
    @Slot()
    def removeClass(self):
        if len(self.items) > 1:
            self.items.pop(self.activeClass)
            if self.activeClass >=  len(self.items)-1:
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
    def onIDChange(self, ID):
        self.items[self.activeClass].id = ID
        self.redraw()
    @Slot(str)
    def onTeacherChange(self,name):
        self.items[self.activeClass].teacher = name
        self.redraw()
    @Slot(str)
    def onNotesChange(self,notes):
        self.items[self.activeClass].notes = notes
        self.redraw()
    def onSectionChange(self, section):
        self.items[self.activeClass].section = section
        self.redraw()
    @Slot(str)
    def onClassroomChange(self,classroom):
        self.items[self.activeClass].classroom = classroom
        self.redraw()
    def onDescChange(self, index):
        self.configs.desclayout = index
        self.redraw()
    def onColorChange(self,color):
        self.items[self.activeClass].color = color
        self.redraw()
    def onLayoutChange(self, layout):
        self.configs.layout = layout
        self.redraw()
    def onBlockTimeChange(self,time):
        self.configs.blockTime = time
        self.redraw()
    def onBreakTimeChange(self,time):
        self.configs.breakT = time
        self.redraw()
    def onLunchStartChange(self,block):
        self.configs.lStart = block
        self.redraw()
    def onLunchTimeChange(self,time):
        self.configs.lTime=time
        self.redraw()
    def onScheduleChange(self,schedule):
        self.configs.schedule = schedule
        self.redraw()
    def onDayStartChange(self,start):
        self.configs.dStart[0] = start.hour()
        self.configs.dStart[1] = start.minute()
        self.redraw()
    def onPeriodStartChange(self, date):
        self.configs.pStart = (date.year(),date.month(),date.day())
        self.redraw()
    def onPeriodEndChange(self, date):
        self.configs.pEnd = (date.year(),date.month(),date.day())
        self.redraw()
    def onAbout(self):
        QMessageBox.about(self, "About", 'Class Schedule Generator\nBy Sebastián Saldias')
    def onAboutQT(self):
        QMessageBox.aboutQt(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
