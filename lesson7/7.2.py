


def make_country(name, capital, **kwargs):
    country = {}
    country['name'] = name
    country['capital'] = capital
    for key, value in kwargs.items():
        country[key] = value
    return country

print(make_country('Ukraine', 'Kyiv'))