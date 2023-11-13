# Overview

To imrpove my skills as a software engineer I have created a simple python and ggogle firbase program for event planning to learn how to work with Google Firbase using the Pyrebase4 Library.

My program is a simple event planner, use for storing and retreiving information on events such as parties, weddings, funerals, conventions, business meetings, etc. Users can create, modify, delete, and read data from a central databse in real time allowing them to track progress on an event, see the key details, and what needs to be done. The results are printed to the console or terminal.

My purpose in creating this software was to learn how to work with JSON based real time databases in python to improve my knowledge and skills.


[Software Demo Video](https://youtu.be/7tqUxpK2ae4)

# Cloud Database

For this program I used Google Firebase for my databse and the Python Pyrebase Library (specifically the pyrebase-4 fork) to interact with it in Python

Database structure:

Master: - Master directory contains all events
    Event: - each event directory contains the following:
    
    * NAME - Event Title (ie. Johnson Wedding Convention)
    
    * TYPE - TYPE of event (ie. Concert, Party, Reception)
    
    * SUMMARY - Event Summary
    
    * Venue - Location of Event
    
    * Address - Venue Address
    
    * Date - Date of event
    
    * Time - Event Time (ie. 12:00PM, 6-10PM, 9AM-5PM)
          
    * Client - Client Name and Information
    
    * Employees - Sub dirctory - Names and posistions of employees hosting event. 

    * Attendees - Sub dirctory - List of All Attendees and whether or not they have arrived
          
    * Requirements - Sub-Directory - Event Requirements and whether or not they have arrived
    
    * Tasks - Sub-Directory - checklist of tasks to be completed



# Development Environment

I used vsCode as my text editor.
For the program I used the Python programming language and the the Pyrebase4 Library to access the database.

# Useful Websites

- [Firebase Docs](https://firebase.google.com/docs)
- [Firestore Docs](https://firebase.google.com/docs/firestore)
- [Connecting Firebase Realtime Database To Python: Creating, Reading, Updating, and Deleting Data](https://www.youtube.com/watch?v=DCaH4bQ4DxA&list=WL&index=36&t=791s)
- [Firebase in 100 Seconds](https://www.youtube.com/watch?v=vAoB4VbhRzM&list=WL&index=35)
- [Module collections has no attribute 'MutableMapping' [Fixed]](https://bobbyhadz.com/blog/python-attributeerror-module-collections-has-no-attribute-mutablemapping#:~:text=To%20solve%20the%20"AttributeError%3A%20module%20collections%20has%20no,3.9%20if%20you%20are%20unable%20to%20make%20corrections.)
- [Python requests ImportError: cannot import name HeaderParsingError](https://stackoverflow.com/questions/32986626/python-requests-importerror-cannot-import-name-headerparsingerror)
- [Installing multiple versions of a package with pip](https://stackoverflow.com/questions/6570635/installing-multiple-versions-of-a-package-with-pip)
- [Firebase Admin Python SDK](https://firebase.google.com/docs/reference/admin/python/)
- [PyPi - firebase 4.0.1](https://pypi.org/project/firebase/)
- [Pyrebase4 - Repo](https://github.com/nhorvath/Pyrebase4)
- [Web Site Name](https://softwareengineering.stackexchange.com/questions/308972/python-file-naming-convention#:~:text=So%20PEP%208%20tells%20you%20that%3A%201%20modules,underscores%3B%203%20classes%20should%20use%20the%20CapWords%20convention.)
- [How can I write a `try`/`except` block that catches all exceptions?](https://stackoverflow.com/questions/4990718/how-can-i-write-a-try-except-block-that-catches-all-exceptions)
# Future Work
- Figure out how to handle connection Errors
- Add ability to write to txt and json files to store data in them 
- Expand functionality of the read_database Function to only view one element of an event at a time.