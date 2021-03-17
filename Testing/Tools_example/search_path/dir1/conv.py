#-*- coding: utf-8 -*-
"""
conv.py - file converter DataFrame objects
"""
import sys
import os
import time
sys.path.append(os.path.realpath('..'))
# субродительский каталог в sys.path

import pandas as pd
from tabulate import tabulate
from Data import val_1


data = val_1

class New:
    def __init__(self, data: pd.DataFrame):
        """

        """
        self.data = data
    def __str__(self):
        return tabulate(self.data, headers = 'keys', tablefmt = 'psql')

if __name__=='__main__':
    print(sys.path)
    x= New(data)
    print(x)
