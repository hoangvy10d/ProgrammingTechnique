# Form implementation generated from reading ui file 'D:\HOANG VY\LAPTRINH\HK2\FINAL_PROJECT\MainwindowManagementManager.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 440)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 240, 246);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 561, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonBROWSER = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonBROWSER.setFont(font)
        self.pushButtonBROWSER.setStyleSheet("background-color: rgb(194, 237, 255);")
        self.pushButtonBROWSER.setObjectName("pushButtonBROWSER")
        self.gridLayout.addWidget(self.pushButtonBROWSER, 2, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 6, 1, 1)
        self.pushButtonVIP = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonVIP.setFont(font)
        self.pushButtonVIP.setStyleSheet("background-color: rgb(255, 198, 212);\n"
"\n"
"")
        self.pushButtonVIP.setObjectName("pushButtonVIP")
        self.gridLayout.addWidget(self.pushButtonVIP, 3, 3, 3, 3)
        self.lineEditSEARCHYEAR = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditSEARCHYEAR.setFont(font)
        self.lineEditSEARCHYEAR.setStyleSheet("background-color: rgb(255, 198, 212);")
        self.lineEditSEARCHYEAR.setObjectName("lineEditSEARCHYEAR")
        self.gridLayout.addWidget(self.lineEditSEARCHYEAR, 3, 1, 3, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.gridLayoutWidget)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 235, 240);\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tableWidget, 6, 2, 1, 5)
        self.pushButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/FINAL_PROJECT/z6349350049717_fe0d8f805ba3244a80b65aaae50fe960.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 1)
        self.pushButtonWRITEREVIEW = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonWRITEREVIEW.setFont(font)
        self.pushButtonWRITEREVIEW.setStyleSheet("background-color: rgb(194, 237, 255);")
        self.pushButtonWRITEREVIEW.setObjectName("pushButtonWRITEREVIEW")
        self.gridLayout.addWidget(self.pushButtonWRITEREVIEW, 2, 2, 1, 5)
        self.pushButton_CLOSE = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_CLOSE.setFont(font)
        self.pushButton_CLOSE.setStyleSheet("background-color: rgb(255, 198, 212);")
        self.pushButton_CLOSE.setObjectName("pushButton_CLOSE")
        self.gridLayout.addWidget(self.pushButton_CLOSE, 3, 6, 3, 1)
        self.lineEditNAME_MANAGER = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditNAME_MANAGER.setFont(font)
        self.lineEditNAME_MANAGER.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditNAME_MANAGER.setObjectName("lineEditNAME_MANAGER")
        self.gridLayout.addWidget(self.lineEditNAME_MANAGER, 0, 1, 1, 6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 198, 212);")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.lineEditSEARCHID = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditSEARCHID.setFont(font)
        self.lineEditSEARCHID.setStyleSheet("background-color: rgb(255, 198, 212);")
        self.lineEditSEARCHID.setObjectName("lineEditSEARCHID")
        self.gridLayout.addWidget(self.lineEditSEARCHID, 3, 0, 3, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(255, 235, 240);\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButtonSAVE = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonSAVE.setGeometry(QtCore.QRect(40, 260, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonSAVE.setFont(font)
        self.pushButtonSAVE.setStyleSheet("background-color: rgb(203, 235, 255);")
        self.pushButtonSAVE.setObjectName("pushButtonSAVE")
        self.pushButtonUPGRADEVIP = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonUPGRADEVIP.setGeometry(QtCore.QRect(160, 230, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonUPGRADEVIP.setFont(font)
        self.pushButtonUPGRADEVIP.setStyleSheet("background-color: rgb(203, 235, 255);")
        self.pushButtonUPGRADEVIP.setObjectName("pushButtonUPGRADEVIP")
        self.pushButtonDELETE = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonDELETE.setGeometry(QtCore.QRect(160, 260, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonDELETE.setFont(font)
        self.pushButtonDELETE.setStyleSheet("background-color: rgb(203, 235, 255);")
        self.pushButtonDELETE.setObjectName("pushButtonDELETE")
        self.lineEditUSERID = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditUSERID.setGeometry(QtCore.QRect(120, 30, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEditUSERID.setFont(font)
        self.lineEditUSERID.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditUSERID.setObjectName("lineEditUSERID")
        self.lineEditUSERNAME = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditUSERNAME.setGeometry(QtCore.QRect(120, 60, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEditUSERNAME.setFont(font)
        self.lineEditUSERNAME.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditUSERNAME.setObjectName("lineEditUSERNAME")
        self.lineEditPASSWORD = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditPASSWORD.setGeometry(QtCore.QRect(120, 90, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEditPASSWORD.setFont(font)
        self.lineEditPASSWORD.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditPASSWORD.setObjectName("lineEditPASSWORD")
        self.lineEditEMAIL = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditEMAIL.setGeometry(QtCore.QRect(120, 120, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEditEMAIL.setFont(font)
        self.lineEditEMAIL.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditEMAIL.setObjectName("lineEditEMAIL")
        self.lineEditSIGNUPDATE = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditSIGNUPDATE.setGeometry(QtCore.QRect(120, 150, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEditSIGNUPDATE.setFont(font)
        self.lineEditSIGNUPDATE.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditSIGNUPDATE.setObjectName("lineEditSIGNUPDATE")
        self.lineEditFANFIC = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditFANFIC.setGeometry(QtCore.QRect(120, 180, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEditFANFIC.setFont(font)
        self.lineEditFANFIC.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditFANFIC.setObjectName("lineEditFANFIC")
        self.pushButton_CLEARPASSWORD = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_CLEARPASSWORD.setGeometry(QtCore.QRect(40, 230, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_CLEARPASSWORD.setFont(font)
        self.pushButton_CLEARPASSWORD.setStyleSheet("background-color: rgb(203, 235, 255);")
        self.pushButton_CLEARPASSWORD.setObjectName("pushButton_CLEARPASSWORD")
        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 18))
        self.menubar.setObjectName("menubar")
        self.menuIMPORT = QtWidgets.QMenu(parent=self.menubar)
        self.menuIMPORT.setObjectName("menuIMPORT")
        self.menuIMPORT_2 = QtWidgets.QMenu(parent=self.menuIMPORT)
        self.menuIMPORT_2.setObjectName("menuIMPORT_2")
        self.menuEXPORT = QtWidgets.QMenu(parent=self.menuIMPORT)
        self.menuEXPORT.setObjectName("menuEXPORT")
        self.menuUS = QtWidgets.QMenu(parent=self.menubar)
        self.menuUS.setObjectName("menuUS")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMannual = QtGui.QAction(parent=MainWindow)
        self.actionMannual.setObjectName("actionMannual")
        self.actionABOUT = QtGui.QAction(parent=MainWindow)
        self.actionABOUT.setObjectName("actionABOUT")
        self.actionExcel_import = QtGui.QAction(parent=MainWindow)
        self.actionExcel_import.setObjectName("actionExcel_import")
        self.actionJson_import = QtGui.QAction(parent=MainWindow)
        self.actionJson_import.setObjectName("actionJson_import")
        self.actionJson_export = QtGui.QAction(parent=MainWindow)
        self.actionJson_export.setObjectName("actionJson_export")
        self.actionExcel_Export = QtGui.QAction(parent=MainWindow)
        self.actionExcel_Export.setObjectName("actionExcel_Export")
        self.menuIMPORT_2.addAction(self.actionExcel_import)
        self.menuIMPORT_2.addAction(self.actionJson_import)
        self.menuEXPORT.addAction(self.actionJson_export)
        self.menuEXPORT.addAction(self.actionExcel_Export)
        self.menuIMPORT.addAction(self.menuIMPORT_2.menuAction())
        self.menuIMPORT.addAction(self.menuEXPORT.menuAction())
        self.menuUS.addAction(self.actionMannual)
        self.menuUS.addAction(self.actionABOUT)
        self.menubar.addAction(self.menuIMPORT.menuAction())
        self.menubar.addAction(self.menuUS.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_CLOSE.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonBROWSER.setText(_translate("MainWindow", "BROWSER"))
        self.pushButtonVIP.setText(_translate("MainWindow", "VIP"))
        self.lineEditSEARCHYEAR.setText(_translate("MainWindow", "SEARCH YEAR"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "UserID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Signup Date"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fanfic number"))
        self.pushButtonWRITEREVIEW.setText(_translate("MainWindow", "WRITE REVIEW"))
        self.pushButton_CLOSE.setText(_translate("MainWindow", "CLOSE"))
        self.label.setText(_translate("MainWindow", "Manager\'s Name:"))
        self.lineEditSEARCHID.setText(_translate("MainWindow", "SEARCH ID"))
        self.groupBox.setTitle(_translate("MainWindow", "DETAILS"))
        self.label_2.setText(_translate("MainWindow", "User ID:"))
        self.label_3.setText(_translate("MainWindow", "User Name:"))
        self.label_4.setText(_translate("MainWindow", "Password:"))
        self.label_5.setText(_translate("MainWindow", "Email:"))
        self.label_6.setText(_translate("MainWindow", "Sign up date:"))
        self.label_8.setText(_translate("MainWindow", "FanFic Number:"))
        self.pushButtonSAVE.setText(_translate("MainWindow", "SAVE"))
        self.pushButtonUPGRADEVIP.setText(_translate("MainWindow", "UPGRADE VIP"))
        self.pushButtonDELETE.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_CLEARPASSWORD.setText(_translate("MainWindow", "CLEAR PASSWORD"))
        self.menuIMPORT.setTitle(_translate("MainWindow", "System"))
        self.menuIMPORT_2.setTitle(_translate("MainWindow", "IMPORT"))
        self.menuEXPORT.setTitle(_translate("MainWindow", "EXPORT"))
        self.menuUS.setTitle(_translate("MainWindow", "Us"))
        self.actionMannual.setText(_translate("MainWindow", "MANUAL"))
        self.actionABOUT.setText(_translate("MainWindow", "ABOUT"))
        self.actionExcel_import.setText(_translate("MainWindow", "Excel"))
        self.actionJson_import.setText(_translate("MainWindow", "Json file"))
        self.actionJson_export.setText(_translate("MainWindow", "Json"))
        self.actionExcel_Export.setText(_translate("MainWindow", "Excel"))
