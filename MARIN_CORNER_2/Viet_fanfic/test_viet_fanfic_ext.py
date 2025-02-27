from PyQt6.QtWidgets import QMainWindow, QApplication

from Group_Project.Viet_fanfic_ext import Viet_fanfic_ext

app=QApplication([])
Mainwindow=QMainWindow()
myui=Viet_fanfic_ext()
myui.setupUi(Mainwindow)
myui.showWindow()
app.exec()