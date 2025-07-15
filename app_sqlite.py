from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'demo-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gps_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Basit model tanımlamaları
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    imei = db.Column(db.String(50), unique=True, nullable=False)
    program_serial_no = db.Column(db.String(100), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class LocationHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    accuracy = db.Column(db.Float)
    speed = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    employee = db.relationship('Employee', backref='locations')

# Ana sayfa
@app.route('/')
def index():
    employees = Employee.query.all()
    return f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>GPS Takip Sistemi</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
            .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
            .nav {{ margin: 20px 0; }}
            .nav a {{ background: #3498db; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin-right: 10px; }}
            .nav a:hover {{ background: #2980b9; }}
            .stats {{ background: #ecf0f1; padding: 15px; border-radius: 5px; margin: 20px 0; }}
            .employee {{ background: #fff; border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }}
            .success {{ color: #27ae60; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 GPS Takip Sistemi</h1>
            
            <div class="nav">
                <a href="/employees">👥 Çalışanlar</a>
                <a href="/map">🗺️ Canlı Harita</a>
                <a href="/demo-data">➕ Demo Veri Ekle</a>
            </div>
            
            <div class="stats">
                <h3>📊 Sistem Durumu</h3>
                <p><strong>Toplam Çalışan:</strong> {len(employees)}</p>
                <p><strong>Sistem:</strong> <span class="success">✅ Çalışıyor</span></p>
                <p><strong>Veritabanı:</strong> <span class="success">✅ SQLite Bağlı</span></p>
            </div>
            
            <h3>Son Eklenen Çalışanlar</h3>
            {f'<div class="employee">Henüz çalışan eklenmemiş. <a href="/demo-data">Demo veri ekle</a></div>' if len(employees) == 0 else ''}
            {''.join([f'<div class="employee"><strong>{e.first_name} {e.last_name}</strong><br>📱 {e.phone_number}<br>📟 IMEI: {e.imei}</div>' for e in employees[:5]])}
            
            <hr style="margin: 30px 0;">
            <p><small>🔧 Sistem SQLite ile çalışıyor | Debug Mode: ON</small></p>
        </div>
    </body>
    </html>
    """

# Çalışan listesi
@app.route('/employees')
def employees():
    employees_list = Employee.query.all()
    return f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>Çalışanlar - GPS Takip</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
            .container {{ max-width: 900px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
            .nav {{ margin: 20px 0; }}
            .nav a {{ background: #3498db; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin-right: 10px; }}
            .nav a:hover {{ background: #2980b9; }}
            .employee-card {{ background: #fff; border: 1px solid #ddd; padding: 20px; margin: 15px 0; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
            .employee-card h3 {{ margin: 0 0 10px 0; color: #2c3e50; }}
            .info {{ color: #7f8c8d; margin: 5px 0; }}
            .status {{ background: #27ae60; color: white; padding: 3px 8px; border-radius: 3px; font-size: 12px; }}
            .no-employees {{ text-align: center; color: #7f8c8d; padding: 40px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>👥 Çalışanlar</h1>
            
            <div class="nav">
                <a href="/">🏠 Ana Sayfa</a>
                <a href="/demo-data">➕ Demo Veri Ekle</a>
            </div>
            
            <p><strong>Toplam Çalışan:</strong> {len(employees_list)}</p>
            
            {f'<div class="no-employees"><h3>Henüz çalışan yok</h3><p><a href="/demo-data">Demo veri ekleyerek başlayın</a></p></div>' if len(employees_list) == 0 else ''}
            
            {''.join([f'''
            <div class="employee-card">
                <h3>{e.first_name} {e.last_name} <span class="status">{'Aktif' if e.is_active else 'Pasif'}</span></h3>
                <div class="info">📱 Telefon: {e.phone_number}</div>
                <div class="info">📟 IMEI: {e.imei}</div>
                <div class="info">🔢 Program Seri No: {e.program_serial_no}</div>
                <div class="info">📅 Kayıt Tarihi: {e.created_at.strftime('%d.%m.%Y %H:%M') if e.created_at else 'Bilinmiyor'}</div>
                <div class="info">📍 Konum Sayısı: {len(e.locations)} kayıt</div>
            </div>
            ''' for e in employees_list])}
            
        </div>
    </body>
    </html>
    """

# Google Maps harita sayfası
@app.route('/map')
def map_page():
    return render_template('map.html')

# API: Mevcut konumları getir
@app.route('/api/locations')
def get_locations():
    # Her çalışan için en son konum kaydını getir
    subquery = db.session.query(
        LocationHistory.employee_id,
        db.func.max(LocationHistory.timestamp).label('max_timestamp')
    ).group_by(LocationHistory.employee_id).subquery()
    
    latest_locations = db.session.query(LocationHistory, Employee).join(
        Employee, LocationHistory.employee_id == Employee.id
    ).join(
        subquery,
        (LocationHistory.employee_id == subquery.c.employee_id) &
        (LocationHistory.timestamp == subquery.c.max_timestamp)
    ).all()
    
    locations = []
    for loc_history, employee in latest_locations:
        locations.append({
            'employee_id': employee.id,
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'phone': employee.phone_number,
            'imei': employee.imei,
            'latitude': float(loc_history.latitude),
            'longitude': float(loc_history.longitude),
            'accuracy': float(loc_history.accuracy) if loc_history.accuracy else None,
            'speed': float(loc_history.speed) if loc_history.speed else 0,
            'timestamp': loc_history.timestamp.isoformat()
        })
    
    return jsonify(locations)

# Demo veri ekleme
@app.route('/demo-data')
def add_demo_data():
    try:
        # Çalışan ekle
        emp = Employee(
            first_name="Ahmet",
            last_name="Yılmaz", 
            phone_number="05551234567",
            imei="123456789012345",
            program_serial_no="GPS001"
        )
        db.session.add(emp)
        db.session.commit()
        
        # Konum ekle
        loc = LocationHistory(
            employee_id=emp.id,
            latitude=39.9334,
            longitude=32.8597,
            accuracy=10.0,
            speed=0.0
        )
        db.session.add(loc)
        db.session.commit()
        
        return f"""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <title>Demo Veri Eklendi</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
                .container {{ max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center; }}
                .success {{ color: #27ae60; font-size: 24px; margin-bottom: 20px; }}
                .nav a {{ background: #3498db; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; margin: 10px; display: inline-block; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="success">✅ Demo veri başarıyla eklendi!</div>
                <p>Örnek çalışan ve konum bilgileri sisteme kaydedildi.</p>
                <div class="nav">
                    <a href="/">🏠 Ana Sayfa</a>
                    <a href="/employees">👥 Çalışanları Gör</a>
                </div>
            </div>
        </body>
        </html>
        """
    except Exception as e:
        return f"Hata: {str(e)}"

# Android uygulamasından gelen konum güncellemeleri
@app.route('/api/location', methods=['POST'])
def update_location():
    data = request.json
    try:
        # Çalışanı IMEI'ye göre bul veya oluştur
        imei = data.get('imei', 'UNKNOWN_IMEI')
        employee = Employee.query.filter_by(imei=imei).first()
        
        if not employee:
            # Yeni çalışan oluştur
            employee = Employee(
                first_name=data.get('first_name', 'Mobil'),
                last_name=data.get('last_name', 'Kullanıcı'),
                phone_number=data.get('phone', 'Telefon yok'),
                imei=imei,
                program_serial_no=f"MOB_{imei[-6:]}"  # Son 6 karakter
            )
            db.session.add(employee)
            db.session.commit()
        
        # Konum kaydı oluştur
        location = LocationHistory(
            employee_id=employee.id,
            latitude=data['latitude'],
            longitude=data['longitude'],
            accuracy=data.get('accuracy'),
            speed=data.get('speed')
        )
        db.session.add(location)
        db.session.commit()
        
        print(f"📍 Konum alındı: {employee.first_name} {employee.last_name} - {data['latitude']}, {data['longitude']}")
        return jsonify({'status': 'success', 'employee_id': employee.id})
    except Exception as e:
        print(f"❌ Konum kaydı hatası: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Veritabanı tabloları oluştur
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    print("🚀 GPS Tracker başlatılıyor...")
    print("📱 Tarayıcıda şu adresi açın: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000) 