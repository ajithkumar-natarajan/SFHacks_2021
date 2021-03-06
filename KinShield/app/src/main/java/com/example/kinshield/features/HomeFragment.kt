package com.example.kinshield.features

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.example.kinshield.R

class HomeFragment : Fragment() {
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        // Inflate the layout for this fragment
        val view:View = inflater.inflate(R.layout.fragment_home, container, false)
        val fabAddHabit: View = view.findViewById(R.id.fabAddHabit)
        fabAddHabit.setOnClickListener { view ->
            val intent = Intent(context, AddMemberActivity::class.java)
            //intent.putExtra("habit", emptyHabit)
            startActivity(intent)
        }
        return view
    }
}