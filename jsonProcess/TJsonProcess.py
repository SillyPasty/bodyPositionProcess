import os
import PySide2.QtCore as QtCore
import numpy as np
import math
from dataBase.hisInfoDb import HisInfoDb


class TJsonProcess(QtCore.QObject):

    signal_update_time = QtCore.Signal(int)
    hisInfo = HisInfoDb()

    def __init__(self, folder_path):
        super().__init__()
        self.results = []
        self.tendency = []
        self.result = {}
        self.files = os.listdir(folder_path)
