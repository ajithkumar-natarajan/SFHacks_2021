package com.example.kinshield.features.data

import com.google.gson.annotations.SerializedName

class Member(
        @SerializedName("name") var name: String?= null,
        @SerializedName("email")  var email:String?= null,
        @SerializedName("zip")  var zip:Int?= null,
        @SerializedName("age") var age : Int?= null,
        @SerializedName("kid") var kid : Boolean?= null,
        @SerializedName("uuid")  var uuid : String?= null
) {

}

