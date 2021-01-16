import requests

api_key = 'acd4a9d43c6892795dac4f3df613261a'
base_url = 'http://api.openweathermap.org/data/2.5/weather'
city = input('Enter city name ')


def get_data(url, params):
    return requests.get(url, params).json()


data = get_data(base_url, {"q": city, "appid": api_key})


def get_forecast(data):
    in_celsius = float(data['main']['temp'])-273.15
    in_celsius = "%.1f" % in_celsius
    temperature = float(in_celsius)
    print(temperature)
    if temperature < 0:
        return "Cold outside! Please wear warm clothes"
    elif temperature > 30:
        return "Very hot! Stay in the shadow"
    else:
        return "Nice weather outside, have a nice day"


print(get_forecast(data))
