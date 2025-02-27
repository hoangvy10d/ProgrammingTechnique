from PyQt6.QtWidgets import QApplication, QMainWindow

from DoAnNhomCK.Panh.ui.ManagerRemoveExt import ManagerRemoveExt

app=QApplication([])
mainwindow=QMainWindow()
myui=ManagerRemoveExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()