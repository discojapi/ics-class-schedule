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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFormLayout, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QSizePolicy, QSpinBox, QStatusBar, QTableWidget,
    QTableWidgetItem, QTimeEdit, QToolBar, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1149, 781)
        self.actionAdd_class = QAction(MainWindow)
        self.actionAdd_class.setObjectName(u"actionAdd_class")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.actionAdd_class.setIcon(icon)
        self.actionAdd_class.setMenuRole(QAction.MenuRole.NoRole)
        self.actionRemove_class = QAction(MainWindow)
        self.actionRemove_class.setObjectName(u"actionRemove_class")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.actionRemove_class.setIcon(icon1)
        self.actionRemove_class.setMenuRole(QAction.MenuRole.NoRole)
        self.actionsaveas = QAction(MainWindow)
        self.actionsaveas.setObjectName(u"actionsaveas")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSaveAs))
        self.actionsaveas.setIcon(icon2)
        self.actionsaveas.setMenuRole(QAction.MenuRole.NoRole)
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.actionLoad.setIcon(icon3)
        self.actionLoad.setMenuRole(QAction.MenuRole.NoRole)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.actionNew.setIcon(icon4)
        self.actionNew.setMenuRole(QAction.MenuRole.NoRole)
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.actionabout.setIcon(icon5)
        self.actionabout.setMenuRole(QAction.MenuRole.AboutRole)
        self.action_gen = QAction(MainWindow)
        self.action_gen.setObjectName(u"action_gen")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AppointmentNew))
        self.action_gen.setIcon(icon6)
        self.action_gen.setMenuRole(QAction.MenuRole.NoRole)
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InsertImage))
        self.actionExport.setIcon(icon7)
        self.actionExport.setMenuRole(QAction.MenuRole.NoRole)
        self.actionDuplicate_class = QAction(MainWindow)
        self.actionDuplicate_class.setObjectName(u"actionDuplicate_class")
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.actionDuplicate_class.setIcon(icon8)
        self.actionDuplicate_class.setMenuRole(QAction.MenuRole.NoRole)
        self.actionAboutQT = QAction(MainWindow)
        self.actionAboutQT.setObjectName(u"actionAboutQT")
        self.actionAboutQT.setIcon(icon5)
        self.actionAboutQT.setMenuRole(QAction.MenuRole.NoRole)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon9 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.actionSave.setIcon(icon9)
        self.actionSave.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeWidget = QTreeWidget(self.centralwidget)
        self.treeWidget.headerItem().setText(0, "")
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setAnimated(True)

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
        self.tableWidget.setRowCount(11)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(119)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(38)
        self.tableWidget.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 5)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 17))

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
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

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.setValue(1)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.spinBox)

        self.colorLabel = QLabel(self.centralwidget)
        self.colorLabel.setObjectName(u"colorLabel")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.colorLabel)

        self.colorComboBox = QComboBox(self.centralwidget)
        self.colorComboBox.addItem("")
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

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.colorComboBox)


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
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.periodStartLabel = QLabel(self.centralwidget)
        self.periodStartLabel.setObjectName(u"periodStartLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.periodStartLabel)

        self.periodStartDateEdit = QDateEdit(self.centralwidget)
        self.periodStartDateEdit.setObjectName(u"periodStartDateEdit")
        self.periodStartDateEdit.setDateTime(QDateTime(QDate(2025, 1, 2), QTime(0, 0, 0)))
        self.periodStartDateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.periodStartDateEdit)

        self.periodEndLabel = QLabel(self.centralwidget)
        self.periodEndLabel.setObjectName(u"periodEndLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.periodEndLabel)

        self.periodEndDateEdit = QDateEdit(self.centralwidget)
        self.periodEndDateEdit.setObjectName(u"periodEndDateEdit")
        self.periodEndDateEdit.setDateTime(QDateTime(QDate(2026, 1, 1), QTime(0, 0, 0)))
        self.periodEndDateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.periodEndDateEdit)

        self.blockTimeMinutesLabel = QLabel(self.centralwidget)
        self.blockTimeMinutesLabel.setObjectName(u"blockTimeMinutesLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.blockTimeMinutesLabel)

        self.blockTimeMinutesSpinBox = QSpinBox(self.centralwidget)
        self.blockTimeMinutesSpinBox.setObjectName(u"blockTimeMinutesSpinBox")
        self.blockTimeMinutesSpinBox.setValue(70)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.blockTimeMinutesSpinBox)

        self.timeBetweenBlockLabel = QLabel(self.centralwidget)
        self.timeBetweenBlockLabel.setObjectName(u"timeBetweenBlockLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.timeBetweenBlockLabel)

        self.timeBetweenBlockSpinBox = QSpinBox(self.centralwidget)
        self.timeBetweenBlockSpinBox.setObjectName(u"timeBetweenBlockSpinBox")
        self.timeBetweenBlockSpinBox.setValue(10)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.timeBetweenBlockSpinBox)

        self.lunchStartLabel = QLabel(self.centralwidget)
        self.lunchStartLabel.setObjectName(u"lunchStartLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lunchStartLabel)

        self.lunchStartSpinBox = QSpinBox(self.centralwidget)
        self.lunchStartSpinBox.setObjectName(u"lunchStartSpinBox")
        self.lunchStartSpinBox.setMinimum(1)
        self.lunchStartSpinBox.setMaximum(10)
        self.lunchStartSpinBox.setValue(5)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lunchStartSpinBox)

        self.lunchTimeLabel = QLabel(self.centralwidget)
        self.lunchTimeLabel.setObjectName(u"lunchTimeLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lunchTimeLabel)

        self.lunchTimeSpinBox = QSpinBox(self.centralwidget)
        self.lunchTimeSpinBox.setObjectName(u"lunchTimeSpinBox")
        self.lunchTimeSpinBox.setMinimum(1)
        self.lunchTimeSpinBox.setMaximum(200)
        self.lunchTimeSpinBox.setValue(60)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lunchTimeSpinBox)

        self.dayStartLabel = QLabel(self.centralwidget)
        self.dayStartLabel.setObjectName(u"dayStartLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.dayStartLabel)

        self.dayStartTimeEdit = QTimeEdit(self.centralwidget)
        self.dayStartTimeEdit.setObjectName(u"dayStartTimeEdit")
        self.dayStartTimeEdit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(8, 15, 0)))
        self.dayStartTimeEdit.setMaximumTime(QTime(23, 59, 59))
        self.dayStartTimeEdit.setMinimumTime(QTime(0, 0, 0))
        self.dayStartTimeEdit.setCalendarPopup(False)
        self.dayStartTimeEdit.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.dayStartTimeEdit)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.line_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.filenameLabel = QLabel(self.centralwidget)
        self.filenameLabel.setObjectName(u"filenameLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.filenameLabel)

        self.scheduleLineEdit = QLineEdit(self.centralwidget)
        self.scheduleLineEdit.setObjectName(u"scheduleLineEdit")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.scheduleLineEdit)


        self.verticalLayout.addLayout(self.formLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 2)
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
        self.toolBar.addAction(self.action_gen)
        self.toolBar.addAction(self.actionExport)
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
        self.actionsaveas.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
#if QT_CONFIG(tooltip)
        self.actionsaveas.setToolTip(QCoreApplication.translate("MainWindow", u"Save to a .txt file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionsaveas.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
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
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Teacher", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Block", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Day", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Class name", None));
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
        self.colorComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Yellow", None))
        self.colorComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Brown", None))
        self.colorComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.colorComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Cyan", None))
        self.colorComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Green", None))
        self.colorComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Purple", None))
        self.colorComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gray", None))
        self.colorComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Orange", None))
        self.colorComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Pink", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Schedule settings", None))
        self.periodStartLabel.setText(QCoreApplication.translate("MainWindow", u"Period start", None))
        self.periodStartDateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yyyy", None))
        self.periodEndLabel.setText(QCoreApplication.translate("MainWindow", u"Period end", None))
        self.periodEndDateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yyyy", None))
        self.blockTimeMinutesLabel.setText(QCoreApplication.translate("MainWindow", u"Block time (minutes)", None))
        self.timeBetweenBlockLabel.setText(QCoreApplication.translate("MainWindow", u"Time between blocks (minutes)", None))
        self.lunchStartLabel.setText(QCoreApplication.translate("MainWindow", u"Lunch start block", None))
        self.lunchTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Lunch time (Minutes)", None))
        self.dayStartLabel.setText(QCoreApplication.translate("MainWindow", u"Day start", None))
        self.dayStartTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Export settings", None))
        self.filenameLabel.setText(QCoreApplication.translate("MainWindow", u"Calendar name", None))
        self.scheduleLineEdit.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

