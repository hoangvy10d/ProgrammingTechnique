# Form implementation generated from reading ui file 'D:\NetworkAutomatic\HK 2 - KTLT - K24411E\Group_Project\Viet_fanfic.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 734)
        MainWindow.setStyleSheet("background-color: rgb(250, 232, 237);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 400, 851, 271))
        self.groupBox.setStyleSheet("background-color: rgb(203, 235, 255);\n"
"\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout_2.setHorizontalSpacing(12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_Character = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_Character.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_Character.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_Character.setObjectName("lineEdit_Character")
        self.gridLayout.addWidget(self.lineEdit_Character, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_Author = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_Author.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_Author.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_Author.setObjectName("lineEdit_Author")
        self.gridLayout.addWidget(self.lineEdit_Author, 3, 1, 1, 1)
        self.lineEdit_Title = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_Title.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_Title.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_Title.setObjectName("lineEdit_Title")
        self.gridLayout.addWidget(self.lineEdit_Title, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.lineEdit_LinkFilm = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_LinkFilm.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_LinkFilm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_LinkFilm.setObjectName("lineEdit_LinkFilm")
        self.gridLayout.addWidget(self.lineEdit_LinkFilm, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineEdit_Date = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_Date.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_Date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_Date.setObjectName("lineEdit_Date")
        self.gridLayout.addWidget(self.lineEdit_Date, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.groupBox_function = QtWidgets.QGroupBox(parent=self.groupBox)
        self.groupBox_function.setTitle("")
        self.groupBox_function.setObjectName("groupBox_function")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_function)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_Post = QtWidgets.QPushButton(parent=self.groupBox_function)
        self.pushButton_Post.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Post.setFont(font)
        self.pushButton_Post.setStyleSheet("background-color: rgb(255, 162, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Post.setObjectName("pushButton_Post")
        self.verticalLayout_3.addWidget(self.pushButton_Post)
        self.pushButton_Save = QtWidgets.QPushButton(parent=self.groupBox_function)
        self.pushButton_Save.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Save.setFont(font)
        self.pushButton_Save.setStyleSheet("background-color: rgb(255, 162, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.verticalLayout_3.addWidget(self.pushButton_Save)
        self.pushButton_Back = QtWidgets.QPushButton(parent=self.groupBox_function)
        self.pushButton_Back.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Back.setFont(font)
        self.pushButton_Back.setStyleSheet("background-color: rgb(255, 162, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.verticalLayout_3.addWidget(self.pushButton_Back)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout_2.addWidget(self.groupBox_function, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.groupBox_history = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_history.setGeometry(QtCore.QRect(620, 10, 251, 361))
        self.groupBox_history.setStyleSheet("background-color: rgb(203, 235, 255);")
        self.groupBox_history.setTitle("")
        self.groupBox_history.setObjectName("groupBox_history")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_history)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_Search = QtWidgets.QLineEdit(parent=self.groupBox_history)
        self.lineEdit_Search.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_Search.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.PreventContextMenu)
        self.lineEdit_Search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_Search.setInputMask("")
        self.lineEdit_Search.setFrame(True)
        self.lineEdit_Search.setCursorPosition(0)
        self.lineEdit_Search.setObjectName("lineEdit_Search")
        self.horizontalLayout.addWidget(self.lineEdit_Search)
        self.pushButton_Search = QtWidgets.QPushButton(parent=self.groupBox_history)
        self.pushButton_Search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\NetworkAutomatic\\HK 2 - KTLT - K24411E\\Group_Project\\search_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Search.setIcon(icon)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.horizontalLayout.addWidget(self.pushButton_Search)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Qlistview_da_viet = QtWidgets.QListView(parent=self.groupBox_history)
        self.Qlistview_da_viet.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Qlistview_da_viet.setObjectName("Qlistview_da_viet")
        self.verticalLayout.addWidget(self.Qlistview_da_viet)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.groupBox_write_script = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_write_script.setGeometry(QtCore.QRect(20, 10, 571, 361))
        self.groupBox_write_script.setStyleSheet("background-color: rgb(255, 178, 197);")
        self.groupBox_write_script.setTitle("")
        self.groupBox_write_script.setObjectName("groupBox_write_script")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_write_script)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit = QtWidgets.QTextEdit(parent=self.groupBox_write_script)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_write_script)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 178, 197);")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Date Released:"))
        self.label_3.setText(_translate("MainWindow", "Characters:"))
        self.label_5.setText(_translate("MainWindow", "Author:"))
        self.label_6.setText(_translate("MainWindow", "Link Film:"))
        self.label_8.setText(_translate("MainWindow", "Title:"))
        self.pushButton_Post.setText(_translate("MainWindow", "Post"))
        self.pushButton_Save.setText(_translate("MainWindow", "Save"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        self.lineEdit_Search.setPlaceholderText(_translate("MainWindow", "Search "))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">WRITE YOUR SCRIPT</span></p></body></html>"))
