# 🚀 GPS Takip Sistemi - Hızlı Başlangıç

## 📱 Android APK Oluşturma (En Kolay Yöntemler)

### Seçenek 1: GitHub Actions (Otomatik - Önerilen)

1. **Projeyi GitHub'a yükleyin:**
   ```bash
   git init
   git add .
   git commit -m "İlk commit"
   git remote add origin https://github.com/kullanici-adiniz/gps-tracker.git
   git push -u origin main
   ```

2. **APK otomatik oluşacak:**
   - GitHub repository'nizde "Actions" sekmesine gidin
   - Build tamamlandığında "Artifacts" bölümünden APK'yı indirin
   - Her kod değişikliğinde otomatik yeni APK oluşur

### Seçenek 2: Command Line (Manuel)

1. **Java JDK 11 indirin:**
   - https://adoptium.net/temurin/releases/ 
   - JDK 11 LTS Windows x64 seçin

2. **Android Command Line Tools indirin:**
   - https://developer.android.com/studio#command-tools
   - "Command line tools only" Windows zip dosyasını indirin

3. **Kurulum yapın:**
   ```bash
   # 1. C:\Android\ klasörü oluşturun
   # 2. cmdline-tools'u C:\Android\cmdline-tools\latest\ içine çıkarın
   # 3. Environment Variables ayarlayın:
   #    ANDROID_HOME = C:\Android
   #    PATH'e ekleyin: %ANDROID_HOME%\cmdline-tools\latest\bin
   ```

4. **SDK bileşenleri yükleyin:**
   ```bash
   sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.2"
   sdkmanager --licenses
   ```

5. **APK oluşturun:**
   ```bash
   cd GPS\android
   build.bat
   ```

### Seçenek 3: Online Build Servisi

**AppCenter (Microsoft) - Ücretsiz:**
1. https://appcenter.ms/ hesap açın
2. Projenizi yükleyin
3. Build ayarları yapın
4. APK indirin

## 🌐 Web Arayüzü Kurulumu

1. **Python kurulumu:**
   ```bash
   # Python 3.8+ indirin: https://python.org
   pip install -r requirements.txt
   ```

2. **Veritabanı kurulumu:**
   - SQL Server Express indirin
   - `database/schema.sql` dosyasını çalıştırın

3. **Konfigürasyon:**
   ```bash
   # .env dosyası oluşturun ve düzenleyin:
   SECRET_KEY=gizli-anahtar-buraya
   DATABASE_URL=mssql+pyodbc://kullanici:sifre@server/veritabani?driver=SQL+Server
   ```

4. **Çalıştırma:**
   ```bash
   python app.py
   ```

## 📋 Checklist

### ✅ Hazırlık
- [ ] Python 3.8+ kuruldu
- [ ] Java JDK 11+ kuruldu
- [ ] SQL Server kuruldu
- [ ] GitHub hesabı var

### ✅ Android APK
- [ ] GitHub'da proje oluşturuldu
- [ ] Actions workflow çalışıyor
- [ ] APK başarıyla oluştu
- [ ] APK test cihazında yüklendi

### ✅ Web Arayüzü
- [ ] Python paketleri yüklendi
- [ ] Veritabanı tabloları oluşturuldu
- [ ] .env dosyası yapılandırıldı
- [ ] Web uygulaması çalışıyor

### ✅ Test
- [ ] Android uygulaması konum gönderiyor
- [ ] Web arayüzünde konumlar görünüyor
- [ ] Canlı takip çalışıyor

## 🆘 Sorun Çözme

### Android Studio olmadan APK alamıyorum
➡️ **Çözüm:** GitHub Actions kullanın - hiçbir kurulum gerektirmez

### Gradle build hatası alıyorum
➡️ **Çözüm:** Java versiyonunu kontrol edin (JDK 11+)

### Veritabanı bağlantısı yok
➡️ **Çözüm:** .env dosyasındaki connection string'i kontrol edin

### Konumlar gelmiyor
➡️ **Çözüm:** Android uygulamasında konum izinlerini kontrol edin

## 📞 Destek

Sorun yaşarsanız:
1. `android/APK_BUILD_GUIDE.md` dosyasını inceleyin
2. Error loglarını kontrol edin
3. GitHub Issues açın

## 🎯 Sonraki Adımlar

1. **Production kurulumu için:**
   - SSL sertifikası ekleyin
   - Güvenlik ayarlarını sıkılaştırın
   - Signed APK oluşturun

2. **Özellik geliştirmesi:**
   - Coğrafi sınırlar (geofencing)
   - Raporlama sistemi
   - Push notification

**🚨 ÖNEMLİ:** Test ortamında kullanın, production'a geçmeden önce güvenlik testleri yapın! 