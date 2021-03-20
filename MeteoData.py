import requests
import json
import urllib3
import os

global weather_response
global weather_url
token_url = "https://sso-int.sbb.ch/auth/realms/SBB_Public/protocol/openid-connect/token"
client_id = 'df3fa736'
client_secret = '15a45c13f35913d407d3a3faef9cda5e'
data = {'grant_type': 'client_credentials'}
access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))
tokens = json.loads(access_token_response.text)
api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}



''' Reference and documentation:
    
        https://www.meteomatics.com/en/api/getting-started/

'''
coordinates = '47.0607007264,7.62169447355' # Burgdorf co-ordinates
dateRange = '2021-01-01T00:00:00.000+05:30--2021-02-28T23:59:59.000+05:30:PT1H' # PT1H means for every hour
parameters = 't_2m:C,precip_1h:mm,fresh_snow_1h:cm' # Instant Temperature 2m above ground, in C
                                                    # Precipitation by hour, in mm
                                                    # Snowfall by hour, in cm

weather_url = f'https://weather-int.api.sbb.ch/' + dateRange + '/' + parameters + '/' + coordinates + '/csv'

print (weather_url)
weather_response = requests.get(weather_url,headers=api_call_headers )

f = open("Burgdorf.csv", "w")
f.write(weather_response.text)  #   Writing raw data retrieved from API in a file
f.close()


# Reading file with RAW Data
dfMeto = pd.read_csv('Burgdorf.csv', sep = ";")
dfMeto.columns = ['DateTime', 'Temperature per Hour', 'Precipitation per Hour', 'Snowfall Hourly']


# Changing Datetime to UNIX time
dfMeto["DateTime"] = pd.to_datetime(dfMeto["DateTime"])

for i in range(len(dfMeto)):
    dfMeto.iloc[i,0] = datetime.datetime.timestamp(dfMeto.iloc[i,0])

dfMeto.to_csv("BurgdorfMeteor.csv",index = False)


# np.where(pd.isnull(dfMeto)) # checked: no empty values
# dfMeto.head()
