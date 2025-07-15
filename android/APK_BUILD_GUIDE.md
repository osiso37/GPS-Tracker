# Android APK Oluşturma Rehberi

Bu rehber Android Studio kullanmadan APK dosyası oluşturmanız için gerekli adımları içerir.

## Seçenek 1: Command Line Tools ile APK Oluşturma (Önerilen)

### 1. Gerekli Yazılımları İndirin

#### a) Java Development Kit (JDK)
```
https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html
```
- JDK 11 veya üstünü indirin ve kurun

#### b) Android SDK Command Line Tools
```
https://developer.android.com/studio#command-tools
```
- "Command line tools only" bölümünden Windows için zip dosyasını indirin

### 2. Kurulum Adımları

#### a) Android SDK Kurulumu
1. İndirdiğiniz cmdline-tools.zip dosyasını açın
2. `C:\Android\` klasörü oluşturun
3. Zip içeriğini `C:\Android\cmdline-tools\latest\` klasörüne çıkarın

#### b) Environment Variables Ayarlama
1. Windows + R tuşlarına basın, `sysdm.cpl` yazın
2. "Advanced" sekmesine gidin
3. "Environment Variables" butonuna tıklayın
4. System Variables bölümünde "New" butonuna tıklayın:
   - Variable name: `ANDROID_HOME`
   - Variable value: `C:\Android`
5. PATH değişkenine şunları ekleyin:
   - `%ANDROID_HOME%\cmdline-tools\latest\bin`
   - `%ANDROID_HOME%\platform-tools`

### 3. Android SDK Bileşenlerini İndirin

Command Prompt'u yönetici olarak açın ve şu komutları çalıştırın:

```bash
# SDK Manager ile gerekli bileşenleri yükleyin
sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.2"
sdkmanager "platforms;android-34" "build-tools;34.0.0"

# Lisansları kabul edin
sdkmanager --licenses
```

### 4. APK Oluşturma

1. Proje klasörüne gidin:
```bash
cd GPS\android
```

2. Windows'ta build.bat dosyasını çalıştırın:
```bash
build.bat
```

3. Veya manuel olarak:
```bash
gradlew.bat clean
gradlew.bat assembleDebug
```

### 5. APK Konumu
Oluşturulan APK dosyası şu konumda bulunacak:
```
android\app\build\outputs\apk\debug\app-debug.apk
```

## Seçenek 2: Online Build Servisleri

### AppCenter (Microsoft)
1. https://appcenter.ms/ adresine gidin
2. GitHub hesabınızla giriş yapın
3. Projenizi yükleyin
4. Build konfigürasyonu yapın
5. APK dosyasını indirin

### GitHub Actions (Ücretsiz)
1. Projenizi GitHub'a yükleyin
2. `.github/workflows/android.yml` dosyası oluşturun
3. Her commit'te otomatik APK oluşturulsun

## Seçenek 3: Docker ile Build

Docker kullanarak izole bir ortamda build yapabilirsiniz:

```dockerfile
# Dockerfile
FROM openjdk:11-jdk

# Android SDK kurulumu
ENV ANDROID_HOME /opt/android-sdk
RUN mkdir -p ${ANDROID_HOME}/cmdline-tools && \
    wget -q https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip && \
    unzip -q commandlinetools-linux-8512546_latest.zip -d ${ANDROID_HOME}/cmdline-tools && \
    mv ${ANDROID_HOME}/cmdline-tools/cmdline-tools ${ANDROID_HOME}/cmdline-tools/latest

ENV PATH ${PATH}:${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools

# SDK bileşenlerini yükle
RUN yes | sdkmanager --licenses && \
    sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.2"

WORKDIR /app
COPY . .
RUN ./gradlew assembleDebug
```

## Sorun Giderme

### "ANDROID_HOME not set" Hatası
- Environment variables'ı doğru ayarladığınızdan emin olun
- Command Prompt'u yeniden başlatın

### "SDK location not found" Hatası
- `local.properties` dosyası oluşturun:
```properties
sdk.dir=C:\\Android
```

### "Permission denied" Hatası (Linux/Mac)
```bash
chmod +x gradlew
```

### Gradle Download Hatası
- İnternet bağlantınızı kontrol edin
- Proxy ayarlarınızı kontrol edin

## APK'yı Cihaza Yükleme

### ADB ile Yükleme
```bash
# USB debugging açık olmalı
adb install app-debug.apk
```

### Manuel Yükleme
1. APK dosyasını cihaza kopyalayın
2. Dosya yöneticisinden APK'ya tıklayın
3. "Bilinmeyen kaynaklardan uygulama yükleme" iznini verin
4. Yükleme işlemini tamamlayın

## Güvenlik Notları

- Debug APK sadece test için kullanın
- Production için signed APK oluşturun
- Keystore dosyanızı güvenli saklayın

## Destek

Sorun yaşarsanız:
1. Gradle build loglarını kontrol edin
2. Android SDK versiyonlarını kontrol edin
3. Java versiyonunu kontrol edin (JDK 11+)

Build işlemi başarılı olduğunda `app-debug.apk` dosyası hazır olacaktır. 