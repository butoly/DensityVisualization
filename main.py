import sys
import os

from PyQt5 import QtWidgets

import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonOpenFile.clicked.connect(self.browse_folder)

    def browse_folder(self):
        self.textEdit.clear() # Чистим текстовое окно
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file') # Не знаю зачем нижнее подчеркивание, но в докухе так.

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
