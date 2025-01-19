# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTimeEdit, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(713, 550)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFrameShape(QFrame.Shape.Panel)
        self.listWidget.setSortingEnabled(False)

        self.horizontalLayout_2.addWidget(self.listWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addClass = QPushButton(self.centralwidget)
        self.addClass.setObjectName(u"addClass")

        self.horizontalLayout.addWidget(self.addClass)

        self.removeClass = QPushButton(self.centralwidget)
        self.removeClass.setObjectName(u"removeClass")

        self.horizontalLayout.addWidget(self.removeClass)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 17))

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.classNameLabel = QLabel(self.centralwidget)
        self.classNameLabel.setObjectName(u"classNameLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.classNameLabel)

        self.classNameLineEdit = QLineEdit(self.centralwidget)
        self.classNameLineEdit.setObjectName(u"classNameLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.classNameLineEdit)

        self.teacherLabel = QLabel(self.centralwidget)
        self.teacherLabel.setObjectName(u"teacherLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.teacherLabel)

        self.teacherLineEdit = QLineEdit(self.centralwidget)
        self.teacherLineEdit.setObjectName(u"teacherLineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.teacherLineEdit)

        self.dayOfTheWeekLabel = QLabel(self.centralwidget)
        self.dayOfTheWeekLabel.setObjectName(u"dayOfTheWeekLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.dayOfTheWeekLabel)

        self.dayOfTheWeekComboBox = QComboBox(self.centralwidget)
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.setObjectName(u"dayOfTheWeekComboBox")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.dayOfTheWeekComboBox)

        self.blockSetupLabel = QLabel(self.centralwidget)
        self.blockSetupLabel.setObjectName(u"blockSetupLabel")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.blockSetupLabel)

        self.blockSetupLineEdit = QLineEdit(self.centralwidget)
        self.blockSetupLineEdit.setObjectName(u"blockSetupLineEdit")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.blockSetupLineEdit)

        self.notesLabel = QLabel(self.centralwidget)
        self.notesLabel.setObjectName(u"notesLabel")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.notesLabel)

        self.notesLineEdit = QLineEdit(self.centralwidget)
        self.notesLineEdit.setObjectName(u"notesLineEdit")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.notesLineEdit)

        self.classroomLabel = QLabel(self.centralwidget)
        self.classroomLabel.setObjectName(u"classroomLabel")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.classroomLabel)

        self.classroomLineEdit = QLineEdit(self.centralwidget)
        self.classroomLineEdit.setObjectName(u"classroomLineEdit")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.classroomLineEdit)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignBottom)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.periodStartLabel = QLabel(self.centralwidget)
        self.periodStartLabel.setObjectName(u"periodStartLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.periodStartLabel)

        self.periodStartDateEdit = QDateEdit(self.centralwidget)
        self.periodStartDateEdit.setObjectName(u"periodStartDateEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.periodStartDateEdit)

        self.periodEndLabel = QLabel(self.centralwidget)
        self.periodEndLabel.setObjectName(u"periodEndLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.periodEndLabel)

        self.periodEndDateEdit = QDateEdit(self.centralwidget)
        self.periodEndDateEdit.setObjectName(u"periodEndDateEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.periodEndDateEdit)

        self.timeBetweenBlockLabel = QLabel(self.centralwidget)
        self.timeBetweenBlockLabel.setObjectName(u"timeBetweenBlockLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.timeBetweenBlockLabel)

        self.timeBetweenBlockSpinBox = QSpinBox(self.centralwidget)
        self.timeBetweenBlockSpinBox.setObjectName(u"timeBetweenBlockSpinBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.timeBetweenBlockSpinBox)

        self.lunchTimeLabel = QLabel(self.centralwidget)
        self.lunchTimeLabel.setObjectName(u"lunchTimeLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lunchTimeLabel)

        self.lunchTimeTimeEdit = QTimeEdit(self.centralwidget)
        self.lunchTimeTimeEdit.setObjectName(u"lunchTimeTimeEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lunchTimeTimeEdit)

        self.dayStartLabel = QLabel(self.centralwidget)
        self.dayStartLabel.setObjectName(u"dayStartLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.dayStartLabel)

        self.dayStartTimeEdit = QTimeEdit(self.centralwidget)
        self.dayStartTimeEdit.setObjectName(u"dayStartTimeEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.dayStartTimeEdit)

        self.filenameLabel = QLabel(self.centralwidget)
        self.filenameLabel.setObjectName(u"filenameLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.filenameLabel)

        self.filenameLineEdit = QLineEdit(self.centralwidget)
        self.filenameLineEdit.setObjectName(u"filenameLineEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.filenameLineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        self.listWidget.setCurrentRow(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.addClass.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.removeClass.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Class settings", None))
        self.classNameLabel.setText(QCoreApplication.translate("MainWindow", u"Class name", None))
        self.teacherLabel.setText(QCoreApplication.translate("MainWindow", u"Teacher", None))
        self.dayOfTheWeekLabel.setText(QCoreApplication.translate("MainWindow", u"Day of the week", None))
        self.dayOfTheWeekComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Monday", None))
        self.dayOfTheWeekComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Tuesday", None))
        self.dayOfTheWeekComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Wednesday", None))
        self.dayOfTheWeekComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Thursday", None))
        self.dayOfTheWeekComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Friday", None))
        self.dayOfTheWeekComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Saturday", None))
        self.dayOfTheWeekComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Sunday", None))

        self.blockSetupLabel.setText(QCoreApplication.translate("MainWindow", u"Block", None))
        self.notesLabel.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.classroomLabel.setText(QCoreApplication.translate("MainWindow", u"Classroom", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Schedule settings", None))
        self.periodStartLabel.setText(QCoreApplication.translate("MainWindow", u"Period start", None))
        self.periodEndLabel.setText(QCoreApplication.translate("MainWindow", u"Period end", None))
        self.timeBetweenBlockLabel.setText(QCoreApplication.translate("MainWindow", u"Time between blocks", None))
        self.lunchTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Lunch time", None))
        self.dayStartLabel.setText(QCoreApplication.translate("MainWindow", u"Day start", None))
        self.filenameLabel.setText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.filenameLineEdit.setText(QCoreApplication.translate("MainWindow", u"schedule.ics", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

