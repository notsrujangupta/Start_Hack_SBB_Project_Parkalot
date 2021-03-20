# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:01:34 2021

@author: Srujan Gupta
"""
import pandas as pd
import datetime

pd.options.mode.chained_assignment = None  # default='warn'


folder = "C:/Users/Srujan Gupta/Desktop/Start Hack/"

##since the data in "parkrail-sale-app-history.csv" and "parkrail-sale-app-2018" is all from before 2021, but the data found in "parkrail-burgdorf" all begins from January 1 2021, and because we intend to use UNIX time as one of our factors for judging the expected value for the full parking spots, (extrapolating data from Burgdorf's spots filled data in "parkrail-burgdorf.csv"), we will not be using them. For the purposes of this project, we will only use data from January 1 2021 in "parkrail-sale-app.csv" and "parkrail-sale-backend.csv".
sale_app = pd.read_csv(folder+"parkrail-sale-app.csv",sep=';')
sale_other = pd.read_csv(folder+"parkrail-sale-backend.csv",sep = ';')

print(sale_app.columns)

print(sale_other.columns)

sale_app = sale_app[["start","end","facility_name"]]

burgdorf_app = sale_app[sale_app["facility_name"]=="Burgdorf"]
burgdorf_app.drop(["facility_name"],axis = 1, inplace = True)


burgdorf_app["start"] = pd.to_datetime(burgdorf_app["start"])
burgdorf_app["end"] = pd.to_datetime(burgdorf_app["end"])

for i in range(len(burgdorf_app)):
    burgdorf_app.iloc[i,0] = datetime.datetime.timestamp(burgdorf_app.iloc[i,0])
    burgdorf_app.iloc[i,1] = datetime.datetime.timestamp(burgdorf_app.iloc[i,1])
    
sale_other = sale_other[["start","end","didok_id"]]

burgdorf_other = sale_other[sale_other["didok_id"]==8005]
burgdorf_other.drop(["didok_id"],axis = 1, inplace = True)

burgdorf_other["start"] = pd.to_datetime(burgdorf_other["start"])
burgdorf_other["end"] = pd.to_datetime(burgdorf_other["end"])

for i in range(len(burgdorf_other)):
    burgdorf_other.iloc[i,0] = datetime.datetime.timestamp(burgdorf_other.iloc[i,0])
    burgdorf_other.iloc[i,1] = datetime.datetime.timestamp(burgdorf_other.iloc[i,1])

app = burgdorf_app.loc[burgdorf_app["start"] >= 1609459200]
app = app.loc[app["end"] >= 1609459200]

other = burgdorf_other.loc[burgdorf_other["start"] >= 1609459200]
other = other.loc[other["start"] >= 1609459200]

app.to_csv("Burgdorf App Sales 2021.csv",index = False)
other.to_csv("Burgdorf Other Sales 2021.csv",index = False)
burgdorf_app.to_csv("Burgdorf App Sales Total.csv",index = False)
burgdorf_other.to_csv("Burgdorf Other Sales Total.csv",index = False)