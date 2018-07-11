import sys
import os

from PyQt5 import QtWidgets
import numpy as np
import mayavi.mlab as mlab

import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonOpenFile.clicked.connect(self.browse_folder)
        self.solve.clicked.connect(self.vizualization)

    def browse_folder(self):
        self.textEdit.clear() 
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')

        #Вывод исходных данных
        #f = open(fname, 'r')
        data = str(np.load(fname))
        self.textEdit.setText(data)

    def vizualization(self):
        x, y ,z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
        s = x + y + z
        #index = [[[10,10,10]]]
        #new_s = np.delete(s, index)
        #s = np.sin(x*y*z)/(x*y*z)
        #print(s)
        mlab.pipeline.volume(mlab.pipeline.scalar_field(s), color = (0,1,1))
        #mlab.contour3d(s)
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    mlab.show()
    app.exec_()
    

if __name__ == '__main__':
    main()
