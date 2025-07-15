from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
import os
from dotenv import load_dotenv
import socketio

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mssql+pyodbc://username:password@server/database?driver=SQL+Server')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
sio = socketio.Server(async_mode='threading')
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

# Model tanımlamaları
class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), unique=True, nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), nullable=False)
    IsAdmin = db.Column(db.Boolean, default=False)
    
    def get_id(self):
        return str(self.UserID)

class Employee(db.Model):
    __tablename__ = 'Employees'
    EmployeeID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(100), nullable=False)
    LastName = db.Column(db.String(100), nullable=False)
    PhoneNumber = db.Column(db.String(20), unique=True, nullable=False)
    IMEI = db.Column(db.String(50), unique=True, nullable=False)
    ProgramSerialNo = db.Column(db.String(100), unique=True, nullable=False)
    IsActive = db.Column(db.Boolean, default=True)
    ContractDate = db.Column(db.DateTime, nullable=False)
    locations = db.relationship('LocationHistory', backref='employee', lazy=True)

class LocationHistory(db.Model):
    __tablename__ = 'LocationHistory'
    LocationID = db.Column(db.Integer, primary_key=True)
    EmployeeID = db.Column(db.Integer, db.ForeignKey('Employees.EmployeeID'), nullable=False)
    Latitude = db.Column(db.Float, nullable=False)
    Longitude = db.Column(db.Float, nullable=False)
    Accuracy = db.Column(db.Float)
    Speed = db.Column(db.Float)
    Timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Ana sayfa
@app.route('/')
@login_required
def index():
    return render_template('index.html')

# Çalışan listesi
@app.route('/employees')
@login_required
def employees():
    employees_list = Employee.query.all()
    return render_template('employees.html', employees=employees_list)

# Canlı konum takibi
@app.route('/live-tracking')
@login_required
def live_tracking():
    return render_template('live_tracking.html')

# Android uygulamasından gelen konum güncellemeleri için API
@app.route('/api/location', methods=['POST'])
def update_location():
    data = request.json
    try:
        location = LocationHistory(
            EmployeeID=data['employee_id'],
            Latitude=data['latitude'],
            Longitude=data['longitude'],
            Accuracy=data.get('accuracy'),
            Speed=data.get('speed')
        )
        db.session.add(location)
        db.session.commit()
        
        # Canlı takip için WebSocket ile konum bilgisini gönder
        sio.emit('location_update', {
            'employee_id': data['employee_id'],
            'latitude': data['latitude'],
            'longitude': data['longitude'],
            'timestamp': datetime.utcnow().isoformat()
        })
        
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# WebSocket olayları
@sio.event
def connect(sid, environ):
    print(f'Client connected: {sid}')

@sio.event
def disconnect(sid):
    print(f'Client disconnected: {sid}')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 