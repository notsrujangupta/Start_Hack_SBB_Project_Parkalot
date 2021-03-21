# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 06:39:13 2021

@author: Srujan Gupta
"""
import pandas as pd
import numpy as np
folder = ##inisert folder here##
folder2 = ##insert folder here##

df = pd.read_csv(folder+"BurgdorfMeteor.csv")

app_sales = pd.read_csv(folder2+"Burgdorf App Sales 2021.csv")
other_sales = pd.read_csv(folder2+"Burgdorf Other Sales 2021.csv")
sales = pd.concat([app_sales,other_sales], axis = 0)

## make a dataframe with arrival times, giving them a +1  value to help us count the number of sold tickets filled at any given point in time
sales_val_in = pd.DataFrame(data = sales["start"])
sales_val_in["value"] = 1
sales_val_in = sales_val_in.rename(columns = {"start":"UNIX time"})

sales_val_out = pd.DataFrame(data = sales["end"])
sales_val_out["value"] = -1
sales_val_out = sales_val_out.rename(columns = {"end":"UNIX time"})

##concatenate the two dataframes to form the final dataframe that we can sum at various points in time to figure out number of tickets sold at those timestamps
sales_final = pd.concat([sales_val_in,sales_val_out])

##sorting data based on time to make it easier to work with
sales_final = sales_final.sort_values(by=['UNIX time'])

##creating a sumcheck column to use the sum later
sales_final["sumcheck"] = 0

## first row value
sales_final.iloc[0,2] = sales_final.iloc[0,1]

## future row values for sumcehck come from previous total vehicles (sumcheck previosu value) + new change (latest UNIX time arrival/departure)
for i in range(1,len(sales_final)):
    sales_final.iloc[i,2] = sales_final.iloc[i-1,2] + sales_final.iloc[i,1]

df["Sales"] = 0

for i in range(len(df)):
    df.iloc[i,4] = sales_final["sumcheck"][sales_final["UNIX time"]>df.iloc[i,0]].iloc[0]

df["Sales"] = df["Sales"].astype(int)
##Now we do all that with parking spots as well since that will be the dependent variable on UNIX timestamps, meteo data, and tickets sold.
spots = pd.read_csv(folder2+"burgdorf_clean.csv")

## this one already has the dataset in an appropriate format, we jsut need to append the column and attach values as needed.
df["Spots"] = 0

for i in range(len(df)):
    df.iloc[i,5] = spots["sumcheck"][spots["UNIX time"]>df.iloc[i,0]].iloc[0]

issue = df[["Sales","Spots"]].copy()
issue["Diff"] = issue["Sales"]-issue["Spots"]

len(issue["Diff"].where(issue["Diff"]<0).dropna())  #answer is 382. This means there were 382 hourly timestamps when there were more spots filled than shown sales at those points. This corroborates the idea that a nontrivial chunk of sales data is missing.

df.to_csv("model_dataset.csv",index = False)
