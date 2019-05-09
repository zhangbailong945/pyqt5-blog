import os,sys
from PyQt5.QtWidgets import QApplication
from MyWidgets.Do_MainLayout import Do_MainLayout


if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Do_MainLayout()
    w.show()
    sys.exit(app.exec_())