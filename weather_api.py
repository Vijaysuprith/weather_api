from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
api_key = "22cead8305fc63538df1cc9bb40b3447"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    weather_data = get_weather_data(city)
    return jsonify(weather_data)

def get_weather_data(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract relevant information from the API response
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        return {'error': f'Error fetching data from OpenWeatherMap: {str(e)}'}

if __name__ == '__main__':
    app.run(debug=True)
