# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:36:44 2019

@author: Tanmay
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

data = pd.read_csv("crime.csv", encoding = 'latin-1')
data = data.loc[data['YEAR'].isin([2016,2017])]
data = data.loc[data['UCR_PART'] == 'Part One']
data = data.drop(['INCIDENT_NUMBER','OFFENSE_CODE','UCR_PART','Location'], axis=1)

data['OCCURRED_ON_DATE'] = pd.to_datetime(data['OCCURRED_ON_DATE'])
data.SHOOTING.fillna('N', inplace=True)
data.DAY_OF_WEEK = pd.Categorical(data.DAY_OF_WEEK, 
              categories=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
              ordered=True)
