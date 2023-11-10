#Import Libraries
import pyrebase

#Create Access to Database
#---------------------------------------------------------------------------------------------------------------------------------
firebaseConfig = {
    "apiKey": "AIzaSyDLVNQEQCPfqkWNzRlvqhiwjp3mJUIZ3Y0",
    "authDomain": "eventmanager128-57f00.firebaseapp.com",
    "databaseURL": "https://eventmanager128-57f00-default-rtdb.firebaseio.com",
    "projectId": "eventmanager128-57f00",
    "storageBucket": "eventmanager128-57f00.appspot.com",
    "messagingSenderId": "890938382710",
    "appId": "1:890938382710:web:979bb9255ff02cc1ae4257",
    "measurementId": "G-P76K3ELD8Q"
}
#Initialize App
firebase = pyrebase.initialize_app(firebaseConfig)
#Access Database
database = firebase.database()

#test connections
#---------------------------------------------------------------------------------------------------------------------------------
    #test = {"Happy Birthday":"Samantha!"}
    #database.child("Test").set(test)
    #database.child("Test").remove()

#Create Database Structure
#---------------------------------------------------------------------------------------------------------------------------------
#Dummy event used to populate database with master directory and key data 
dummy_data = {"Name":"2 Dummies Concert",
    "Type":"Concert",
    "Summary":"Dummy Event for testing purposes",
    "Venue":"Joplin Concert Hall",
    "Address":"1055 Finn Street",
    "Date":"December 16th 2023",
    "Time":"6PM CST",
    "Employees":{"Lead":"Gerald Fitzwillager","MC":"Mike Jones","Venue Coordinator":"Samantha Jones","Security":"Contractor - Edward's Security Corp"},
    "Client":"Big Record.Co",
    "Attendees":["2 Dummies", "Mr. AgentManSir","Audience"],
    "Resources":{"In House":"#Inventory Link","3rd Party":{"Audio Equipment":"Venue","Security Contractor":"Edward's Security Corp","Refresments":"Zach Co. Snacks","Ticket Booth and Refresments Staff":"Venue"}},
    "Requirements":{"Audio Equipment":True,"Security":True,"Ticket Booth":False,"Refresments":False},
    "Checklist":{"Set up Audio Equipment":True,"Hire Security Contractor":True,"Set Up ticket Booth":False,"Acquire Refreshments":False,"Clean Venue":False}
    }
database.child("Master").child("Dummy").set(dummy_data)
#"":"",

#---------------------------------------------------------------------------------------------------------------------------------
print("Great Success!")