# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:09:48 2020

@author: Hrisheekesh
"""

import pandas as pd
import numpy as np

def date_identifier(data_set):
#creating an list to store the column names
    column_names = []
    #iterating through all the columns in the dataset
    for column in data_set.columns:
        if data_set[column].dtype == 'object':
            try:
                #checking columns whether having date in it or not
                data_set[column] = pd.to_datetime(data_set[column])
                #if column contains date add to the list
                column_names.append(column)
            except ValueError:
                pass 
    for column in range(len(column_names)-1):
       # print("entered the loop")
        # creating new column names 
        a = 'Difference' + str(column)
        #calculating the difference in dates
        data_set[a] = (data_set[column_names[column]].sub(data_set[column_names[column + 1]], axis = 0))
        data_set[a] = data_set[a] / np.timedelta64(1, 'D')
        #adding new columns to the date set
        data_set.to_csv("dates.csv", index = False)
        #print (data_set)
    #iterating through all the columns in the dataset
    for column in data_set.columns:
        #deleting original date columns
        if column in column_names:
            del data_set[column]
    print(data_set)
    data_set.to_csv("sample.csv", index = False)
    print("Dataset has been modified successfully")
    return column_names
#considering the dataset is of csv format       
#loading the dataset Note: Please pass your dataset below by keeping both files in same directory
g = pd.read_csv("sample.csv")
date_identifier(g)
