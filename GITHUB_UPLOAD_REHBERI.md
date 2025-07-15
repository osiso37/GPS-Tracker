# 🚀 GitHub'a Upload ve Otomatik APK

## 📋 Adım Adım GitHub Actions Kurulumu

### 1. GitHub Hesabı Oluştur
- https://github.com/ git
- "Sign up" tıkla
- Email, kullanıcı adı, şifre gir
- Email doğrula

### 2. Yeni Repository Oluştur
- GitHub'da "New repository" buton
- **Repository name:** `gps-tracker`
- **Public** seç (ücretsiz Actions için)
- "Create repository" tıkla

### 3. Dosyalarını Yükle

#### Yöntem A: Web Interface (Kolay)
1. **"uploading an existing file"** linkine tıkla
2. **GPS klasörünüzdeki TÜM dosyaları** sürükle-bırak
3. Commit message: "GPS Tracker projesi"
4. "Commit changes" tıkla

#### Yöntem B: GitHub Desktop (Önerilen)
1. **GitHub Desktop indirin:** https://desktop.github.com/
2. Kurun ve GitHub hesabınızla giriş yapın
3. "Clone repository" → gps-tracker seçin
4. GPS klasörünüzdeki dosyaları kopyalayın
5. "Commit to main" ve "Push origin" yapın

### 4. Actions Otomatik Başlayacak

Upload tamamlandıktan sonra:
- **"Actions"** sekmesine gidin
- **"Build Android APK"** workflow'u otomatik çalışacak
- **10-15 dakika** bekleyin

### 5. APK'yı İndirin

Build tamamlandığında:
- Actions sayfasında **yeşil tick** görünecek
- Build'e tıklayın
- **"Artifacts"** bölümünden **"gps-tracker-debug-apk"** indirin
- ZIP içinde APK dosyası olacak

## 🔄 Her Kod Değişikliğinde

Artık her dosya değişikliğinde:
1. Dosyaları GitHub'a yükleyin
2. Otomatik APK oluşacak
3. Actions sekmesinden APK indirin

## 📱 APK Test Etme

1. APK'yı Android cihaza aktar
2. "Bilinmeyen kaynaklar" iznini ver
3. APK'ya tıklayarak yükle
4. GPS Tracker uygulaması hazır!

## 🚨 Sorun Giderme

### Build Failed Hatası
- Actions loglarını kontrol edin
- Gradle build hatalarını inceleyin
- Dosya eksikse ekleyin

### Permission Denied
- Repository Public olmalı
- Dosyalar doğru klasörde olmalı

### APK Bulunamıyor
- Build tamamlanmış mı kontrol edin
- Artifacts bölümüne bakın

## ⚡ Hızlı Başlangıç

1. **GitHub hesabı aç** (2 dk)
2. **Repository oluştur** (1 dk)
3. **Dosyaları yükle** (5 dk)
4. **APK bekle** (15 dk)
5. **Test et** (5 dk)

**Toplam süre: ~30 dakika**

## 🎯 Avantajlar

✅ **Tamamen ücretsiz**
✅ **Otomatik build**
✅ **Her değişiklikte APK**
✅ **Versiyon kontrolü**
✅ **Güvenli ve güvenilir**

Hazır olduğunuzda başlayabiliriz! 🚀 