# 🔄 GitHub ile Senkronizasyon Rehberi

## 🚀 GitHub Desktop ile Kolay Senkronizasyon

### 1. GitHub Desktop İndirin
- https://desktop.github.com/ adresine gidin
- "Download for Windows" butonuna tıklayın
- İndirilen dosyayı çalıştırın ve kurun

### 2. GitHub Hesabınızla Giriş Yapın
- GitHub Desktop'u açın
- "Sign in to GitHub.com" seçin
- GitHub kullanıcı adı ve şifrenizi girin
- Yetkilendirmeyi onaylayın

### 3. Yeni Repository Oluşturun
#### A) Yerel Repository Oluşturma
- GitHub Desktop'ta "Create a new repository" seçin
- **Name:** `gps-tracker`
- **Local path:** `C:\Users\EROL\Desktop\GPS`
- **Initialize with README** işaretleyin
- "Create repository" tıklayın

#### B) GitHub'a Publish
- "Publish repository" butonuna tıklayın
- **Name:** `gps-tracker`
- **Public** seçin (ücretsiz Actions için)
- "Publish repository" tıklayın

### 4. Dosyalarınızı Commit Edin
GitHub Desktop otomatik olarak tüm dosyalarınızı görecek:
- **Summary:** "GPS Tracker projesi - İlk commit"
- **Description:** "Web arayüzü ve Android uygulaması"
- "Commit to main" butonuna tıklayın

### 5. GitHub'a Push Edin
- "Push origin" butonuna tıklayın
- Dosyalarınız GitHub'a yüklenecek

### 6. GitHub Actions Çalışacak
- GitHub.com'da repository'nizi açın
- "Actions" sekmesine gidin
- "Build Android APK" workflow'u otomatik başlayacak
- 10-15 dakika bekleyin

### 7. APK'yı İndirin
- Build tamamlandığında
- Actions sayfasında build'e tıklayın
- "Artifacts" → "gps-tracker-debug-apk" indirin

## 🔄 Güncellemeler İçin

Her değişiklikte:
1. **GitHub Desktop'ta değişiklikleri görün**
2. **Commit message yazın**
3. **"Commit to main" tıklayın**
4. **"Push origin" tıklayın**
5. **Otomatik APK oluşacak**

## 🛠️ Alternatif: Web Interface

Git kurulumunda sorun yaşıyorsanız:

### 1. GitHub.com'da Repository Oluşturun
- GitHub.com → "New repository"
- **Name:** `gps-tracker`
- **Public** seçin
- "Create repository"

### 2. Dosyaları Drag & Drop
- "uploading an existing file" linkine tıklayın
- GPS klasörünüzdeki TÜM dosyaları sürükleyip bırakın
- **Commit message:** "GPS Tracker projesi"
- "Commit changes" tıklayın

## 📱 APK Test Rehberi

APK indirdikten sonra:
1. **APK'yı telefona gönderin** (WhatsApp, Email, USB)
2. **"Bilinmeyen kaynaklar" iznini verin**
3. **APK'ya tıklayarak yükleyin**
4. **GPS Tracker uygulaması açılacak**

## 🎯 Sistem Özeti

✅ **Web arayüzü:** http://localhost:5000
✅ **Android kodu:** Hazır
✅ **GitHub Actions:** Otomatik APK
✅ **Senkronizasyon:** Desktop/Web

## 🚨 Sorun Giderme

### GitHub Desktop Kurulumunda Sorun
- Web interface kullanın (drag & drop)

### Build Failed
- Actions loglarını kontrol edin
- Repository'nin Public olduğundan emin olun

### APK Yüklenmiyor
- "Bilinmeyen kaynaklar" iznini kontrol edin
- Cihazda yeterli alan olduğundan emin olun

**Hangi yöntemi tercih edersiniz?**
1. GitHub Desktop (önerilen)
2. Web interface (kolay)

Her iki durumda da 15-20 dakikada APK hazır olacak! 🚀 

## 🎉 GitHub Senkronizasyon Hazır!

Mükemmel! GitHub hesabınız olduğuna göre şu seçenekleriniz var:

### 🥇 **GitHub Desktop (Önerilen)**
```
1. https://desktop.github.com/ → Download
2. Kurun ve GitHub hesabınızla giriş yapın
3. GPS klasörünü repository olarak ekleyin
4. Commit & Push → Otomatik APK oluşacak
```

### 🥈 **Web Interface (Hızlı)**
```
1. GitHub.com → New repository → gps-tracker
2. "Upload files" → GPS klasörünüzdeki dosyaları sürükleyin
3. Commit → Actions otomatik başlar
```

## 📁 Senkronize Edilecek Dosyalar

✅ **Web uygulaması:** `app_sqlite.py` (çalışıyor)
✅ **Android kodu:** `android/` klasörü (hazır)
✅ **GitHub Actions:** `.github/workflows/` (otomatik APK)
✅ **Veritabanı:** `database/` şeması
✅ **Dökümanlar:** Tüm `.md` rehberleri

## 🚀 Sonraki Adımlar

1. **GitHub Desktop kurun** VEYA **web interface kullanın**
2. **Dosyaları yükleyin** (5 dakika)
3. **Actions'ın çalışmasını bekleyin** (15 dakika)
4. **APK'yı indirip test edin** (5 dakika)

## 📱 APK Hazır Olduğunda

- Telefona WhatsApp/Email ile gönderin
- "Bilinmeyen kaynaklar" iznini verin
- APK'ya tıklayıp yükleyin
- GPS Tracker uygulaması kulıma hazır!

**`GITHUB_SENKRONIZASYON.md` dosyasını açın ve tercih ettiğiniz yöntemi takip edin!**

Hangi yöntemi seçmek istiyorsunuz? GitHub Desktop mi yoksa web interface mi? 🤔 

## 🚀 Dosyaları GitHub'a Yükleyelim

### Adım 1: Dosyaları Commit Edin

GitHub Desktop'ta şu anda sol tarafta tüm dosyaları görüyorsunuz. Şimdi:

1. **Sol alttaki "Summary (required)" kutusuna** şunu yazın:
   ```
   GPS Tracker projesi - İlk yükleme
   ```

2. **"Description" kutusuna** (opsiyonel) şunu yazın:
   ```
   Web arayüzü ve Android uygulaması eklendi
   KVKK uyumlu GPS takip sistemi
   ```

3. **"Commit to main"** mavi butonuna tıklayın

### Adım 2: GitHub'a Push Edin

Commit'ten sonra:

1. Üst kısımda **"Push origin"** butonu görünecek
2. Bu butona tıklayın
3. Dosyalar GitHub'a yüklenmeye başlayacak

### Adım 3: Repository'yi Public Yapın

Eğer repository private ise:

1. **"View on GitHub"** butonuna tıklayın (tarayıcıda açılacak)
2. GitHub'da **Settings** sekmesine gidin
3. En aşağıda **"Change repository visibility"** bölümünü bulun
4. **"Change visibility"** → **"Make public"** seçin
5. Repository adını onaylayın

### Adım 4: GitHub Actions'ı Kontrol Edin

GitHub'da (tarayıcıda):

1. **"Actions"** sekmesine tıklayın
2. **"Build Android APK"** workflow'unun başladığını göreceksiniz
3. ⏱️ **10-15 dakika bekleyin**
4. Build tamamlandığında **yeşil tick (✅)** görünecek

### Adım 5: APK'yı İndirin

Build tamamlandığında:

1. Actions sayfasında **build'e tıklayın**
2. **"Artifacts"** bölümünde **"gps-tracker-debug-apk"** bulun
3. İndirin ve ZIP'i açın
4. 🎉 **APK dosyanız hazır!**

---

## 📱 Sonraki Adım: APK Test

APK hazır olduğunda:
- Telefona gönderin (WhatsApp/Email)
- "Bilinmeyen kaynaklar" iznini verin
- Yükleyin ve test edin

**Şu anda hangi adımdasınız? Commit'i yaptınız mı?** 🤔 