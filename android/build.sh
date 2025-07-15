#!/bin/bash

# Android APK Build Script
# Bu script Android SDK command line tools kullanarak APK oluşturur

echo "Android GPS Tracker APK Build Script"
echo "=================================="

# Android SDK kurulu olup olmadığını kontrol et
if [ -z "$ANDROID_HOME" ]; then
    echo "Hata: ANDROID_HOME environment variable tanımlanmamış"
    echo "Android SDK'yı indirin ve ANDROID_HOME'u ayarlayın"
    exit 1
fi

# Proje dizinine git
cd "$(dirname "$0")"

echo "1. Dependencies indiriliyor..."
./gradlew dependencies

echo "2. Proje temizleniyor..."
./gradlew clean

echo "3. Debug APK oluşturuluyor..."
./gradlew assembleDebug

if [ $? -eq 0 ]; then
    echo "✅ APK başarıyla oluşturuldu!"
    echo "📱 APK konumu: app/build/outputs/apk/debug/app-debug.apk"
    
    # APK bilgilerini göster
    echo ""
    echo "APK Bilgileri:"
    echo "============="
    ls -lh app/build/outputs/apk/debug/app-debug.apk
    
    echo ""
    echo "APK'yı cihaza yüklemek için:"
    echo "adb install app/build/outputs/apk/debug/app-debug.apk"
else
    echo "❌ APK oluşturulurken hata oluştu"
    exit 1
fi 