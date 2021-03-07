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

class AddMemberActivity : AppCompatActivity() {
    val TAG = "AddMemberActivity"
    private lateinit var database : FirebaseDatabase
    private lateinit var reference : DatabaseReference
    private lateinit var etName: EditText
    private lateinit var etNickname: EditText
    private lateinit var etEmail: EditText
    private lateinit var etZip: EditText
    private lateinit var etRelation: EditText
    private lateinit var etAge: EditText
    private lateinit var toggleSwitch : Switch
    private lateinit var btnSubmit: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_add_member)
        etName = findViewById(R.id.etName)
        etEmail = findViewById(R.id.etEmail)
        etZip = findViewById(R.id.etZip)
        etAge = findViewById(R.id.etAge)
        toggleSwitch = findViewById(R.id.toggleSwitch)
        btnSubmit = findViewById(R.id.btnSubmit)
        database = FirebaseDatabase.getInstance()
        reference = database.getReference("message")

        btnSubmit.setOnClickListener(View.OnClickListener {
            val name = etName.getText().toString()
            val email = etEmail.getText().toString()
            val zip = etZip.getText().toString()
            val age = etAge.getText().toString()
            if (name == "") {
                Toast.makeText(
                    this@AddMemberActivity,
                    "Name cannot be empty",
                    Toast.LENGTH_LONG
                ).show()
                return@OnClickListener
            }
            if (email == "") {
                Toast.makeText(
                        this@AddMemberActivity,
                        "Email cannot be empty",
                        Toast.LENGTH_LONG
                ).show()
                return@OnClickListener
            }
            if (zip == "") {
                Toast.makeText(
                        this@AddMemberActivity,
                        "ZipCode cannot be empty",
                        Toast.LENGTH_LONG
                ).show()
                return@OnClickListener
            }
            if (age == "") {
                Toast.makeText(
                    this@AddMemberActivity,
                    "Age cannot be empty",
                    Toast.LENGTH_LONG
                ).show()
                return@OnClickListener
            }
            var kid = false
            if (toggleSwitch.isChecked) {
                kid = true }
            saveMemberToDatabase(name, email,zip.toInt(), age.toInt(), kid )

            finish()
        })
    }

    private fun saveMemberToDatabase(name: String, email: String , zip : Int,age: Int,kid: Boolean) {
        try {
            var id = reference.push().key
        var item = Member(name,email,zip, age, kid, id)

        reference.child(id!!).setValue(item)
        } catch (e: Exception) {
            Toast.makeText(this,"Issue with $e",Toast.LENGTH_LONG).show()
        }
        Toast.makeText(this,"Successfully Added !",Toast.LENGTH_LONG).show()
    }
}
