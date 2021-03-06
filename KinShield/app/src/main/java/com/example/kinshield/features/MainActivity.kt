package com.example.kinshield.features

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.RelativeLayout
import androidx.fragment.app.Fragment
import com.example.kinshield.R
import com.google.android.material.bottomnavigation.BottomNavigationView

class MainActivity : AppCompatActivity() {
    private lateinit var bottomNavigationView : BottomNavigationView
    private lateinit var rlRoot: RelativeLayout
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        bottomNavigationView = findViewById(R.id.bottom_navigation)
        rlRoot = findViewById(R.id.rlRoot)
        val homeFragment = HomeFragment()
        val kidsFragment =
                KidsFragment()
        val vaccinesFragment =
                VaccinesFragment()
        val settingsFragment =
                SettingsFragment()

        makeCurrentFragment(homeFragment)
        bottomNavigationView.setOnNavigationItemSelectedListener { menuItem ->
            when (menuItem.itemId) {
                R.id.action_home -> makeCurrentFragment(homeFragment)
                R.id.action_kids -> makeCurrentFragment(kidsFragment)
                R.id.action_vaccines -> makeCurrentFragment(vaccinesFragment)
                R.id.action_user -> makeCurrentFragment(settingsFragment)
            }
            true
        }
    }

    private fun makeCurrentFragment(fragment: Fragment) = supportFragmentManager.beginTransaction().apply {
        replace(R.id.fl_container, fragment)
        commit()
    }

}