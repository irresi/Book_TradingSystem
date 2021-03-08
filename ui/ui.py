from kiwoom.kiwoom import *

import sys
from PyQt5.QtWidgets import *


class Ui_class():
    def __init__(self):
        print("UI 클래스 입니다.")
        self.app = QApplication(sys.argv) # 파이썬 경로

        self.kiwoom = Kiwoom()

        self.app.exec_()