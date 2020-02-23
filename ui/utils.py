import sys
from Qt import QtWidgets, QtCompat


class HelpWidget(QtWidgets.QApplication):
    def __init__(self, args):
        QtWidgets.QApplication.__init__(self,args)
        self.window = QtCompat.loadUi(uifile='ui/help.ui')

    def set_help_text(self, help_text='test'):
        help_text_and_link = '<a href=http://www.google.com>www.google.com</a>'
        #self.window.help.readOnly(False)
        self.window.help.setOpenExternalLinks(True)
        self.window.help.setText(help_text_and_link)
        #self.window.help.setText("");

    def show(self):
        self.window.show()
        sys.exit(self.exec_())


def show_help(help_text=''):
    app = HelpWidget(sys.argv)
    app.set_help_text(help_text)
    app.show()



if __name__ == '__main__':
    show_help('help text endlich los mach')
    