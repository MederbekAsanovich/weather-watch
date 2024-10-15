# WeatherWatch API

WeatherWatch is a RESTful API for monitoring and managing weather data from various sensors. This API allows meteorologists and researchers to analyze weather patterns and trends effectively.

## Features

- Manage weather sensors (Create, Read, Update, Delete)
- Record and retrieve weather data (temperature, humidity, wind speed)
- Manage alerts for extreme weather conditions
- Basic authentication using JWT

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-RESTful
- Flask-JWT-Extended

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/weather_watch.git
   cd weather_watch

2. Create and activate a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate

3. Install the dependencies:

pip install -r requirements.txt

4. Set up the database:
    
    python app.py

Usage

Start the Flask server:

```bash
python app.py


The API will be available at http://127.0.0.1:5000/api/v1.

Endpoints
GET /api/v1/sensors - Retrieve a list of all sensors
POST /api/v1/sensors - Create a new sensor
GET /api/v1/sensors/{id} - Retrieve a specific sensor
PUT /api/v1/sensors/{id} - Update a specific sensor
DELETE /api/v1/sensors/{id} - Delete a specific sensor
GET /api/v1/sensors/{id}/data - Retrieve data for a specific sensor
POST /api/v1/sensors/{id}/data - Add weather data for a specific sensor
GET /api/v1/sensors/{id}/alerts - Retrieve alerts for a specific sensor
POST /api/v1/sensors/{id}/alerts - Create a new alert for a specific sensor

Authentication
The API uses JWT for authentication. You will need to implement the login endpoint to receive a token for protected routes.


