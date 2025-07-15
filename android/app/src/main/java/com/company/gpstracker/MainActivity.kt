package com.company.gpstracker

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.location.Location
import android.os.Bundle
import android.os.Looper
import android.provider.Settings
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import com.google.android.gms.location.*
import kotlinx.coroutines.*
import okhttp3.*
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject
import java.io.IOException

class MainActivity : AppCompatActivity() {
    private lateinit var fusedLocationClient: FusedLocationProviderClient
    private lateinit var locationCallback: LocationCallback
    private lateinit var startButton: Button
    private lateinit var stopButton: Button
    private lateinit var statusText: TextView
    private lateinit var editFirstName: EditText
    private lateinit var editLastName: EditText
    private lateinit var editPhone: EditText
    private lateinit var deviceInfo: TextView
    
    private val LOCATION_PERMISSION_REQUEST = 1000
    // Yerel sunucu için - WiFi IP adresinizi buraya yazın (örn: 192.168.1.100)
    private val serverUrl = "http://192.168.1.28:5000/api/location"
    private val employeeId = "MOBILE_USER_001"
    private val client = OkHttpClient()
    private var isTracking = false
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        // UI elementlerini bağla
        startButton = findViewById(R.id.startButton)
        stopButton = findViewById(R.id.stopButton)
        statusText = findViewById(R.id.statusText)
        editFirstName = findViewById(R.id.editFirstName)
        editLastName = findViewById(R.id.editLastName)
        editPhone = findViewById(R.id.editPhone)
        deviceInfo = findViewById(R.id.deviceInfo)
        
        // Cihaz bilgilerini göster
        val deviceId = Settings.Secure.getString(contentResolver, Settings.Secure.ANDROID_ID)
        deviceInfo.text = "📱 IMEI: ${deviceId.take(16)}\n🏭 Seri No: MOB_${deviceId.takeLast(6)}"
        
        fusedLocationClient = LocationServices.getFusedLocationProviderClient(this)
        
        // Buton click listener'larını ekle
        startButton.setOnClickListener {
            if (validateUserInput()) {
                if (checkPermissions()) {
                    startTracking()
                } else {
                    requestPermissions()
                }
            }
        }
        
        stopButton.setOnClickListener {
            stopTracking()
        }
        
        // Konum güncellemelerini dinle
        locationCallback = object : LocationCallback() {
            override fun onLocationResult(locationResult: LocationResult) {
                locationResult.lastLocation?.let { location ->
                    sendLocationToServer(location)
                    updateStatus("Konum gönderildi: ${location.latitude}, ${location.longitude}")
                }
            }
        }
        
        updateStatus("📝 Bilgilerinizi girip takibi başlatın")
    }
    
    private fun startTracking() {
        if (!checkPermissions()) {
            requestPermissions()
            return
        }
        
        updateStatus("GPS takibi başlatılıyor...")
        startLocationUpdates()
        isTracking = true
        startButton.isEnabled = false
        stopButton.isEnabled = true
    }
    
    private fun stopTracking() {
        fusedLocationClient.removeLocationUpdates(locationCallback)
        isTracking = false
        startButton.isEnabled = true
        stopButton.isEnabled = false
        updateStatus("GPS takibi durduruldu")
        Toast.makeText(this, "Takip durduruldu", Toast.LENGTH_SHORT).show()
    }
    
    private fun updateStatus(message: String) {
        runOnUiThread {
            statusText.text = message
        }
    }
    
    private fun checkPermissions(): Boolean {
        return REQUIRED_PERMISSIONS.all {
            ContextCompat.checkSelfPermission(this, it) == PackageManager.PERMISSION_GRANTED
        }
    }
    
    private fun requestPermissions() {
        ActivityCompat.requestPermissions(
            this,
            REQUIRED_PERMISSIONS,
            LOCATION_PERMISSION_REQUEST
        )
    }
    
    private fun startLocationUpdates() {
        val locationRequest = LocationRequest.create().apply {
            priority = LocationRequest.PRIORITY_HIGH_ACCURACY
            interval = 10000 // 10 saniye
            fastestInterval = 5000 // 5 saniye
        }
        
        if (ActivityCompat.checkSelfPermission(
                this,
                Manifest.permission.ACCESS_FINE_LOCATION
            ) == PackageManager.PERMISSION_GRANTED
        ) {
            fusedLocationClient.requestLocationUpdates(
                locationRequest,
                locationCallback,
                Looper.getMainLooper()
            )
            Toast.makeText(this, "GPS takibi başlatıldı", Toast.LENGTH_SHORT).show()
            updateStatus("GPS takibi aktif - konum bekleniyor...")
        }
    }
    
    private fun validateUserInput(): Boolean {
        val firstName = editFirstName.text.toString().trim()
        val lastName = editLastName.text.toString().trim()
        val phone = editPhone.text.toString().trim()
        
        when {
            firstName.isEmpty() -> {
                editFirstName.error = "Ad gerekli"
                editFirstName.requestFocus()
                return false
            }
            lastName.isEmpty() -> {
                editLastName.error = "Soyad gerekli"
                editLastName.requestFocus()
                return false
            }
            phone.isEmpty() -> {
                editPhone.error = "Telefon numarası gerekli"
                editPhone.requestFocus()
                return false
            }
            !phone.matches(Regex("^[0-9]{11}$")) -> {
                editPhone.error = "11 haneli telefon numarası girin (05xxxxxxxxx)"
                editPhone.requestFocus()
                return false
            }
        }
        return true
    }
    
    private fun sendLocationToServer(location: Location) {
        val deviceId = Settings.Secure.getString(contentResolver, Settings.Secure.ANDROID_ID)
        val firstName = editFirstName.text.toString().trim()
        val lastName = editLastName.text.toString().trim()
        val phone = editPhone.text.toString().trim()
        
        val json = JSONObject().apply {
            put("employee_id", employeeId)
            put("first_name", firstName)
            put("last_name", lastName)
            put("phone", phone)
            put("imei", deviceId)
            put("latitude", location.latitude)
            put("longitude", location.longitude)
            put("accuracy", location.accuracy)
            put("speed", location.speed)
        }
        
        val request = Request.Builder()
            .url(serverUrl)
            .post(json.toString().toRequestBody("application/json".toMediaType()))
            .build()
            
        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {
                runOnUiThread {
                    updateStatus("Sunucu bağlantı hatası: ${e.message}")
                }
                e.printStackTrace()
            }
            
            override fun onResponse(call: Call, response: Response) {
                runOnUiThread {
                    if (response.isSuccessful) {
                        updateStatus("Konum başarıyla gönderildi ✓")
                    } else {
                        updateStatus("Sunucu hatası: ${response.code}")
                    }
                }
                response.close()
            }
        })
    }
    
    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if (requestCode == LOCATION_PERMISSION_REQUEST) {
            if (grantResults.all { it == PackageManager.PERMISSION_GRANTED }) {
                startTracking()
            } else {
                Toast.makeText(
                    this,
                    "Konum izni olmadan uygulama çalışamaz",
                    Toast.LENGTH_LONG
                ).show()
                updateStatus("Konum izni gerekli")
            }
        }
    }
    
    override fun onDestroy() {
        super.onDestroy()
        if (isTracking) {
            fusedLocationClient.removeLocationUpdates(locationCallback)
        }
    }
    
    companion object {
        private val REQUIRED_PERMISSIONS = arrayOf(
            Manifest.permission.ACCESS_FINE_LOCATION,
            Manifest.permission.ACCESS_COARSE_LOCATION
        )
    }
} 