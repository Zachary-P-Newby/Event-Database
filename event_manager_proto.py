#Import Libraries
import pyrebase

def connect_to_database():
    #Create Access to Database
    firebaseConfig = {
    "apiKey": "AIzaSyDLVNQEQCPfqkWNzRlvqhiwjp3mJUIZ3Y0",
    "authDomain": "eventmanager128-57f00.firebaseapp.com",
    "databaseURL": "https://eventmanager128-57f00-default-rtdb.firebaseio.com",
    "projectId": "eventmanager128-57f00",
    "storageBucket": "eventmanager128-57f00.appspot.com",
    "messagingSenderId": "890938382710",
    "appId": "1:890938382710:web:979bb9255ff02cc1ae4257",
    "measurementId": "G-P76K3ELD8Q"}
    #Initialize App

    firebase = pyrebase.initialize_app(firebaseConfig)
    
    return firebase.database()

    


#Functions
def event_manger_help():
    #Print list of common functions
    print("""
> database_overview
    Print overview of database structure and event object values
>list_events(database)
    Print list of all events 
>
>
>
>
>
""")

def database_overview():
    #Print overview of database structure and event object values
    print("Databse Overview:\n")
    print("""Master: - Master directory contains all events
          
            Event: - each event directory contains the following:

            * Name - Event Title (ie. Johnson Wedding Convention)
          
            * Type - Type of event (ie. Concert, Party, Reception)
          
            * Summary - Event Summary
          
            * Venue - Location of Event
          
            * Address - Venue Address
          
            * Date - Date of event
          
            * Time - Event Time (ie. 12:00PM, 6-10PM, 9AM-5PM)

            * Client - Client Name and Information

            * Attendee list - List of All Attendees

            * Hosting Employees - Sub dirctory - Titles and names of employees hosting event.

            * Resources - Sub-Directory - Resources avilible for Event
                * In house - What we have at the Office
                * Availible - What is availible from 3rd Party Vendors

            * Requirements - Sub-Directory - Event Requirements
                * Each Item has a name and boolean value signifying whether or not it has been acquired

            * Checklist - Sub-Directory - list of tasks to be completed
                * Each Task has a name and boolean value signifying whether or not it has been completed
          """)


def list_events(database):
    #Print list of all events
    print("Databse Overview:")
    print("Events:")

    for i in database.child("Master").get().val():
        print(f"> {i}")



def create_event(database):
    """ Create a New Event """

    def _create_event(database,event):
        database.child(event["Name"]).set()

    print(""*5)
    event = dict()
    
    print("Enter Event Initialization Information:")
    event["Name"] = input("Enter Event Name: ")
    event["Type"] = input("Enter Event Summary: ")
    event["Venue"] = input("Enter Event Venue: ")
    event["Address"] = input("Enter Event Address: ")
    event["Client"] = input("Enter Event Client: ")

    
    _create_event(database,event)
    print("Event Created Successfully. Use update_event to fill in remaining data.")


#Main
def main():

    database = connect_to_database()
    create_event(database)
    
    print("\nGreat Success!")

#Run Program
if __name__ == "__main__":
    main()