import pyowm

def get_weather_data(location):

    owm = pyowm.OWM("e62967467e7a6728ba24f74263389563")

    observation = owm.weather_at_place(location +', uk')

    w = observation.get_weather()

    weather = {'weather_Status':(w.get_status()), 'weather_Temperature':(w.get_temperature('celsius'))['temp'],
           'weather_Wind':w.get_wind()['speed']}

    print (weather['weather_Status'])
    return weather