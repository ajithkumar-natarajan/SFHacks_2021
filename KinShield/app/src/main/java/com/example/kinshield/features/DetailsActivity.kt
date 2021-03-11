package com.example.kinshield.features

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Switch
import androidx.appcompat.app.AppCompatActivity
import com.example.kinshield.R
import android.view.View
import android.widget.Toast
import com.example.kinshield.features.data.Member
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.FirebaseDatabase

class DetailsActivity : AppCompatActivity() {
    val TAG = "AddMemberActivity"
    private lateinit var database : FirebaseDatabase


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_details)


    }
}
