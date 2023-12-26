

def menue():
     print("***Diary Application**")
     print("1. View entry")
     print("2. Add entry")
     print("3. Edit entry")
     print("4. Delete entry")
     print("5. Exit")
menue()


def Add_entry():
    while True:
        event = input("Enter an event for your diary: ")
        print("Event added successfully!\n")
        return event
        
        
        
def add_entry():
    entries = []

    while True:
        event = input("Enter an event for your diary (type 'complete' to finish): ")
        if event.lower() == 'complete':
            break
        entries.append(event)
        print("Event added successfully!\n")

    return entries

user_entries = add_entry()
print("User entries:", user_entries)

    
    
def view_entries(event):
    if not add_entry:
        print("No entries available.")
        return

    for i, entry in enumerate(entry, 7):
        print(f"Entry {i}:\n{entry}\n")



def edit_latest_entry():
    global latest_entry
    if latest_entry:
        edited_entry = input("Enter the edited diary entry: ")
        latest_entry[-1] = edited_entry
        latest_entry = edited_entry
        print("Latest entry edited successfully!")
    else:
        print("No entry available to edit. Please add an entry first.")


def  Delete_entry():
       pass



def exit_diary():
    print("Exiting Diary Application. Goodbye!")
    exit()  