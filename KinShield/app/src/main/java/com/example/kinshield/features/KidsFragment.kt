package com.example.kinshield.features

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.RecyclerView
import androidx.recyclerview.widget.StaggeredGridLayoutManager
import com.example.kinshield.R
import com.example.kinshield.features.data.Member
import com.google.firebase.database.*
import com.google.firebase.database.ktx.getValue

class KidsFragment : Fragment() {
    private var mainRecycler : RecyclerView?= null
    private lateinit var database : FirebaseDatabase
    private lateinit var reference : DatabaseReference
    private lateinit var query : Query

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        return return inflater.inflate(R.layout.activity_kids, container, false)
    }
    override fun onViewCreated(
        view: View,
        savedInstanceState: Bundle?
    ) {
        super.onViewCreated(view, savedInstanceState)
        mainRecycler = view.findViewById(R.id.rvTasks)
        val layoutManager : RecyclerView.LayoutManager = StaggeredGridLayoutManager(3,StaggeredGridLayoutManager.VERTICAL)
//        val layoutManager : RecyclerView.LayoutManager = LinearLayoutManager(context)
//        layoutManager.(StaggeredGridLayoutManager.GAP_HANDLING_NONE
        mainRecycler!!.layoutManager = layoutManager
        mainRecycler!!.setHasFixedSize(true)
        val itemOnClick: (Member) -> Unit = { position ->
        //    Toast.makeText(this.context,"$position. item clicked.",Toast.LENGTH_SHORT).show()
            val intent = Intent(context, DetailsActivity::class.java)

            startActivity(intent)
        }
        val mainAdapter = MainAdapter (context, itemOnClick)

        mainRecycler!!.adapter = mainAdapter

         query = FirebaseDatabase.getInstance().getReference("message").orderByChild("kid").equalTo(true)


        query.addValueEventListener(object : ValueEventListener{
            override fun onCancelled(error: DatabaseError) {
                Log.e("cancel",error.toString())        }

            override fun onDataChange(snapshot: DataSnapshot) {
                var list = ArrayList<Member>()
                for ( data in snapshot.children){
//                    var model = data.getValue(Member::class.java)
                    var model = data.getValue<Member>()
                    list.add(model as Member)
                }

                mainAdapter.setData(list)
            }})


    }
    private  fun getData() {

    }

    companion object {
        const val TAG = "HOME_FRAGMENT"
    }


}
