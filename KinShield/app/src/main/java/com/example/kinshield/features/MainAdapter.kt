package com.example.kinshield.features

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.constraintlayout.widget.ConstraintLayout
import androidx.recyclerview.widget.RecyclerView
import com.example.kinshield.R
import com.example.kinshield.features.data.Member


class MainAdapter(
    private val context: Context?,private val onItemClicked: (Member) -> Unit
): RecyclerView.Adapter<MainAdapter.goalsHolder>() {
    private var kidsList = emptyList<Member>()

    class goalsHolder (itemView : View) : RecyclerView.ViewHolder(itemView){
        var kidName : TextView = itemView.findViewById(R.id.goal_title)
//        var itemRecycler :RecyclerView = itemView.findViewById(R.id.goal_item_recycler)
        var mainLinearLayout : ConstraintLayout = itemView.findViewById(R.id.main_linearLayout)
       }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): goalsHolder {

        return goalsHolder(LayoutInflater.from(context).inflate(R.layout.each_goal_recycler_item ,parent , false))
    }

    override fun getItemCount(): Int {
        return kidsList.size
    }

    override fun onBindViewHolder(holder: goalsHolder, position: Int) {
        holder.kidName.text = kidsList[position].name
        val item = kidsList[position]
        holder.itemView.setOnClickListener { onItemClicked(item) }

//        if (position % 2 ==0){
//            holder.mainLinearLayout.setBackgroundResource(R.drawable.rounded_background_orange) }
//        else {
//            holder.mainLinearLayout.setBackgroundResource(R.drawable.rounded_background_blue) }
//            mGoalViewModel = ViewModelProvider((context as FragmentActivity?)!!).get(GoalViewModel::class.java)
//            mGoalViewModel.getHabitsByGoal(goalList[position].goalTitle).observe(viewLifecycleOwner,androidx.lifecycle.Observer { habit ->
//                    val habitList = habit[0].habits
//                    val itemRecyclerAdapter = TaskAdapter( habitList )
//                    holder.itemRecycler .layoutManager = GridLayoutManager(context ,2, GridLayoutManager.VERTICAL,false)
//                    holder.itemRecycler .adapter = itemRecyclerAdapter
//                })
    }

    fun setData( member: List<com.example.kinshield.features.data.Member> ){
        this.kidsList = member
        notifyDataSetChanged()
    }



    companion object {
        const val TAG = "GoalsAdapter"
    }


}