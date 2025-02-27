from MARIN_CORNER_2.Viet_fanfic.Viet_fanfic import Ui_MainWindow


class Viet_fanfic_ext(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        pass


