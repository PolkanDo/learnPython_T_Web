from flask import Flask
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    weather = weather_by_city('Moscow,Russia')
    if weather:
        return f'Weather: {weather["temp_C"]}, feels like {weather["FeelsLikeC"]}'
    else:
        return "Weather server is temporarily unavailable..."

if __name__ == "__main__":
    app.run(debug=True)