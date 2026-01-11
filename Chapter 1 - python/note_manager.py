"""
Docstring for Chapter 1 - python.note_manager
"""



from datetime import datetime

def create_note(notes, title, content, tags=None):
    """Create a new note"""
    note = {
        'title': title,
        'content': content,
        'tags': tags if tags else [],
        'created': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'modified': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'id': len(notes) + 1
    }
    notes.append(note)
    return note

def edit_note(notes, note_id, new_content):
    """Edit note content"""
    for note in notes:
        if note['id'] == note_id:
            note['content'] = new_content
            note['modified'] = datetime.now().strftime('%Y-%m-%d %H:%M')
            return True, note
    return False, None

def delete_note(notes, note_id):
    """Delete a note"""
    for i, note in enumerate(notes):
        if note['id'] == note_id:
            deleted = notes.pop(i)
            return True, deleted
    return False, None

def search_notes(notes, keyword):
    """Search notes by keyword in title or content"""
    results = []
    keyword_lower = keyword.lower()
    
    for note in notes:
        if (keyword_lower in note['title'].lower() or 
            keyword_lower in note['content'].lower()):
            results.append(note)
    
    return results

def get_notes_by_tag(notes, tag):
    """Get all notes with specific tag"""
    return [note for note in notes if tag.lower() in [t.lower() for t in note['tags']]]

def display_notes(notes, title="ALL NOTES"):
    """Display notes list"""
    if not notes:
        print("\n  No notes found.\n")
        return
    
    print("\n" + "="*80)
    print(f"{title:^80}")
    print("="*80)
    
    for note in notes:
        print(f"\n[#{note['id']}] {note['title']}")
        print(f"Created: {note['created']} | Modified: {note['modified']}")
        
        if note['tags']:
            tags_str = ", ".join(note['tags'])
            print(f"Tags: {tags_str}")
        
        content_preview = note['content'][:100] + "..." if len(note['content']) > 100 else note['content']
        print(f"{content_preview}")
        print("-" * 80)
    
    print()

def display_note_full(note):
    """Display full note content"""
    print("\n" + "="*80)
    print(f"[#{note['id']}] {note['title']}")
    print("="*80)
    print(f"Created: {note['created']}")
    print(f"Modified: {note['modified']}")
    
    if note['tags']:
        print(f"Tags: {', '.join(note['tags'])}")
    
    print("\n" + note['content'])
    print("="*80 + "\n")

# Main program
notes = []

print("=== NOTE MANAGER ===")
print("Commands: create, list, view, edit, delete, search, tags, quit\n")

while True:
    command = input("Command: ").lower().strip()
    
    if command == 'quit':
        print("Goodbye!")
        break
    
    elif command == 'create':
        title = input("  Title: ").strip()
        
        if not title:
            print("  ✗ Title cannot be empty\n")
            continue
        
        print("  Content (type 'END' on new line when done):")
        content_lines = []
        while True:
            line = input()
            if line == 'END':
                break
            content_lines.append(line)
        
        content = "\n".join(content_lines)
        
        if not content:
            print("  ✗ Content cannot be empty\n")
            continue
        
        tags_input = input("  Tags (comma-separated, or press Enter to skip): ").strip()
        tags = [tag.strip() for tag in tags_input.split(',')] if tags_input else []
        
        note = create_note(notes, title, content, tags)
        print(f"  ✓ Note #{note['id']} created\n")
    
    elif command == 'list':
        display_notes(notes)
    
    elif command == 'view':
        if not notes:
            print("  ✗ No notes available\n")
            continue
        
        try:
            note_id = int(input("  Note ID: "))
            
            note = None
            for n in notes:
                if n['id'] == note_id:
                    note = n
                    break
            
            if note:
                display_note_full(note)
            else:
                print(f"  ✗ Note #{note_id} not found\n")
                
        except ValueError:
            print("  ✗ Invalid ID\n")
    
    elif command == 'edit':
        if not notes:
            print("  ✗ No notes to edit\n")
            continue
        
        try:
            note_id = int(input("  Note ID: "))
            
            print("  New content (type 'END' on new line when done):")
            content_lines = []
            while True:
                line = input()
                if line == 'END':
                    break
                content_lines.append(line)
            
            new_content = "\n".join(content_lines)
            
            if not new_content:
                print("  ✗ Content cannot be empty\n")
                continue
            
            success, note = edit_note(notes, note_id, new_content)
            
            if success:
                print(f"  ✓ Note updated\n")
            else:
                print(f"  ✗ Note not found\n")
                
        except ValueError:
            print("  ✗ Invalid ID\n")
    
    elif command == 'delete':
        if not notes:
            print("  ✗ No notes to delete\n")
            continue
        
        try:
            note_id = int(input("  Note ID: "))
            
            success, note = delete_note(notes, note_id)
            
            if success:
                print(f"  ✓ Note deleted: {note['title']}\n")
            else:
                print(f"  ✗ Note not found\n")
                
        except ValueError:
            print("  ✗ Invalid ID\n")
    
    elif command == 'search':
        keyword = input("  Search keyword: ").strip()
        
        if not keyword:
            print("  ✗ Keyword cannot be empty\n")
            continue
        
        results = search_notes(notes, keyword)
        
        if results:
            display_notes(results, f"SEARCH RESULTS: '{keyword}'")
        else:
            print(f"  ✗ No notes found matching '{keyword}'\n")
    
    elif command == 'tags':
        tag = input("  Tag name: ").strip()
        
        if not tag:
            print("  ✗ Tag cannot be empty\n")
            continue
        
        results = get_notes_by_tag(notes, tag)
        
        if results:
            display_notes(results, f"NOTES WITH TAG: '{tag}'")
        else:
            print(f"  ✗ No notes with tag '{tag}'\n")
    
    else:
        print("  ✗ Unknown command\n")


"""
Detailed Line-by-Line Explanation:

========================
IMPORTS AND SETUP
========================

from datetime import datetime

Module import: Import datetime for timestamps
datetime: Python's built-in module for date/time operations
We use: datetime.now() to get current time


========================
Function 1: create_note()
========================

def create_note(notes, title, content, tags=None):

Function definition
Parameters:
  - notes: List to store notes
  - title: Note title (string)
  - content: Note content/body (string)
  - tags=None: Optional parameter (default None)

    ###Create a new note###

Docstring: Brief description of function purpose

    note = {
        'title': title,
        'content': content,
        'tags': tags if tags else [],
        'created': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'modified': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'id': len(notes) + 1
    }

Dictionary creation: Store note information
Key-value breakdown:

'title': title
  - Stores the note title

'content': content
  - Stores the note content/body

'tags': tags if tags else []
  - Ternary operator: If tags exist, use them; else empty list
  - Example: ['python', 'coding'] or []

'created': datetime.now().strftime('%Y-%m-%d %H:%M')
  - datetime.now(): Get current date/time
  - .strftime(): Format datetime as string
  - '%Y-%m-%d %H:%M': Format pattern
    %Y = Year (2026)
    %m = Month (01)
    %d = Day (11)
    %H = Hour (14)
    %M = Minute (30)
  - Result: "2026-01-11 14:30"

'modified': datetime.now().strftime('%Y-%m-%d %H:%M')
  - Same as created time initially
  - Will change when note is edited

'id': len(notes) + 1
  - Unique identifier
  - len(notes): Count existing notes
  - Example: If 5 notes exist, new ID = 6

Example dictionary:
{
    'title': 'Python Notes',
    'content': 'Learn Python basics',
    'tags': ['python', 'learning'],
    'created': '2026-01-11 14:30',
    'modified': '2026-01-11 14:30',
    'id': 1
}

    notes.append(note)

List method: Add note to end of list
Modifies: Original notes list

    return note

Return: Send back the created note


========================
Function 2: edit_note()
========================

def edit_note(notes, note_id, new_content):

Function: Update existing note content
Parameters:
  - notes: List of all notes
  - note_id: ID of note to edit
  - new_content: New content text

    ###Edit note content###

Docstring: Function description

    for note in notes:

Loop: Iterate through all notes

        if note['id'] == note_id:

Conditional: Check if this is the target note
Dictionary access: note['id']
Comparison: == (equals)

            note['content'] = new_content

Dictionary update: Replace old content with new
Direct modification of dictionary value

            note['modified'] = datetime.now().strftime('%Y-%m-%d %H:%M')

Update modified timestamp
Shows when note was last edited

            return True, note

Return tuple: (success, modified_note)
True: Operation succeeded
note: The updated note
Early exit: Stops function immediately

    return False, None

Default return: If note not found
False: Operation failed
None: No note to return


========================
Function 3: delete_note()
========================

def delete_note(notes, note_id):

Function: Remove note from list
Parameters:
  - notes: List of notes
  - note_id: ID to delete

    ###Delete a note###

Docstring

    for i, note in enumerate(notes):

Loop with index: Get position and item
enumerate(): Returns (index, item) pairs
Example: enumerate(['a', 'b']) → (0, 'a'), (1, 'b')

Why index?
Need position to remove from list

        if note['id'] == note_id:

Conditional: Found target note

            deleted = notes.pop(i)

List method: .pop(i) removes item at index i
Returns: The removed item
Modifies: Original list

Example:
notes = [note1, note2, note3]
deleted = notes.pop(1)
# deleted = note2
# notes = [note1, note3]

            return True, deleted

Return: Success + deleted note

    return False, None

Not found: Return failure


========================
Function 4: search_notes()
========================

def search_notes(notes, keyword):

Function: Find notes containing keyword
Parameters:
  - notes: List to search
  - keyword: Search term

    ###Search notes by keyword in title or content###

Docstring

    results = []

List: Store matching notes

    keyword_lower = keyword.lower()

String method: Convert to lowercase
Example: "Python" → "python"
Purpose: Case-insensitive search

    for note in notes:

Loop: Check each note

        if (keyword_lower in note['title'].lower() or 
            keyword_lower in note['content'].lower()):

Multi-line condition:
  - Check if keyword in title (lowercase)
  - OR check if keyword in content (lowercase)
  - in operator: Check substring presence

Example:
keyword_lower = "python"
note['title'].lower() = "learn python basics"
"python" in "learn python basics" → True

Logical operator: or
Returns True if either condition is True

            results.append(note)

List method: Add matching note to results

    return results

Return: List of matching notes (could be empty)


========================
Function 5: get_notes_by_tag()
========================

def get_notes_by_tag(notes, tag):

Function: Filter notes by tag
Parameters:
  - notes: All notes
  - tag: Tag to search for

    ###Get all notes with specific tag###

Docstring

    return [note for note in notes if tag.lower() in [t.lower() for t in note['tags']]]

List comprehension: Create filtered list in one line

Breakdown:

Inner part: [t.lower() for t in note['tags']]
  - List comprehension within list comprehension
  - Converts all tags to lowercase
  - Example: ['Python', 'AI'] → ['python', 'ai']

Outer part: [note for note in notes if condition]
  - Filters notes based on condition
  - Only keeps notes where tag matches

Condition: tag.lower() in [lowercase_tags]
  - Checks if search tag in note's tags
  - Case-insensitive comparison

Example:
tag = "Python"
note['tags'] = ['python', 'coding', 'basics']

Process:
1. tag.lower() = "python"
2. [t.lower() for t in ['python', 'coding', 'basics']] = ['python', 'coding', 'basics']
3. "python" in ['python', 'coding', 'basics'] → True
4. Include this note in results


========================
Function 6: display_notes()
========================

def display_notes(notes, title="ALL NOTES"):

Function: Show list of notes
Parameters:
  - notes: List to display
  - title: Header text (default "ALL NOTES")

    ###Display notes list###

Docstring

    if not notes:
        print("\n  No notes found.\n")
        return

Early exit: If list empty, show message and stop
not notes: Checks if list is empty
return: Exit function

    print("\n" + "="*80)

String concatenation:
  - "\n": Newline
  - "="*80: 80 equals signs (border)

    print(f"{title:^80}")

f-string formatting:
  - {title:^80}: Center text in 80 characters
  - ^ = center alignment
  - Example: "       ALL NOTES        "

    print("="*80)

Bottom border for header

    for note in notes:

Loop: Display each note

        print(f"\n[#{note['id']}] {note['title']}")

f-string: Display note ID and title
Format: [#1] My Note Title

        print(f"Created: {note['created']} | Modified: {note['modified']}")

Display timestamps
| : Visual separator

        if note['tags']:

Conditional: Only show tags if they exist
Empty list is False in boolean context

            tags_str = ", ".join(note['tags'])

String method: .join() combines list items
Example: ['python', 'ai'] → "python, ai"

            print(f"Tags: {tags_str}")

Display tags

        content_preview = note['content'][:100] + "..." if len(note['content']) > 100 else note['content']

Ternary operator: Create preview
Breakdown:

note['content'][:100]
  - String slicing: Get first 100 characters
  - Example: "Very long content..."[:10] → "Very long "

len(note['content']) > 100
  - Check if content longer than 100 chars

If True: first_100_chars + "..."
If False: full content

Example:
Long: "This is a very long note content..." (truncated to 100 + "...")
Short: "Short note" (shown in full)

        print(f"{content_preview}")

Display content preview

        print("-" * 80)

Separator line between notes

    print()

Final newline


========================
Function 7: display_note_full()
========================

def display_note_full(note):

Function: Show complete note with all details
Parameter: note (dictionary)

    ###Display full note content###

Docstring

    print("\n" + "="*80)
    print(f"[#{note['id']}] {note['title']}")
    print("="*80)

Header section with borders

    print(f"Created: {note['created']}")
    print(f"Modified: {note['modified']}")

Display timestamps

    if note['tags']:
        print(f"Tags: {', '.join(note['tags'])}")

Conditional display: Only show tags if present
Inline .join(): Combine tags with commas

    print("\n" + note['content'])

Display full content (not truncated)
\n: Add blank line before content

    print("="*80 + "\n")

Bottom border + newline


========================
MAIN PROGRAM
========================

notes = []

List initialization: Empty list for storing notes

print("=== NOTE MANAGER ===")
print("Commands: create, list, view, edit, delete, search, tags, quit\n")

Welcome message: Show available commands

while True:

Infinite loop: Keeps program running

    command = input("Command: ").lower().strip()

Input handling:
  - input("Command: "): Get user input
  - .lower(): Convert to lowercase
  - .strip(): Remove extra spaces
Example: "  CREATE  " → "create"


========================
QUIT COMMAND
========================

    if command == 'quit':
        print("Goodbye!")
        break

Exit condition:
  - Check if command is 'quit'
  - Print message
  - break: Exit while loop (stop program)


========================
CREATE COMMAND
========================

    elif command == 'create':

Branch: Handle create command

        title = input("  Title: ").strip()

Get note title from user

        if not title:
            print("  ✗ Title cannot be empty\n")
            continue

Validation: Reject empty title
continue: Skip to next loop iteration

        print("  Content (type 'END' on new line when done):")
        content_lines = []

Multi-line input setup:
  - Instructions for user
  - Empty list to store lines

        while True:
            line = input()
            if line == 'END':
                break
            content_lines.append(line)

Nested loop: Collect content lines
  - Get one line at a time
  - If user types 'END', stop
  - Otherwise add line to list

Example interaction:
> First line
> Second line
> END
Result: ['First line', 'Second line']

        content = "\n".join(content_lines)

String method: Join lines with newlines
Example: ['Line 1', 'Line 2'] → "Line 1\nLine 2"

        if not content:
            print("  ✗ Content cannot be empty\n")
            continue

Validation: Reject empty content

        tags_input = input("  Tags (comma-separated, or press Enter to skip): ").strip()

Get tags from user (optional)

        tags = [tag.strip() for tag in tags_input.split(',')] if tags_input else []

Complex line breakdown:

tags_input.split(',')
  - Split by commas
  - Example: "python, ai, coding" → ['python', ' ai', ' coding']

tag.strip() for tag in ...
  - Remove spaces from each tag
  - Example: [' ai'] → ['ai']

[...] if tags_input else []
  - If user entered tags: process them
  - If empty input: return empty list

Full example:
Input: "python, ai, coding"
Step 1: split → ['python', ' ai', ' coding']
Step 2: strip each → ['python', 'ai', 'coding']

        note = create_note(notes, title, content, tags)

Function call: Create and add note

        print(f"  ✓ Note #{note['id']} created\n")

Confirmation message with note ID


========================
LIST COMMAND
========================

    elif command == 'list':
        display_notes(notes)

Simple: Display all notes


========================
VIEW COMMAND
========================

    elif command == 'view':

Branch: Show full note details

        if not notes:
            print("  ✗ No notes available\n")
            continue

Validation: Check if notes exist

        try:

Try block: Handle potential errors

            note_id = int(input("  Note ID: "))

Input: Get note ID
int(): Convert string to number
Can raise ValueError if input not a number

            note = None

Variable initialization: Start with None

            for n in notes:
                if n['id'] == note_id:
                    note = n
                    break

Loop: Search for note by ID
  - Check each note
  - If ID matches: save it and break
  - break: Stop searching once found

            if note:
                display_note_full(note)
            else:
                print(f"  ✗ Note #{note_id} not found\n")

Conditional: Display if found, else show error
note: Will be None if not found (falsy)
note: Will be dictionary if found (truthy)

        except ValueError:
            print("  ✗ Invalid ID\n")

Exception handling: Catch conversion error
Happens if user enters non-number


========================
EDIT COMMAND
========================

    elif command == 'edit':

Branch: Modify existing note

        if not notes:
            print("  ✗ No notes to edit\n")
            continue

Validation

        try:
            note_id = int(input("  Note ID: "))

Get target note ID

            print("  New content (type 'END' on new line when done):")
            content_lines = []
            while True:
                line = input()
                if line == 'END':
                    break
                content_lines.append(line)

Multi-line input: Same as create command
Collect new content line by line

            new_content = "\n".join(content_lines)

Combine lines into single string

            if not new_content:
                print("  ✗ Content cannot be empty\n")
                continue

Validation: Reject empty content

            success, note = edit_note(notes, note_id, new_content)

Function call: Update note
Tuple unpacking: Get success status and note

            if success:
                print(f"  ✓ Note updated\n")
            else:
                print(f"  ✗ Note not found\n")

Feedback: Show result

        except ValueError:
            print("  ✗ Invalid ID\n")

Error handling


========================
DELETE COMMAND
========================

    elif command == 'delete':

Branch: Remove note

        if not notes:
            print("  ✗ No notes to delete\n")
            continue

Validation

        try:
            note_id = int(input("  Note ID: "))

Get ID to delete

            success, note = delete_note(notes, note_id)

Function call: Delete note
Returns: success status and deleted note

            if success:
                print(f"  ✓ Note deleted: {note['title']}\n")
            else:
                print(f"  ✗ Note not found\n")

Feedback with note title

        except ValueError:
            print("  ✗ Invalid ID\n")

Error handling


========================
SEARCH COMMAND
========================

    elif command == 'search':

Branch: Find notes by keyword

        keyword = input("  Search keyword: ").strip()

Get search term from user

        if not keyword:
            print("  ✗ Keyword cannot be empty\n")
            continue

Validation

        results = search_notes(notes, keyword)

Function call: Search notes
Returns list of matching notes

        if results:
            display_notes(results, f"SEARCH RESULTS: '{keyword}'")
        else:
            print(f"  ✗ No notes found matching '{keyword}'\n")

Conditional display:
  - If results found: show them
  - If empty list: show error
Empty list is falsy in Python


========================
TAGS COMMAND
========================

    elif command == 'tags':

Branch: Filter by tag

        tag = input("  Tag name: ").strip()

Get tag to search for

        if not tag:
            print("  ✗ Tag cannot be empty\n")
            continue

Validation

        results = get_notes_by_tag(notes, tag)

Function call: Find notes with tag

        if results:
            display_notes(results, f"NOTES WITH TAG: '{tag}'")
        else:
            print(f"  ✗ No notes with tag '{tag}'\n")

Display results or error


========================
UNKNOWN COMMAND
========================

    else:
        print("  ✗ Unknown command\n")

Default case: Handle invalid commands


========================
KEY CONCEPTS USED
========================

1. Dictionaries: Store structured data (notes)
2. Lists: Store collections (notes list, tags)
3. Functions: Organize code into reusable blocks
4. Loops: Iterate through collections
5. Conditionals: Make decisions
6. String methods: .lower(), .strip(), .split(), .join()
7. List methods: .append(), .pop()
8. datetime module: Timestamps
9. Try-except: Error handling
10. Tuple unpacking: Multiple return values
11. List comprehensions: Concise filtering
12. f-strings: String formatting
13. Ternary operators: Compact conditionals
14. Boolean context: Truthy/falsy values

"""