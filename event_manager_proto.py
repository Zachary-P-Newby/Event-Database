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
    print("\nAll Events:")

    for i in events:
        print(f"> {i}")

def read_event():
    """print out information on an event"""
    print("\nReading Event\n")

    event = _select_event()
    if event == "quit":
        print("Reading Cancelled")
        return None
    else:
        
        print("Event Overview:\n")
        print(f"""{event["NAME"]}:
* Type: {event["TYPE"]}
* Summary: {event["SUMMARY"]}
* Venue - {event["VENUE"]}
* Address - {event["ADDRESS"]}
* Date - {event["DATE"]}
* Time - {event["TIME"]}
* Client - {event["CLIENT"]}
""")
        
        #["NAME","TYPE","SUMMARY","VENUE","ADDRESS","DATE","TIME","CLIENT","ATTENDEES","EMPLOYEES","REQUIREMENTS","TASKS"]
    print("Employees:")
    for key in event["EMPLOYEES"]:
        print(f"    * {key} - {event["EMPLOYEES"][key]}")

    print("Attendees:")
    for key in event["ATTENDEES"]:
        print(f"    * {key} - {event["ATTENDEES"][key]}")

    print("Requirements:")
    for key in event["REQUIREMENTS"]:
        print(f"    * {key} - {event["REQUIREMENTS"][key]}")

    print("Checklist:")
    for key in event["TASKS"]:
        print(f"    * {key} - {event["TASKS"][key]}")

def create_event(database):
    """ Create a New Event """

    #Nested Functions
    def _create_checklist(element):
        print(f"\nAdding Items to {element}")
        checklist = dict()
        active = True

        if element == "ATTENDEES":
            print("Enter name and statement (true or false) indicating if they have RSVP'd. If the event is open to the public, include, open as key, and true as value.\n(enter quit as name to stop)")
        elif element == "REQUIREMENTS":
            print("Enter required good or service and statement (true or false) indicating if it has been acquired.\n(enter quit as requirement to stop)")
        else:
            print("Enter task and statement (true or false) indicating if it has been completed\n(enter quit as task to stop)")
        
        while active:

            key = input("Enter key: ")
            if key.lower() == "quit":
                print("Appending items finished")
                
                if checklist == {}:
                    checklist['Placeholder'] = "Add Data here"
                return checklist                

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

    def _create_employees():
        print("\nAdding Employees Assigned to Event:")
        employees = dict()
        active = True
        print("Enter name and posistion, enter quit as name to stop")
        while active:
            name = input("Enter name: ")
            if name.lower() == "quit":
                print("Appending items finished")
                if employees == {}:
                    employees["Placeholder"] = "Add data here"
                return employees
            
            else:
                value = input("Enter posistion: ")
                employees[name] = value

    def _create_event(database,event):
        events[event["NAME"]] = event
        database.child(event["NAME"]).set(event)
    #Function Body
    print("\nCreating Event\n")
    event = dict()
    
    print("Enter Event Initialization Information:")

    active = True
    while active:
        name = input("Enter Event NAME: ('quit' to cancel) ")
        if "." in name:
            print("Invalid name, '.' cannot be in event name. Enter again")
            continue
        elif name.lower() == "quit":
            print('Event Creation Cancelled')
            return None
        else:
            event["NAME"] = name
            break

    event["TYPE"] = input("Enter the type of the event (ie. party, wedding, tournament): ")

    event["SUMMARY"] = input("Enter Event Summary: ")

    event["VENUE"] = input("Enter Event Venue: ")

    event["ADDRESS"] = input("Enter Event Address: ")

    event["DATE"] = input("Enter Event Date: ")

    event["TIME"] = input("Enter Event Time: ")

    event["CLIENT"] = input("Enter Event Client: ")

    print("Adding sub directories - checklists and employees")

    event["ATTENDEES"] = _create_checklist("ATTENDEES")

    #event["Employees"] = dict()
    event["EMPLOYEES"] = _create_employees()

    event["REQUIREMENTS"] = _create_checklist("REQUIREMENTS")

    event["TASKS"] = _create_checklist("TASKS")
    
    _create_event(database,event)
    print("Event Successfully Created.")

    
                
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
                print("\nChecking off item")
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
                continue

            elif option == "2":
                print("\nAdding Items")
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
                continue 
            
            elif option == "3":
                print("\nRemoving Items")
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
                continue 
            
            elif option.lower() == "quit":
                print("Operation finished")
                running = False
                return checklist
            else:
                print("Invalid input, try again")
                continue 
    

    def _update_employees(employees):
        print("\nUpdating Employees")
        running = True
        while running:
            print("\nSelect an option")
            option = input("""    1. Add Employee
    2. Remove Employee
    quit - quit operation
    Option: """)
            if option == "1":
                print("\nAdding Employees")
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
                continue 
            
            elif option == "2":
                print("\nRemoving Employees")
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
                continue                        
            
            elif option.lower() == "quit":
                print("Operation finished")
                running = False
                return employees
            else:
                print("Invalid input, try again")
                continue 

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
                event[element] = _enter_data(element)
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

def _select_element():
    """ Select an element """
    running = True
    while running:
        print("Select an element:")
        element = input("Enter 'quit' to Cancel: ")
        if element.upper() in event_elements:
            return element.upper()
        elif element.lower() == "quit":
            return "quit"
        else:
            print("Invalid Input, Please Re-enter")
            continue

def _create_event_dict(database):
    """ creates dict containing all events """
    data = database.get().val()
    #Error handling if databse is empty
    if data == None:
        print("Empty")
        database.child("Init_dummy").set({"NAME":"Init_Dummy","Dummy":"Stand-in value for initialization"})
        return _create_event_dict(database)
    else:
        return dict(data)




#Main
def main():

    global database
    database = connect_to_database()

    global events
    events = _create_event_dict(database)

    global event_elements 
    event_elements = ["NAME","TYPE","SUMMARY","VENUE","ADDRESS","DATE","TIME","CLIENT","ATTENDEES","EMPLOYEES","REQUIREMENTS","TASKS"]

    global checklists
    checklists = ["ATTENDEES","REQUIREMENTS","TASKS"]

    database_overview()
    """ create_event(database) """
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
