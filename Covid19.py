# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:55:27 2020

@author: Kuldeep Singh Shekhawat'

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import numpy as np


df=pd.read_csv("covid_19_india.csv",parse_dates=["Date"],dayfirst=True)
df.head()



