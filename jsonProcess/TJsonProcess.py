import os
import PySide2.QtCore as QtCore
import numpy as np
import math


class TJsonProcess(QtCore.QObject):

    signal_update_time = QtCore.Signal(int)

    def __init__(self, folder_path):
        super().__init__()
        self.results = []
        self.tendency = []
        self.result = {}
        self.files = os.listdir(folder_path)

    def getTendency(self, tick, var):
        """ Get the tendency of a tick
            Args: tick a list of data
                n the size of judge
            Output: string
        """
        first_value = tick[0]
        upper = down = 0
        tick_var = np.var(tick)
        for i in range(len(tick)):
            if tick[i] < first_value:
                down += 1
            elif first_value < tick[i]:
                upper += 1
        if tick_var <= var:
            return 'stable'
        elif 3 <= down:
            return 'down'
        elif 3 <= upper:
            return 'upper'
        else:
            return 'stable'