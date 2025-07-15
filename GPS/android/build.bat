@echo off
title Android GPS Tracker APK Build

echo Android GPS Tracker APK Build Script
echo ==================================

REM Android SDK kurulu olup olmadigini kontrol et
if "%ANDROID_HOME%"=="" (
    echo Hata: ANDROID_HOME environment variable tanimlanmamis
    echo Android SDK'yi indirin ve ANDROID_HOME'u ayarlayin
    pause
    exit /b 1
)

REM Proje dizinine git
cd /d "%~dp0"

echo 1. Dependencies indiriliyor...
call gradlew.bat dependencies

echo 2. Proje temizleniyor...
call gradlew.bat clean

echo 3. Debug APK olusturuluyor...
call gradlew.bat assembleDebug

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ APK basariyla olusturuldu!
    echo 📱 APK konumu: app\build\outputs\apk\debug\app-debug.apk
    
    echo.
    echo APK Bilgileri:
    echo =============
    dir app\build\outputs\apk\debug\app-debug.apk
    
    echo.
    echo APK'yi cihaza yuklemek icin:
    echo adb install app\build\outputs\apk\debug\app-debug.apk
) else (
    echo ❌ APK olusturulurken hata olustu
)

pause 