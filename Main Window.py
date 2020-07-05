import sys
from PyQt5.QtWidgets import QApplication
from function import functions

while True:
    app = QApplication(sys.argv)
    function = functions()
    app.exec()
    sys.exit()

