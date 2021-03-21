# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 02:50:32 2021

@author: Srujan Gupta
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import ks_2samp

    
# first we deal with sales data
folder = ##insert folder here##

df1 = pd.read_csv(folder+"Burgdorf App Sales 2021.csv")
df2 = pd.read_csv(folder+"Burgdorf Other Sales 2021.csv")

df = pd.concat([df1,df2],axis = 0)

## since we're checking for total ticket time from jan 1 2021 to feb 28 2021
df = df[df["start"] < 1614470400]
df = df[df["end"] > 1609459200]

df.loc[df["start"] < 1609459200, "start"] = 1609459200
df.loc[df["end"] > 1614470400, "end"] = 1614470400


df["gap"] = df["end"]-df["start"]
df["gap"] = df["gap"]/(3600*24)

df["gap"].describe()

# second we deal with data from parking spot usage
folder2 = ##insert folder here##

burgdorf = pd.read_csv(folder2+"parkrail-burgdorf.csv",sep=';')

burgdorf = burgdorf.iloc[:,2:4]

burgdorf = burgdorf.rename(columns={"Arrival in unix time": "start", "Departure in unix time": "end"})

burgdorf["gap"] = burgdorf["end"]-burgdorf["start"]

burgdorf = burgdorf[burgdorf["start"] < 1614470400]
burgdorf = burgdorf[burgdorf["end"] > 1609459200]

burgdorf.loc[burgdorf["start"] < 1609459200, "start"] = 1609459200
burgdorf.loc[burgdorf["end"] > 1614470400, "end"] = 1614470400


burgdorf["gap"] = burgdorf["end"]-burgdorf["start"]
burgdorf["gap"] = burgdorf["gap"]/(3600*24)

burgdorf["gap"].describe()

ser1 = burgdorf["gap"]
ser2 = df["gap"]

def normer(series):
    return (series-series.min())/(series.max()-series.min())

norm1 = normer(ser1)
norm2 = normer(ser2)

ks_2samp(norm1, norm2)

