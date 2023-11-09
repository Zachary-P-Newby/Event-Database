import pyrebase
import _collections_abc
#Intialize app
firebaseConfig = {
    "databaseURL": "https://zeta-resource-403920-default-rtdb.firebaseio.com/",
    "apiKey": "AIzaSyDCxGOFDaAcP8DvqPl5Qfx9IC2tWPT8rNs",
    "authDomain": "zeta-resource-403920.firebaseapp.com",
    "databaseURL": "https://zeta-resource-403920-default-rtdb.firebaseio.com",
    "projectId": "zeta-resource-403920",
    "storageBucket": "zeta-resource-403920.appspot.com",
    "messagingSenderId": "166727364399",
    "appId": "1:166727364399:web:137c432742f8e486e47bda",
    "measurementId": "G-F5FTNTXXRC"
}

#import _collections_abc as collections
firebase = pyrebase.initialize_app(firebaseConfig)
#Create Database
database = firebase.database()

#Create Data
#--------------------------------------------------------------------------------------------
#data = {"Eggs":"2 Dozen", "Cereal":"2 Boxes of Oatmeal","Cans of Dog Food":5,"Cartons of Milk":1,"Boxes of Wipes":1}
#Cheese = {"Havarti":"2 Packs of slices","Cheddar":"1 Block","Mozzarella Balls":2}

#database.child("Groceries").child("Walmart").child().set(data)
#database.child("Groceries").child("Walmart").child("Cheese").set(Cheese)
#Melons = {"Water Melon":1,"Cantelope":2}
#
#data = {"Cheese Balls":"1 Jar","Dog Toys":"2","Melons":Melons,"Crackers":"2 Boxes","Toilet Paper":"1 Pack","Paper Towels":"1 Pack","Do I have a Membership":True}
#
#database.child("Groceries").child("Costco").child().set(data)

#Update Data
#--------------------------------------------------------------------------------------------

""" database.child("Groceries").child("Walmart").child("Cheese").child("Havarti").remove()

database.child("Groceries").child("Walmart").child("Cheese").child("Havarti Slices").set("2 Packs")



database.child("Groceries").child("Walmart").child("Potatoes").set("1 Sack")
database.child("Groceries").child("Costco").child("Sack of Flour").set(2)
 """

database.child("Groceries").child("Walmart").child("Cheese").update({"Cheddar":"1 Block"})


#Delete Data
#--------------------------------------------------------------------------------------------
#database.child("-NifNp-VuKu1-g896Tqd").remove() - This was data ={"Name":"Zach","Age":20,"Likes Pizza":True}



#Read Data
#--------------------------------------------------------------------------------------------

shopping_list = database.child("Groceries").get()
print(shopping_list.val())

""" raw_data = database.get() """

""" data = raw_data.val()
print(data)
print("\n") """

""" data = raw_data.each()[0]
print(f"{data.val()}{data.key()}") """

#In the Words of Iskall85:
#--------------------------------------------------------------------------------------------
print("Great Success!")