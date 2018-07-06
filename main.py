import sys
import os


from PyQt5 import QtWidgets
import numpy as np

import design



class ExampleApp(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonOpenFile.clicked.connect(self.browse_folder)

    def browse_folder(self):
        self.textEdit.clear() 
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')

        #Вывод исходных данных
        #f = open(fname, 'r')
        data = str(np.load(fname))
        self.textEdit.setText(data)

    #def vizualization(self):
        

        

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
