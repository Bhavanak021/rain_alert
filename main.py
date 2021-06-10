from twilio.rest import Client
from token import api_key, own_Endpoint, auth_token, account_sid, FROM, TO
import requests
MY_LAT = 25.347799  # Your latitude
MY_LONG = 86.982430  # Your longitude

weather_parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "exclude": "current,minutely,daily",
        "appid": api_key,
    }

will_rain = False
response = requests.get(own_Endpoint, params=weather_parameters)
response.raise_for_status()
for i in range(0, 12):
    data = response.json()["hourly"][:12][i]["weather"][0]["id"]
    if int(data) <= 700:
        will_rain = True
        # print(data)

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella.",
        from_=FROM,
        to=TO
    )

    print(message.status)