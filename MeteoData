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


weather_url = f'https://weather-int.api.sbb.ch/2021-01-01T00:00:00.000+05:30--2021-02-28T23:59:59.000+05:30:PT1H/t_2m:C,precip_1h:mm/47.0607007264,7.62169447355/csv'
# https://weather-int.api.sbb.ch/2021-02-15T00:00:00Z--2021-03-4T00:00:00Z:PT1H/fresh_snow_6h:cm,fresh_snow_1h:cm/46.50389,8.30325/csv
print (weather_url)
weather_response = requests.get(weather_url,headers=api_call_headers )
# print(weather_response.text)
