import sys
import os

from PyQt5 import QtWidgets
import numpy as np
import mayavi.mlab as mlab
import design

readFlag = False # Флаг для проверки считали ли файл или нет
data = ""        # Данные которые мы считываем

class ExampleApp(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonOpenFile.clicked.connect(self.browse_folder)
        self.solve.clicked.connect(self.vizualization)
    
    def browse_folder(self):

        global readFlag
        global data
        
        self.textEdit.clear()
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')

        readFlag = False
        if fname != "":
            readFlag = True
            #Чтение исходных данных
            data = np.load(fname)
            self.textEdit.setText(str(data))
        else:
            readFlag = False
            
    def vizualization(self):

        global readFlag
        global data
        
        if readFlag == True:
            mlab.contour3d(data, transparent = True, contours = 7)
        else:
            self.textEdit.setText("Данные не считаны")
            
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    mlab.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
