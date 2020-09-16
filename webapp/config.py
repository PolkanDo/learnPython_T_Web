from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = 'Moscow, Russia'
WEATHER_API_KEY = 'd54edec65f274a1ab16205718203108'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = "alskdjfiu34i025jw234dlfkjhLkgdfs84LIUG##$3yr39fsldhGOIUG"

REMEMBER_COOKIE_DURATION = timedelta(days=5)