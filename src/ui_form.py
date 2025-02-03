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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDateEdit, QFormLayout, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QScrollArea, QSizePolicy, QSpinBox,
    QStatusBar, QTableWidget, QTableWidgetItem, QTimeEdit,
    QToolBar, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1149, 892)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.actionAdd_class = QAction(MainWindow)
        self.actionAdd_class.setObjectName(u"actionAdd_class")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.actionAdd_class.setIcon(icon1)
        self.actionAdd_class.setMenuRole(QAction.MenuRole.NoRole)
        self.actionRemove_class = QAction(MainWindow)
        self.actionRemove_class.setObjectName(u"actionRemove_class")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.actionRemove_class.setIcon(icon2)
        self.actionRemove_class.setMenuRole(QAction.MenuRole.NoRole)
        self.actionsaveas = QAction(MainWindow)
        self.actionsaveas.setObjectName(u"actionsaveas")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSaveAs))
        self.actionsaveas.setIcon(icon3)
        self.actionsaveas.setMenuRole(QAction.MenuRole.NoRole)
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.actionLoad.setIcon(icon4)
        self.actionLoad.setMenuRole(QAction.MenuRole.NoRole)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.actionNew.setIcon(icon5)
        self.actionNew.setMenuRole(QAction.MenuRole.NoRole)
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.actionabout.setIcon(icon6)
        self.actionabout.setMenuRole(QAction.MenuRole.AboutRole)
        self.action_gen = QAction(MainWindow)
        self.action_gen.setObjectName(u"action_gen")
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AppointmentNew))
        self.action_gen.setIcon(icon7)
        self.action_gen.setMenuRole(QAction.MenuRole.NoRole)
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InsertImage))
        self.actionExport.setIcon(icon8)
        self.actionExport.setMenuRole(QAction.MenuRole.NoRole)
        self.actionDuplicate_class = QAction(MainWindow)
        self.actionDuplicate_class.setObjectName(u"actionDuplicate_class")
        icon9 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.actionDuplicate_class.setIcon(icon9)
        self.actionDuplicate_class.setMenuRole(QAction.MenuRole.NoRole)
        self.actionAboutQT = QAction(MainWindow)
        self.actionAboutQT.setObjectName(u"actionAboutQT")
        self.actionAboutQT.setIcon(icon6)
        self.actionAboutQT.setVisible(True)
        self.actionAboutQT.setMenuRole(QAction.MenuRole.NoRole)
        self.actionAboutQT.setIconVisibleInMenu(True)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon10 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.actionSave.setIcon(icon10)
        self.actionSave.setMenuRole(QAction.MenuRole.NoRole)
        self.actionItemUp = QAction(MainWindow)
        self.actionItemUp.setObjectName(u"actionItemUp")
        icon11 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoUp))
        self.actionItemUp.setIcon(icon11)
        self.actionItemUp.setMenuRole(QAction.MenuRole.NoRole)
        self.actionItemDown = QAction(MainWindow)
        self.actionItemDown.setObjectName(u"actionItemDown")
        icon12 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.actionItemDown.setIcon(icon12)
        self.actionItemDown.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeWidget = QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.treeWidget.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setMinimumSectionSize(100)
        self.treeWidget.header().setDefaultSectionSize(170)

        self.verticalLayout_2.addWidget(self.treeWidget)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 11):
            self.tableWidget.setRowCount(11)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setBackground(brush);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.tableWidget.setDefaultDropAction(Qt.DropAction.ActionMask)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.DashLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(11)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(1)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(119)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(1)
        self.tableWidget.verticalHeader().setDefaultSectionSize(38)
        self.tableWidget.verticalHeader().setProperty(u"showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 5)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 390, 832))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 17))

        self.verticalLayout_3.addWidget(self.label_2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.classNameLabel = QLabel(self.scrollAreaWidgetContents)
        self.classNameLabel.setObjectName(u"classNameLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.classNameLabel)

        self.classNameLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.classNameLineEdit.setObjectName(u"classNameLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.classNameLineEdit)

        self.sectionLabel = QLabel(self.scrollAreaWidgetContents)
        self.sectionLabel.setObjectName(u"sectionLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.sectionLabel)

        self.sectionSpinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.sectionSpinBox.setObjectName(u"sectionSpinBox")
        self.sectionSpinBox.setMinimum(0)
        self.sectionSpinBox.setMaximum(1000)
        self.sectionSpinBox.setValue(0)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.sectionSpinBox)

        self.teacherLabel = QLabel(self.scrollAreaWidgetContents)
        self.teacherLabel.setObjectName(u"teacherLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.teacherLabel)

        self.teacherLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.teacherLineEdit.setObjectName(u"teacherLineEdit")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.teacherLineEdit)

        self.dayOfTheWeekLabel = QLabel(self.scrollAreaWidgetContents)
        self.dayOfTheWeekLabel.setObjectName(u"dayOfTheWeekLabel")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.dayOfTheWeekLabel)

        self.dayOfTheWeekComboBox = QComboBox(self.scrollAreaWidgetContents)
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.addItem("")
        self.dayOfTheWeekComboBox.setObjectName(u"dayOfTheWeekComboBox")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.dayOfTheWeekComboBox)

        self.blockSetupLabel = QLabel(self.scrollAreaWidgetContents)
        self.blockSetupLabel.setObjectName(u"blockSetupLabel")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.blockSetupLabel)

        self.spinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.setValue(1)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.spinBox)

        self.notesLabel = QLabel(self.scrollAreaWidgetContents)
        self.notesLabel.setObjectName(u"notesLabel")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.notesLabel)

        self.notesLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.notesLineEdit.setObjectName(u"notesLineEdit")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.notesLineEdit)

        self.classroomLabel = QLabel(self.scrollAreaWidgetContents)
        self.classroomLabel.setObjectName(u"classroomLabel")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.classroomLabel)

        self.classroomLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.classroomLineEdit.setObjectName(u"classroomLineEdit")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.classroomLineEdit)

        self.colorLabel = QLabel(self.scrollAreaWidgetContents)
        self.colorLabel.setObjectName(u"colorLabel")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.colorLabel)

        self.colorComboBox = QComboBox(self.scrollAreaWidgetContents)
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.setObjectName(u"colorComboBox")
        self.colorComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.colorComboBox)

        self.classIDLabel = QLabel(self.scrollAreaWidgetContents)
        self.classIDLabel.setObjectName(u"classIDLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.classIDLabel)

        self.classIDLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.classIDLineEdit.setObjectName(u"classIDLineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.classIDLineEdit)


        self.verticalLayout_3.addLayout(self.formLayout_2)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.periodStartLabel = QLabel(self.scrollAreaWidgetContents)
        self.periodStartLabel.setObjectName(u"periodStartLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.periodStartLabel)

        self.periodStartDateEdit = QDateEdit(self.scrollAreaWidgetContents)
        self.periodStartDateEdit.setObjectName(u"periodStartDateEdit")
        self.periodStartDateEdit.setDateTime(QDateTime(QDate(2025, 1, 2), QTime(0, 0, 0)))
        self.periodStartDateEdit.setDisplayFormat(u"dd-MM-yyyy")
        self.periodStartDateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.periodStartDateEdit)

        self.periodEndLabel = QLabel(self.scrollAreaWidgetContents)
        self.periodEndLabel.setObjectName(u"periodEndLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.periodEndLabel)

        self.periodEndDateEdit = QDateEdit(self.scrollAreaWidgetContents)
        self.periodEndDateEdit.setObjectName(u"periodEndDateEdit")
        self.periodEndDateEdit.setDateTime(QDateTime(QDate(2026, 1, 1), QTime(0, 0, 0)))
        self.periodEndDateEdit.setDisplayFormat(u"dd-MM-yyyy")
        self.periodEndDateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.periodEndDateEdit)

        self.blockTimeMinutesLabel = QLabel(self.scrollAreaWidgetContents)
        self.blockTimeMinutesLabel.setObjectName(u"blockTimeMinutesLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.blockTimeMinutesLabel)

        self.blockTimeMinutesSpinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.blockTimeMinutesSpinBox.setObjectName(u"blockTimeMinutesSpinBox")
        self.blockTimeMinutesSpinBox.setValue(70)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.blockTimeMinutesSpinBox)

        self.timeBetweenBlockLabel = QLabel(self.scrollAreaWidgetContents)
        self.timeBetweenBlockLabel.setObjectName(u"timeBetweenBlockLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.timeBetweenBlockLabel)

        self.timeBetweenBlockSpinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.timeBetweenBlockSpinBox.setObjectName(u"timeBetweenBlockSpinBox")
        self.timeBetweenBlockSpinBox.setValue(10)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.timeBetweenBlockSpinBox)

        self.lunchStartLabel = QLabel(self.scrollAreaWidgetContents)
        self.lunchStartLabel.setObjectName(u"lunchStartLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lunchStartLabel)

        self.lunchStartSpinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.lunchStartSpinBox.setObjectName(u"lunchStartSpinBox")
        self.lunchStartSpinBox.setMinimum(1)
        self.lunchStartSpinBox.setMaximum(10)
        self.lunchStartSpinBox.setValue(5)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lunchStartSpinBox)

        self.lunchTimeLabel = QLabel(self.scrollAreaWidgetContents)
        self.lunchTimeLabel.setObjectName(u"lunchTimeLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lunchTimeLabel)

        self.lunchTimeSpinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.lunchTimeSpinBox.setObjectName(u"lunchTimeSpinBox")
        self.lunchTimeSpinBox.setMinimum(1)
        self.lunchTimeSpinBox.setMaximum(200)
        self.lunchTimeSpinBox.setValue(60)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lunchTimeSpinBox)

        self.dayStartLabel = QLabel(self.scrollAreaWidgetContents)
        self.dayStartLabel.setObjectName(u"dayStartLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.dayStartLabel)

        self.dayStartTimeEdit = QTimeEdit(self.scrollAreaWidgetContents)
        self.dayStartTimeEdit.setObjectName(u"dayStartTimeEdit")
        self.dayStartTimeEdit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(8, 15, 0)))
        self.dayStartTimeEdit.setMaximumTime(QTime(23, 59, 59))
        self.dayStartTimeEdit.setMinimumTime(QTime(0, 0, 0))
        self.dayStartTimeEdit.setCalendarPopup(False)
        self.dayStartTimeEdit.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.dayStartTimeEdit)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.line_2)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.filenameLabel = QLabel(self.scrollAreaWidgetContents)
        self.filenameLabel.setObjectName(u"filenameLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.filenameLabel)

        self.scheduleLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.scheduleLineEdit.setObjectName(u"scheduleLineEdit")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.scheduleLineEdit)

        self.formatLabel = QLabel(self.scrollAreaWidgetContents)
        self.formatLabel.setObjectName(u"formatLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.formatLabel)

        self.formatComboBox = QComboBox(self.scrollAreaWidgetContents)
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.setObjectName(u"formatComboBox")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.formatComboBox)

        self.eventDescriptionLabel = QLabel(self.scrollAreaWidgetContents)
        self.eventDescriptionLabel.setObjectName(u"eventDescriptionLabel")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.eventDescriptionLabel)

        self.eventDescriptionComboBox = QComboBox(self.scrollAreaWidgetContents)
        self.eventDescriptionComboBox.addItem("")
        self.eventDescriptionComboBox.addItem("")
        self.eventDescriptionComboBox.addItem("")
        self.eventDescriptionComboBox.setObjectName(u"eventDescriptionComboBox")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.eventDescriptionComboBox)


        self.verticalLayout_3.addLayout(self.formLayout_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonFollowStyle)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionLoad)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionsaveas)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_class)
        self.toolBar.addAction(self.actionDuplicate_class)
        self.toolBar.addAction(self.actionRemove_class)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionItemUp)
        self.toolBar.addAction(self.actionItemDown)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_gen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionabout)
        self.toolBar.addAction(self.actionAboutQT)

        self.retranslateUi(MainWindow)

        self.colorComboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd_class.setText(QCoreApplication.translate("MainWindow", u"Add class", None))
#if QT_CONFIG(tooltip)
        self.actionAdd_class.setToolTip(QCoreApplication.translate("MainWindow", u"Adds empty class", None))
#endif // QT_CONFIG(tooltip)
        self.actionRemove_class.setText(QCoreApplication.translate("MainWindow", u"Remove class", None))
#if QT_CONFIG(tooltip)
        self.actionRemove_class.setToolTip(QCoreApplication.translate("MainWindow", u"Removes class data", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionRemove_class.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.actionsaveas.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
#if QT_CONFIG(tooltip)
        self.actionsaveas.setToolTip(QCoreApplication.translate("MainWindow", u"Save to a .txt file", None))
#endif // QT_CONFIG(tooltip)
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_gen.setText(QCoreApplication.translate("MainWindow", u"Generate .ics file", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export to image", None))
        self.actionDuplicate_class.setText(QCoreApplication.translate("MainWindow", u"Duplicate class", None))
#if QT_CONFIG(tooltip)
        self.actionDuplicate_class.setToolTip(QCoreApplication.translate("MainWindow", u"Clone selected event", None))
#endif // QT_CONFIG(tooltip)
        self.actionAboutQT.setText(QCoreApplication.translate("MainWindow", u"AboutQT", None))
#if QT_CONFIG(tooltip)
        self.actionAboutQT.setToolTip(QCoreApplication.translate("MainWindow", u"Show info about QT", None))
#endif // QT_CONFIG(tooltip)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"Save schedule to a file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionItemUp.setText("")
#if QT_CONFIG(tooltip)
        self.actionItemUp.setToolTip(QCoreApplication.translate("MainWindow", u"Moves the current item up.", None))
#endif // QT_CONFIG(tooltip)
        self.actionItemDown.setText("")
#if QT_CONFIG(tooltip)
        self.actionItemDown.setToolTip(QCoreApplication.translate("MainWindow", u"Moves the current item down.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Teacher", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Block", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Day", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Section", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Class name", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Class ID", None));
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Monday", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tuesday", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Wednesday", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Thursday", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Friday", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Saturday", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Sunday", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Class settings", None))
        self.classNameLabel.setText(QCoreApplication.translate("MainWindow", u"Class name", None))
        self.classNameLineEdit.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.sectionLabel.setText(QCoreApplication.translate("MainWindow", u"Section", None))
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
        self.colorLabel.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.colorComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.colorComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Orange", None))
        self.colorComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Yellow", None))
        self.colorComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Green", None))
        self.colorComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.colorComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Purple", None))
        self.colorComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Brown", None))
        self.colorComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Black", None))
        self.colorComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"White", None))

        self.classIDLabel.setText(QCoreApplication.translate("MainWindow", u"Class ID", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Schedule settings", None))
        self.periodStartLabel.setText(QCoreApplication.translate("MainWindow", u"Period start", None))
        self.periodEndLabel.setText(QCoreApplication.translate("MainWindow", u"Period end", None))
        self.blockTimeMinutesLabel.setText(QCoreApplication.translate("MainWindow", u"Block time (minutes)", None))
        self.timeBetweenBlockLabel.setText(QCoreApplication.translate("MainWindow", u"Time between blocks (minutes)", None))
        self.lunchStartLabel.setText(QCoreApplication.translate("MainWindow", u"Lunch start block", None))
        self.lunchTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Lunch time (Minutes)", None))
        self.dayStartLabel.setText(QCoreApplication.translate("MainWindow", u"Day start", None))
        self.dayStartTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Export settings", None))
        self.filenameLabel.setText(QCoreApplication.translate("MainWindow", u"Calendar name", None))
        self.scheduleLineEdit.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.formatLabel.setText(QCoreApplication.translate("MainWindow", u"Event format", None))
        self.formatComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ID - Class name", None))
        self.formatComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Class name -ID", None))
        self.formatComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"ID - Class name {color emoji}", None))
        self.formatComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Class name - ID {color emoji}", None))
        self.formatComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"ID", None))
        self.formatComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Class name", None))

        self.eventDescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Event description", None))
        self.eventDescriptionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Section - Teacher - Classroom - Notes", None))
        self.eventDescriptionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Section ; Teacher ; Classroom ; Notes", None))
        self.eventDescriptionComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Section, Teacher, Classroom, Notes", None))

        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

