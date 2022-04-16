import sys
# pip install pyqt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
from gui_2 import Ui_MainWindow1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.Button_1.clicked.connect(self.show_second_gui)
        self.on = False

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return and self.on == False:
            print("ok")
            self.show_second_gui()
            self.on = True
        elif event.key() == Qt.Key_Return and self.on == True:
            print("work")
            self.show_first_gui()
            self.on = False

    def show_second_gui(self):
        self.uic = Ui_MainWindow1()
        self.uic.setupUi(self)

    def show_first_gui(self):
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
