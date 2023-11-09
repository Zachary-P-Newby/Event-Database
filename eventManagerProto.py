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

#Functions






#Main
def main():
    print("Great Success!")

#Run Program
if __name__ == "__main__":
    main()