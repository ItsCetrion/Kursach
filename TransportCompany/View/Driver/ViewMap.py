# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Map.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ViewMap(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ViewMap()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
