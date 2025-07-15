package com.company.gpstracker

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.location.Location
import android.os.Bundle
import android.os.Looper
import android.provider.Settings
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
    private val LOCATION_PERMISSION_REQUEST = 1000
    private val serverUrl = "https://your-server-url.com/api/location"
    private val employeeId = "YOUR_EMPLOYEE_ID" // Bu değer giriş yapıldığında sunucudan alınmalı
    private val client = OkHttpClient()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        fusedLocationClient = LocationServices.getFusedLocationProviderClient(this)
        
        // Konum güncellemelerini dinle
        locationCallback = object : LocationCallback() {
            override fun onLocationResult(locationResult: LocationResult) {
                locationResult.lastLocation?.let { location ->
                    sendLocationToServer(location)
                }
            }
        }
        
        checkPermissionsAndStartTracking()
    }
    
    private fun checkPermissionsAndStartTracking() {
        when {
            checkPermissions() -> startLocationUpdates()
            shouldShowRequestPermissionRationale() -> showPermissionExplanation()
            else -> requestPermissions()
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
    
    private fun shouldShowRequestPermissionRationale(): Boolean {
        return REQUIRED_PERMISSIONS.any {
            ActivityCompat.shouldShowRequestPermissionRationale(this, it)
        }
    }
    
    private fun showPermissionExplanation() {
        Toast.makeText(
            this,
            "Konum izni uygulamanın çalışması için gereklidir",
            Toast.LENGTH_LONG
        ).show()
        requestPermissions()
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
        }
    }
    
    private fun sendLocationToServer(location: Location) {
        val json = JSONObject().apply {
            put("employee_id", employeeId)
            put("latitude", location.latitude)
            put("longitude", location.longitude)
            put("accuracy", location.accuracy)
            put("speed", location.speed)
            put("imei", Settings.Secure.getString(contentResolver, Settings.Secure.ANDROID_ID))
        }
        
        val request = Request.Builder()
            .url(serverUrl)
            .post(json.toString().toRequestBody("application/json".toMediaType()))
            .build()
            
        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {
                // Hata durumunda lokasyonu yerel veritabanına kaydet
                e.printStackTrace()
            }
            
            override fun onResponse(call: Call, response: Response) {
                if (!response.isSuccessful) {
                    // Başarısız yanıt durumunda lokasyonu yerel veritabanına kaydet
                    response.close()
                }
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
                startLocationUpdates()
            } else {
                Toast.makeText(
                    this,
                    "Konum izni olmadan uygulama çalışamaz",
                    Toast.LENGTH_LONG
                ).show()
                finish()
            }
        }
    }
    
    override fun onDestroy() {
        super.onDestroy()
        fusedLocationClient.removeLocationUpdates(locationCallback)
    }
    
    companion object {
        private val REQUIRED_PERMISSIONS = arrayOf(
            Manifest.permission.ACCESS_FINE_LOCATION,
            Manifest.permission.ACCESS_COARSE_LOCATION
        )
    }
} 