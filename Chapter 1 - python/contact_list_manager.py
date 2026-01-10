"""
Question 8: Contact List Manager
Task: Manage contacts with add, search, update, and delete operations.
Concepts Covered: Lists, Dictionaries, Functions, Loops, Conditionals, Input/Output

"""

def add_contact(contact,name,phone,email):
    """Add a new contact to the list"""
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
    return f"Contact '{name}' added successfully"

def search_contacts(contacts,search_term):
    """Search Contacts by name"""
    search_term = search_term.lower()
    results = []

    for contact in contacts:
        if search_term in contact['name'].lower():
            results.append(contact)

    return results
    

def display_contact(contact, index=None):
    """Display a signle contact"""
    if index is not None:
        print(f"\n[{index}] {contact['name']}")
    else:
        print(f"\n{contact['name']}")
    print(f" Phone: {contact['phone']}")
    print(f" Email: {contact['email']}")


def delete_contact(contacts,index):
    """Delete contact by index"""
    if 0 <= index < len(contacts):
        deleted = contacts.pop(index)
        return True, f" Contact '{deleted['name']}' deleted"
    return False, "x Invalid contact number"

#Main Program
contacts = []

print("== CONTACT MANAGER ===")
print("Commands: add, search, list, delete, quit\n")

while True: 
    command = input("Command: ").lower().strip()

    if command == 'quit':
        print("Goodbye!")
        break

    elif command == "add":
        name = input(" Name: ").strip()
        phone = input(" Phone: ").strip()
        email = input(" Email: ").strip()

        if name and phone:
            message = add_contact(contacts, name, phone, email)
            print(f" {message}\n")
        else:
            print(" x Name and phone are required\n")

    elif command == "search":
        search_term = input(" Search name: ").strip()
        results = search_contacts(contacts, search_term)

        if results: 
            print(f"\n Found{len(results)} contact(s):")
            for i, contact in enumerate(results):
                display_contact(contact, i)

        else:
            print(" x No contacts found\n")

    
    elif command == 'list':
        if contacts:
            print(f"\n Total contacts: {len(contacts)}")
            for i, contact in enumerate(contacts):
                display_contact(contact, i)
        else:
            print(" X No contacts yet\n")

    elif command == 'delete':
        if not contacts:
            print(" x No contacts to delete\n")
            continue

        #show all contacts first
        print("\n Current contacts:")
        for i, contact in enumerate(contacts):
            print(f"   [{i}] {contact['name']}")

        try:
            index = int(input("Enter Contact number to delete: "))
            success, message = delete_contact(contacts,index)
            print(f"  {message}\n")
        except ValueError:
            print(" X Please enter a valid number\n")

    else:
        print(" X Unknown command. Use: add, search, list, delete, quit\n")




"""

Code Explnanation - 

Explanation:
Function 1: add_contact()
pythondef add_contact(contacts, name, phone, email):

Function: Add new contact
Parameters:

contacts - list to add to
name, phone, email - contact details



python    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }

Dictionary: Create contact object
Each contact has three fields

python    contacts.append(contact)

List method: Add contact to list
Important: Lists are mutable, so changes affect original list

python    return f"✓ Contact '{name}' added successfully"

Return: Success message with name


Function 2: search_contacts()
pythondef search_contacts(contacts, search_term):
    search_term = search_term.lower()
    results = []

Function: Find matching contacts
String method: .lower() for case-insensitive search
List: Store matching results

python    for contact in contacts:
        if search_term in contact['name'].lower():
            results.append(contact)

Loop: Check each contact
Conditional: Check if search term is in name
String check: 'john' in 'john smith'.lower() → True

python    return results

Return: List of matching contacts (may be empty)


Function 3: display_contact()
pythondef display_contact(contact, index=None):

Function: Format and print contact
Default parameter: index=None makes it optional

python    if index is not None:
        print(f"\n[{index}] {contact['name']}")
    else:
        print(f"\n{contact['name']}")

Conditional: Show index if provided
is not None checks if value was given

python    print(f"  Phone: {contact['phone']}")
    print(f"  Email: {contact['email']}")

Dictionary access: Get values by keys


Function 4: delete_contact()
pythondef delete_contact(contacts, index):
    if 0 <= index < len(contacts):

Function: Remove contact by position
Conditional: Check if index is valid
0 <= index < len(contacts) checks both bounds
Example: If 5 contacts, valid indices are 0, 1, 2, 3, 4

python        deleted = contacts.pop(index)

List method: .pop(index) removes and returns item
deleted now holds the removed contact

python        return True, f"✓ Contact '{deleted['name']}' deleted"
    return False, "✗ Invalid contact number"

Return tuple: Success/failure + message


Main Program:
pythoncontacts = []

List: Start with empty contact list

pythonwhile True:
    command = input("Command: ").lower().strip()

Loop: Keep running until quit
String methods:

.lower() - make lowercase
.strip() - remove extra spaces



python    if command == 'quit':
        print("Goodbye!")
        break

Conditional: Exit program

python    elif command == 'add':
        name = input("  Name: ").strip()
        phone = input("  Phone: ").strip()
        email = input("  Email: ").strip()

elif: "else if" - checked after previous if
Input: Get contact details

python        if name and phone:
            message = add_contact(contacts, name, phone, email)
            print(f"  {message}\n")

Conditional: Validate required fields
if name and phone: checks both are not empty
Function call: Add the contact

python    elif command == 'search':
        search_term = input("  Search name: ").strip()
        results = search_contacts(contacts, search_term)

Function call: Search contacts

python        if results:
            print(f"\n  Found {len(results)} contact(s):")
            for i, contact in enumerate(results):
                display_contact(contact, i)

Conditional: Check if results found
Loop: Display each result
enumerate(): Get index and contact

python    elif command == 'delete':
        if not contacts:
            print("  ✗ No contacts to delete\n")
            continue

Conditional: Check if list is empty
not contacts is True if list is empty
continue: Skip rest and start next loop iteration

python        for i, contact in enumerate(contacts):
            print(f"    [{i}] {contact['name']}")

Loop: Show all contacts with numbers

python        try:
            index = int(input("  Enter contact number to delete: "))
            success, message = delete_contact(contacts, index)
            print(f"  {message}\n")
        except ValueError:
            print("  ✗ Please enter a valid number\n")
```
- **try-except:** Handle invalid input
- **int():** Convert string to number (may fail)
- **ValueError:** Raised if conversion fails

**Example Run:**
```
=== CONTACT MANAGER ===
Commands: add, search, list, delete, quit

Command: add
  Name: John Smith
  Phone: 555-1234
  Email: john@example.com
  ✓ Contact 'John Smith' added successfully

Command: add
  Name: Alice Johnson
  Phone: 555-5678
  Email: alice@example.com
  ✓ Contact 'Alice Johnson' added successfully

Command: search
  Search name: john

  Found 2 contact(s):

[0] John Smith
  Phone: 555-1234
  Email: john@example.com

[1] Alice Johnson
  Phone: 555-5678
  Email: alice@example.com

Command: list

  Total contacts: 2

[0] John Smith
  Phone: 555-1234
  Email: john@example.com

[1] Alice Johnson
  Phone: 555-5678
  Email: alice@example.com

Command: delete

  Current contacts:
    [0] John Smith
    [1] Alice Johnson
  Enter contact number to delete: 0
  ✓ Contact 'John Smith' deleted

Command: quit
Goodbye!


"""
