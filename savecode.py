import sys
# pip install pyqt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
from gui_1 import Ui_Form
from gui_2 import Ui_MainWindow1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.on_off = False
        self.uic2 = None
        self.sub_win_1 = None
        self.uic.Button_1.clicked.connect(self.show_screen)

    def show_screen(self):
        # # an di man hinh chinh dau tien
        # self.hide()

        # # hien man hinh phu 1 ui_form
        # self.sub_win = QMainWindow()
        # self.uic1 = Ui_Form()
        # self.uic1.setupUi(self.sub_win)
        # self.sub_win.show()

        # hien man hinh phu 2 Ui_MainWindow1
        # self.sub_win_1 = QMainWindow()
        self.uic2 = Ui_MainWindow1()
        self.uic2.setupUi(self)
        # self.sub_win_1.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return and self.on_off == False:
            print("ok")
            self.show_screen()
            self.on_off = True

        elif event.key() == Qt.Key_Return and self.on_off == True:
            print("work")
            self.on_off = False
            self.uic = Ui_MainWindow()
            self.uic.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
