import requests
from twilio.rest import Client

latitude = 44.4268
longitude = 26.1025
api_key = "127a2e67bd50c169364f9fb514b50dcb"

account_sid = "AC6e1c6710d55de8518a8b22b484c234e9"
auth_token = "5ddfeb7ad2625450cb3e44b94936e7de"

api_endpoint_3hours5days = requests.get('https://api.openweathermap.org/data/2.5/forecast?lat=41.12&lon=16.86&cnt=4&appid=127a2e67bd50c169364f9fb514b50dcb')
api_endpoint_3hours5days.raise_for_status()
api_json = api_endpoint_3hours5days.json()
print(api_json)


will_rain = False
for i in range (0, 3):
    if str(api_json['list'][i]['weather'][0]['main']) in ["Rain", "Thunderstorm"]:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Rain today, bring an umbrella",
        from_='+12028662785',
        to='+---------'
    )
    print(message.sid)



