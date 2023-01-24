import requests
import msal
import json
username = 'dhananjay@cloudaeon.net'
password = 'LIfe@@787898'
app_id = '281b83c6-b759-489d-87cd-e2822aa80e6d'
tenant_id = '261b775f-255a-40b3-8b29-3bf762602e84'
authority_url = 'https://login.microsoftonline.com/' + tenant_id
scopes = ['https://analysis.windows.net/powerbi/api/.default']
client = msal.PublicClientApplication(app_id,authority = authority_url)
response = client.acquire_token_by_username_password(username=username , password=password , scopes=scopes)
# print(response)
# print(response.keys())
access_id = response.get('access_token')
endpoint = 'https://api.powerbi.com/v1.0/myorg/groups'
headers = {'Authorization' : f'Bearer '+ access_id}
print(headers)
response_request = requests.get(endpoint, headers=headers)
print(response_request.json())
print(response_request)
if response_request.status_code == 200:
    print(response_request.json())
    result = response_request.json()
    for item in result['value']:   
        print(item['name'])
else:
    print('failed')