# Şirket GPS Takip Sistemi

Bu sistem, şirket çalışanlarının GPS konumlarını takip etmek için geliştirilmiş bir uygulamadır.

## Sistem Bileşenleri

1. Android Uygulaması
2. Python Web Arayüzü

## Kurulum

### Web Arayüzü Kurulumu

1. Python 3.8+ yükleyin
2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```
3. .env dosyasını düzenleyin
4. Veritabanı bağlantısını yapılandırın
5. Uygulamayı başlatın:
```bash
python app.py
```

### Android Uygulaması Kurulumu

1. Android Studio'yu açın
2. Projeyi import edin
3. Build alın ve APK oluşturun
4. Cihazlara yükleyin

## Güvenlik

- Tüm veriler KVKK uyumlu olarak işlenir
- Çalışan onayı gereklidir
- Veriler şifreli olarak saklanır 