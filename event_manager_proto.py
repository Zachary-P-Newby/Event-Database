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
> database_overview - Print overview of database structure and event object values
> list_events - Print list of all events 
> create_event - Create a new event
> delete_event - Delete an event
> update_event - Update data or add new data to an exsisting event
> 
>
""")

def database_overview():
    #Print overview of database structure and event object values
    print("\nDatabase Overview:\n")
    print("""Master: - Master directory contains all events
    Event: - each event directory contains the following:
    * NAME - Event Title (ie. Johnson Wedding Convention)
    
    * TYPE - TYPE of event (ie. Concert, Party, Reception)
    
    * SUMMARY - Event Summary
    
    * Venue - Location of Event
    
    * Address - Venue Address
    
    * Date - Date of event
    
    * Time - Event Time (ie. 12:00PM, 6-10PM, 9AM-5PM)
    * Client - Client Name and Information
    * Attendee list - List of All Attendees and whether or not they have arrived
    * Employees - Sub dirctory - Names and posistions of employees hosting event.
    * Requirements - Sub-Directory - Event Requirements
        * Each Item has a name and boolean value signifying whether or not it has been acquired
    * Checklist - Sub-Directory - list of tasks to be completed
        * Each Task has a name and boolean value signifying whether or not it has been completed
          """)

def list_events():
    """Print list of all events"""
    print("\nDatabse Overview:\n")
    print("Events:")

    for i in events:
        print(f"> {i}")

def read_event():
    """print out information on an event"""
    print("\nReading Event\n")

    event = _select_event()
    if event == "quit":
        print("Reading Cancelled")
    else:
        print("Event Overview:\n")
        print(f"""{event["NAME"]}:
* TYPE: {event["TYPE"]}
* Summary: {event["SUMMARY"]}
* Venue - {event["Venue"]}
* Address - {event["Address"]}
* Date - {event["Date"]}
* Time - {event["Time"]}
* Client - {event["Client"]}
""")
    print("Employees:")
    for key in event["Employees"]:
        print(f"    * {key} - {event["Employees"][key]}")

    print("Attendees:")
    for key in event["Attendees"]:
        print(f"    * {key} - {event["Attendees"][key]}")

    print("Requirements:")
    for key in event["Requirements"]:
        print(f"    * {key} - {event["Requirements"][key]}")

    print("Checklist:")
    for key in event["Checklist"]:
        print(f"    * {key} - {event["Checklist"][key]}")

def create_event(database):
    """ Create a New Event """
    print("\nCreating Event\n")
    event = dict()
    
    print("Enter Event Initialization Information:")

    event["NAME"] = input("Enter Event NAME: ")

    event["TYPE"] = input("Enter the type of the event (ie. party, wedding, tournament): ")

    event["SUMMARY"] = input("Enter Event Summary: ")

    event["VENUE"] = input("Enter Event Venue: ")

    event["ADDRESS"] = input("Enter Event Address: ")

    event["DATE"] = input("Enter Event Date: ")

    event["TIME"] = input("Enter Event Time: ")

    event["CLIENT"] = input("Enter Event Client: ")

    print("Adding sub directories - checklists and employees, each must have at least one value to be saved to database")

    event["ATTENDEES"] = _add_checklist("ATTENDEES")

    #event["Employees"] = dict()
    event["EMPLOYEES"] = _add_employees()

    event["REQUIREMENTS"] = _add_checklist("REQUIREMENTS")

    event["TASKS"] = _add_checklist("TASKS")



    def _create_event(database,event):
        events[event["NAME"]] = event
        database.child(event["NAME"]).set(event)
    
    _create_event(database,event)
    print("Event Created Successfully. Use update_event to fill in remaining data.")

    def _add_checklist(element):
        print(f"Adding Items to {element}")
        checklist = dict()
        active = True
        print("Enter keys and status value (true or false) enter quit as key to stop")
        while active:
            key = input("Enter key: ")
            if key.lower() == "quit":
                print("Appending items finished")
                active = False
            else:
                value = input("Enter status - f for false, t for true, false by default: ")
                if value.lower() == "f":
                    checklist[key] = False
                    continue
                elif value.lower() == "t":
                    checklist[key] = True
                    continue
                else:
                    print("Invalid input, entering false")
                    checklist[key] = False
                    continue
    
    def _add_employees():
        print("Adding Employees Assigned to Event:")
        employees = dict()
        active = True
        print("Enter name and posistion, enter quit as name to stop")
        while active:
            name = input("Enter name: ")
            if name.lower() == "quit":
                print("Appending items finished")
                active = False
                return employees
            else:
                value = input("Enter posistion: ")
                employees[name] = value
                
#______________________________________________________________________________________________

def delete_event(database):
    print("\nDeleting Event\n")
    """ Delete an event """
    print("Warning: This is permanent")
    print("Enter 'quit' to cancel")
    event = _select_event()
    if event == "quit":
        print("Deletion Cancelled")
    else:
        database.child(event["NAME"]).remove()
        del(events[event["NAME"]])


def update_event(database):
    """ Update an Event """
    print("\nUpdating Event\n")
    #Nested functions
    #__________________________
    

    def _update_event(database, event):
        database.child(event["NAME"]).set(event)   
    #Select element to update

    
    
    def _select_element():
        
        running = True
        while running:
            print("Select an event element to update")
            child = input("Enter 'quit' to Cancel: ")
            if child.upper() in event_elements:
                return child
            elif child.lower() == "quit":
                return "quit"
            else:
                print("Invalid Input, Please Re-enter")
                continue
    
    def _enter_data(element):
        print("")
        data = input(f"Enter New Value for {element}: ")
        return data

    def _update_checklist(checklist):
        print(f"Updating {checklist}")
        running = True
        while running:
            print("\nSelect an option")
            option = input("""    1. Check off item
    2. Add items
    3. Remove items
    quit - quit operation
    Option: 
""")
            
            if option == "1":
                print("Checking off item")
                item = input("\nEnter item key: ")
                if item in checklist:
                    if checklist[item] == False:
                        checklist[item] = True
                        print("Set to True")
                    else:
                        checklist[item] = False
                        print("Set to False")
                else:
                    print("Invalid input")
                    continue

            elif option == "2":
                print("Adding Items")
                active = True
                print("Enter keys and values (enter quit as key to stop)")
                while active:
                    key = input("Enter key: ")
                    if key.lower() == "quit":
                        print("Appending items finished")
                        active = False
                    else:
                        value = input("Enter status - f for false, t for true, false by default: ")
                        if value.lower() == "f":
                            checklist[key] = False
                            continue
                        elif value.lower() == "t":
                            checklist[key] = True
                            continue
                        else:
                            print("Invalid input, entering false")
                            checklist[key] = False
                            continue
            
            elif option == "3":
                print("Removing Items")
                active = True
                print("Enter keys of items you wish to remove, enter quit to stop")
                while active:
                    key = input("Enter key: ")
                    if key.lower() == "quit":
                        print("Appending items finished")
                        active = False
                    elif key not in checklist:
                        print("Invalid key, Please re-enter")
                        continue
                    else:
                        del(checklist[key])
                        print(f"{key} removed.")
            
            elif option.lower() == "quit":
                print("Operation finished")
                running = False
                return checklist
            else:
                print("Invalid input, try again")
    

    def _update_employees(employees):
        print("Updating Employees")
        running = True
        while running:
            print("\nSelect an option")
            option = input("""    1. Add Employee
    2. Remove Employee
    quit - quit operation
    Option: """)
            if option == "1":
                print("Adding Employees")
                active = True
                print("Enter names and posistions (enter quit as name to stop)")
                while active:
                    name = input("Enter name: ")
                    if name.lower() == "quit":
                        print("Appending items finished")
                        active = False
                        return employees
                    else:
                        value = input("Enter posistion: ")
                        employees[name] = value
            
            elif option == "2":
                print("Removing Employees")
                active = True
                print("Enter names of employees you wish to remove from the event, enter quit as a name to stop")
                while active:
                    name = input("Enter name: ")
                    if name.lower() == "quit":
                        print("Appending items finished")
                        active = False
                        return employees
                    elif name not in employees:
                        print("Invalid name, Please re-enter")
                        continue
                    else:
                        del(employees[name])
                        print(f"{name} removed.")
            
            elif option.lower() == "quit":
                print("Operation finished")
                running = False
                return employees
            else:
                print("Invalid input, try again")
#-------------------------------------------

    

    #________________________________
    print(""*5)

    event = _select_event()
    if event == "quit":
        print("Update Cancelled")
    else:
        element = _select_element()
        if element == "quit":
            print("Update Cancelled")
        else:

            if element in checklists:
                event[element] = _update_checklist(event[element])
            elif element == "EMPLOYEES":
                event["EMPLOYEES"] == _update_employees(event["EMPLOYEES"])
            else:
                event[element] = _enter_data()
            _update_event(database, event)

            
    

def _select_event():
    """Hidden dunction used for selecting events"""
    running = True
    while running:
        print("Select an event")
        event_NAME = input("Enter 'quit' to Cancel: ")
        if event_NAME in events:
            return events[event_NAME]
        elif event_NAME.lower() == "quit":
            return "quit"
        else:
            print("Invalid Input, Please Re-enter")
            continue

def _create_event_dict(database):
    #creates dict containing all events
    return dict(database.get().val())



#Main
def main():

    database = connect_to_database()

    global events
    events = _create_event_dict(database)

    global event_elements 
    event_elements = ["NAME","TYPE","SUMMARY","VENUE","ADDRESS","DATE","TIME","CLIENT","ATTENDEES","EMPLOYEES","REQUIREMENTS","TASKS"]

    global checklists
    checklists = ["ATTENDEES","REQUIREMENTS","TASKS"]

    database_overview()
    create_event(database)
    create_event(database)
    list_events()
    read_event()
    update_event(database)
    read_event()
    delete_event(database)
    list_events()

    print("\nGreat Success!")

#Run Program
if __name__ == "__main__":
    main()


"""
             
              """