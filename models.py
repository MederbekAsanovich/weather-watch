from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    installation_date = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='active')

    data = db.relationship('WeatherData', backref='sensor', lazy=True)
    alerts = db.relationship('Alert', backref='sensor', lazy=True)

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    wind_speed = db.Column(db.Float)
    timestamp = db.Column(db.String(50), nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.String(50), nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)
