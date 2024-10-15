from flask import Blueprint, request, jsonify
from models import db, Sensor, WeatherData, Alert

api = Blueprint('api', __name__)

@api.route('/sensors', methods=['GET', 'POST'])
def manage_sensors():
    if request.method == 'GET':
        sensors = Sensor.query.all()
        return jsonify([s.__dict__ for s in sensors])
    
    if request.method == 'POST':
        data = request.get_json()
        new_sensor = Sensor(**data)
        db.session.add(new_sensor)
        db.session.commit()
        return jsonify(new_sensor.__dict__), 201

@api.route('/sensors/<int:sensor_id>', methods=['GET', 'PUT', 'DELETE'])
def sensor_details(sensor_id):
    sensor = Sensor.query.get_or_404(sensor_id)

    if request.method == 'GET':
        return jsonify(sensor.__dict__)
    
    if request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            setattr(sensor, key, value)
        db.session.commit()
        return jsonify(sensor.__dict__)
    
    if request.method == 'DELETE':
        db.session.delete(sensor)
        db.session.commit()
        return '', 204

@api.route('/sensors/<int:sensor_id>/data', methods=['GET', 'POST'])
def manage_data(sensor_id):
    if request.method == 'GET':
        data = WeatherData.query.filter_by(sensor_id=sensor_id).all()
        return jsonify([d.__dict__ for d in data])
    
    if request.method == 'POST':
        data = request.get_json()
        new_data = WeatherData(sensor_id=sensor_id, **data)
        db.session.add(new_data)
        db.session.commit()
        return jsonify(new_data.__dict__), 201

@api.route('/sensors/<int:sensor_id>/alerts', methods=['GET', 'POST'])
def manage_alerts(sensor_id):
    if request.method == 'GET':
        alerts = Alert.query.filter_by(sensor_id=sensor_id).all()
        return jsonify([a.__dict__ for a in alerts])
    
    if request.method == 'POST':
        data = request.get_json()
        new_alert = Alert(sensor_id=sensor_id, **data)
        db.session.add(new_alert)
        db.session.commit()
        return jsonify(new_alert.__dict__), 201
