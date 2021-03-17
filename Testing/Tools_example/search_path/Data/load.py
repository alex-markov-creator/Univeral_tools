#-*- coding: utf-8 -*-
"""
load.py - file load pandas.DataFrame objects
"""
import pandas as pd
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

filepath = parentdir+r'/Data/csv/file.csv'

val_1 =  pd.read_csv(filepath)


print(val_1)


