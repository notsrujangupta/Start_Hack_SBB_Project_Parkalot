# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:49:45 2021

@author: Srujan Gupta
"""
import pandas as pd

folder = ##insert folder here##
burgdorf = pd.read_csv(folder+"parkrail-burgdorf.csv",sep=';')

## checking for null values
is_NaN = burgdorf.isnull()
row_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = burgdorf[row_has_NaN]
rows_with_NaN.shape ##the answer is (7,6)
## all NaN values belong in the Departure section, which means that at the end of the dataset, some vehicles had not left their respective parking spots.

## make a dataframe with arrival times, giving them a +1  value to help us count the number of spots filled at any given point in time
burgdorf_in = pd.DataFrame()
burgdorf_in = pd.concat([burgdorf_in,burgdorf.iloc[:,2]],axis = 1)
burgdorf_in["value"] = 1
burgdorf_in = burgdorf_in.rename(columns={"Arrival in unix time": "UNIX time"})

## make a dataframe with arrival times, giving them a -1  value to help us count the number of spots filled at any given point in time
burgdorf_out = pd.DataFrame()
burgdorf_out = pd.concat([burgdorf_out,burgdorf.iloc[:,3]],axis = 1)
burgdorf_out["value"] = -1
burgdorf_out = burgdorf_out.rename(columns={"Departure in unix time": "UNIX time"})

##concatenate the two dataframes to form the final dataframe that we can sum at various points in time to figure out number of full spots at those timestamps
burgdorf_final = pd.concat([burgdorf_in,burgdorf_out])

##sorting data based on time to make it easier to work with
burgdorf_final = burgdorf_final.sort_values(by=['UNIX time'])

##creating a sumcheck column to make sure that the sum is, at no point, less than 0 (so that we can safely assume that the data started with 0 vehicles in the parking lot)
burgdorf_final["sumcheck"] = 0

## first row value
burgdorf_final.iloc[0,2] = burgdorf_final.iloc[0,1]

## future row values for sumcehck come from previous total vehicles (sumcheck previosu value) + new change (latest UNIX time arrival/departure)
for i in range(1,len(burgdorf_final)):
    burgdorf_final.iloc[i,2] = burgdorf_final.iloc[i-1,2] + burgdorf_final.iloc[i,1]
    
## removing all null values since they were in Departures, unnecessarily potentially messing with our dataset
burgdorf_final.dropna(inplace = True)

##converting everything ot integers
burgdorf_final = burgdorf_final.astype(int)

## checking if sum is always nonnegative
sumseries = burgdorf_final["sumcheck"].copy()
sum(n < 0 for n in sumseries.values.flatten()) == 0 ##The answer was true. This confirms it upto reasonable lack of doubt that the dataset is clean enough for us to work with.
## checking max concurrent vehicles in the parking lot
max(burgdorf_final["sumcheck"]) ##The answer is 80. This is very reasonable for a parking lot with a total of 155 parking spaces.

##creating a csv file with burgdorf information
burgdorf_final.to_csv("burgdorf_clean.csv",index = False)
