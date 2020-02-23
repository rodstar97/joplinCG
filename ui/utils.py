import sys
from Qt import QtWidgets, QtCompat



def show_help(help_text=''):
    ui = QtCompat.loadUi(uifile='ui/help.ui')
    ui.help.setText(help_text)
    ui.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    helper = show_help('ahhha')
    app.exec_()
    