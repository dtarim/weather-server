from flask import Flask, request, render_template

app = Flask(__name__)
weather_data = {}

@app.route('/update_weather', methods=['POST'])
def update_weather():
    global weather_data
    weather_data = request.json
    return "Weather data updated successfully", 200

@app.route('/')
def home():
    return render_template('home.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
