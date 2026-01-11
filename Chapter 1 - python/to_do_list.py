"""
## **Example Run:**
```
=== TO-DO LIST MANAGER ===
Commands: add, list, pending, completed, complete, delete, sort, quit

Command: add
  Task title: Buy groceries
  Priority: High, Medium, or Low
  Priority: High
  Due date (or press Enter to skip): Today
  ✓ Task #1 added

Command: add
  Task title: Clean room
  Priority: High, Medium, or Low
  Priority: Low
  Due date (or press Enter to skip): 
  ✓ Task #2 added

Command: list

================================================================================
                                  ALL TASKS                                    
================================================================================
ID    Status     Priority   Due Date        Task                                    
--------------------------------------------------------------------------------
1     ○ Pending  High       Today           Buy groceries                           
2     ○ Pending  Low        No deadline     Clean room                              
================================================================================

Command: complete

  Pending tasks:
    #1: Buy groceries
    #2: Clean room

  Enter task ID to mark complete: 1
  ✓ Task #1 marked as complete

Command: pending

================================================================================
                               PENDING TASKS                                   
================================================================================
ID    Status     Priority   Due Date        Task                                    
--------------------------------------------------------------------------------
2     ○ Pending  Low        No deadline     Clean room                              
================================================================================

Command: quit
Goodbye!


"""

def add_task(tasks, title, priority, due_date=None):
    """Add a new task"""
    task = {
        'title': title,
        'priority': priority,
        'due_date': due_date if due_date else 'No deadline',
        'completed': False,
        'id': len(tasks) + 1
    }
    tasks.append(task)
    return task

def mark_complete(tasks, task_id):
    """Mark a task as completed"""
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return True, task
    return False, None

def delete_task(tasks, task_id):
    """Delete a task by ID"""
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            deleted = tasks.pop(i)
            return True, deleted
    return False, None

def get_pending_tasks(tasks):
    """Get all incomplete tasks"""
    pending = []
    for task in tasks:
        if not task['completed']:
            pending.append(task)
    return pending

def get_completed_tasks(tasks):
    """Get all completed tasks"""
    completed = []
    for task in tasks:
        if task['completed']:
            completed.append(task)
    return completed

def sort_by_priority(tasks):
    """Sort tasks by priority (High, Medium, Low)"""
    priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
    
    def get_priority_value(task):
        return priority_order.get(task['priority'], 4)
    
    return sorted(tasks, key=get_priority_value)

def display_tasks(tasks, title="ALL TASKS"):
    """Display tasks in a formatted table"""
    if not tasks:
        print(f"\n  No tasks to display.\n")
        return
    
    print("\n" + "="*80)
    print(f"{title:^80}")
    print("="*80)
    print(f"{'ID':<5} {'Status':<10} {'Priority':<10} {'Due Date':<15} {'Task':<40}")
    print("-"*80)
    
    for task in tasks:
        status = "✓ Done" if task['completed'] else "○ Pending"
        task_id = str(task['id'])
        priority = task['priority']
        due = task['due_date']
        title_text = task['title'][:37] + "..." if len(task['title']) > 40 else task['title']
        
        print(f"{task_id:<5} {status:<10} {priority:<10} {due:<15} {title_text:<40}")
    
    print("="*80 + "\n")

def get_task_by_id(tasks, task_id):
    """Find task by ID"""
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

# Main program
tasks = []

print("=== TO-DO LIST MANAGER ===")
print("Commands: add, list, pending, completed, complete, delete, sort, quit\n")

while True:
    command = input("Command: ").lower().strip()
    
    if command == 'quit':
        print("Goodbye!")
        break
    
    elif command == 'add':
        title = input("  Task title: ").strip()
        
        if not title:
            print("  ✗ Task title cannot be empty\n")
            continue
        
        print("  Priority: High, Medium, or Low")
        priority = input("  Priority: ").strip().capitalize()
        
        if priority not in ['High', 'Medium', 'Low']:
            print("  ✗ Invalid priority. Using 'Medium'\n")
            priority = 'Medium'
        
        due_date = input("  Due date (or press Enter to skip): ").strip()
        
        if not due_date:
            due_date = None
        
        task = add_task(tasks, title, priority, due_date)
        print(f"  ✓ Task #{task['id']} added\n")
    
    elif command == 'list':
        display_tasks(tasks)
    
    elif command == 'pending':
        pending = get_pending_tasks(tasks)
        display_tasks(pending, "PENDING TASKS")
    
    elif command == 'completed':
        completed = get_completed_tasks(tasks)
        display_tasks(completed, "COMPLETED TASKS")
    
    elif command == 'complete':
        if not tasks:
            print("  ✗ No tasks available\n")
            continue
        
        # Show pending tasks
        pending = get_pending_tasks(tasks)
        
        if not pending:
            print("  ✓ All tasks are completed!\n")
            continue
        
        print("\n  Pending tasks:")
        for task in pending:
            print(f"    #{task['id']}: {task['title']}")
        
        try:
            task_id = int(input("\n  Enter task ID to mark complete: "))
            
            success, task = mark_complete(tasks, task_id)
            
            if success:
                print(f"  ✓ Task #{task_id} marked as complete\n")
            else:
                print(f"  ✗ Task #{task_id} not found\n")
                
        except ValueError:
            print("  ✗ Please enter a valid task ID\n")
    
    elif command == 'delete':
        if not tasks:
            print("  ✗ No tasks to delete\n")
            continue
        
        print("\n  All tasks:")
        for task in tasks:
            status = "✓" if task['completed'] else "○"
            print(f"    #{task['id']} {status} {task['title']}")
        
        try:
            task_id = int(input("\n  Enter task ID to delete: "))
            
            success, task = delete_task(tasks, task_id)
            
            if success:
                print(f"  ✓ Task deleted: {task['title']}\n")
            else:
                print(f"  ✗ Task #{task_id} not found\n")
                
        except ValueError:
            print("  ✗ Please enter a valid task ID\n")
    
    elif command == 'sort':
        if not tasks:
            print("  ✗ No tasks to sort\n")
            continue
        
        sorted_tasks = sort_by_priority(tasks)
        display_tasks(sorted_tasks, "TASKS SORTED BY PRIORITY")
    
    else:
        print("  ✗ Unknown command\n")




    


"""

Detailed Line-by-Line Explanation:

Function 1: add_task()
pythondef add_task(tasks, title, priority, due_date=None):

def: Define a function
add_task: Function name
Parameters:

tasks: List to add task to
title: Task description
priority: High, Medium, or Low
due_date=None: Optional parameter with default value



Default parameters:
python# due_date=None means it's optional
add_task(tasks, "Buy milk", "High")           # due_date will be None
add_task(tasks, "Buy milk", "High", "Today")  # due_date will be "Today"
python   ####Add a new task###




Docstring: Explains what function does

python    task = {
        'title': title,
        'priority': priority,
        'due_date': due_date if due_date else 'No deadline',
        'completed': False,
        'id': len(tasks) + 1
    }

Dictionary: Store task information
Keys: Field names
Values: Task data

Line-by-line breakdown:
python        'title': title,

Key: 'title'
Value: Whatever was passed as title parameter

python        'priority': priority,

Key: 'priority'
Value: High, Medium, or Low

python        'due_date': due_date if due_date else 'No deadline',

Ternary operator: value if condition else other_value
Logic: If due_date exists, use it; otherwise use 'No deadline'
Example: None if None else 'No deadline' → 'No deadline'
Example: "Today" if "Today" else 'No deadline' → "Today"

python        'completed': False,

Boolean: New tasks start as not completed

python        'id': len(tasks) + 1

Unique ID: Based on number of existing tasks
len(tasks): Returns number of tasks in list
Example: If 5 tasks exist, new ID = 5 + 1 = 6

Example task dictionary:
python{
    'title': 'Buy groceries',
    'priority': 'High',
    'due_date': 'Today',
    'completed': False,
    'id': 1
}
python    tasks.append(task)

List method: .append() adds item to
Continue11:17 AMend of list

Modifies original list

python    return task

Return: Send back the created task


Function 2: mark_complete()
pythondef mark_complete(tasks, task_id):
    #Mark a task as completed
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return True, task
    return False, None
Line by line:
pythondef mark_complete(tasks, task_id):

Function: Mark task as done
Parameters: task list and ID to mark

python    for task in tasks:

Loop: Check each task in list

python        if task['id'] == task_id:

Conditional: Check if this is the task we want
Dictionary access: task['id'] gets the ID
Comparison: == checks equality

python            task['completed'] = True

Dictionary update: Change completed status
Directly modifies the task dictionary

python            return True, task

Return tuple: (success_status, task_object)
True: Operation succeeded
task: The modified task
Exits function immediately

python    return False, None

Default return: If no task found
False: Operation failed
None: No task to return


Function 3: delete_task()
pythondef delete_task(tasks, task_id):
    ###Delete a task by ID
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            deleted = tasks.pop(i)
            return True, deleted
    return False, None
Line by line:
pythondef delete_task(tasks, task_id):

Function: Remove task from list

python    for i, task in enumerate(tasks):

Loop with index: Get both position and item
enumerate(): Returns (index, item) pairs
Example: enumerate(['a', 'b']) → (0, 'a'), (1, 'b')

Why need index?
We need the position to delete from list
python        if task['id'] == task_id:

Conditional: Found the task to delete

python            deleted = tasks.pop(i)

List method: .pop(i) removes item at index i
Returns: The removed item
Modifies: Original list

Example:
pythontasks = ['task1', 'task2', 'task3']
deleted = tasks.pop(1)  # Remove index 1
# deleted = 'task2'
# tasks = ['task1', 'task3']
python            return True, deleted

Return tuple: Success + deleted task

python    return False, None

Not found: Return failure


Function 4: get_pending_tasks()
pythondef get_pending_tasks(tasks):
    ###Get all incomplete tasks###
    pending = []
    for task in tasks:
        if not task['completed']:
            pending.append(task)
    return pending
Line by line:
pythondef get_pending_tasks(tasks):

Function: Filter incomplete tasks

python    pending = []

List: Store results

python    for task in tasks:

Loop: Check each task

python        if not task['completed']:

Conditional: Check if NOT completed
not False → True
not True → False

python            pending.append(task)

List method: Add to pending list

python    return pending

Return: List of incomplete tasks


Function 5: get_completed_tasks()
pythondef get_completed_tasks(tasks):
    ###Get all completed tasks###
    completed = []
    for task in tasks:
        if task['completed']:
            completed.append(task)
    return completed
Line by line:
pythondef get_completed_tasks(tasks):

Function: Filter completed tasks

python        if task['completed']:

Conditional: Check if completed is True
If task['completed'] is True, condition passes

Difference from pending:

Pending: if not task['completed'] (False)
Completed: if task['completed'] (True)


Function 6: sort_by_priority()
pythondef sort_by_priority(tasks):
    ###Sort tasks by priority (High, Medium, Low)###
    priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
    
    def get_priority_value(task):
        return priority_order.get(task['priority'], 4)
    
    return sorted(tasks, key=get_priority_value)
Line by line:
pythondef sort_by_priority(tasks):

Function: Sort by priority level

python    priority_order = {'High': 1, 'Medium': 2, 'Low': 3}

Dictionary: Map priority to number
Why? Easier to sort numbers than strings
Lower number = higher priority

python    def get_priority_value(task):

Nested function: Function inside a function
Purpose: Extract priority number for sorting

python        return priority_order.get(task['priority'], 4)

Dictionary method: .get(key, default)
Gets value for key, or default if key doesn't exist
Example: priority_order.get('High', 4) → 1
Example: priority_order.get('Unknown', 4) → 4

python    return sorted(tasks, key=get_priority_value)

sorted(): Built-in function to sort
key parameter: Function to determine sort order
How it works:

Calls get_priority_value() for each task
Sorts by the returned numbers
Returns new sorted list



Example:
pythontasks = [
    {'priority': 'Low', 'title': 'Task 1'},
    {'priority': 'High', 'title': 'Task 2'},
    {'priority': 'Medium', 'title': 'Task 3'}
]

# Sorting process:
# Task 1: get_priority_value() → 3
# Task 2: get_priority_value() → 1
# Task 3: get_priority_value() → 2

# Sort by these numbers: [1, 2, 3]
# Result: [Task 2, Task 3, Task 1]  (High, Medium, Low)

Function 7: display_tasks()
pythondef display_tasks(tasks, title="ALL TASKS"):
    ###Display tasks in a formatted table###
    if not tasks:
        print(f"\n  No tasks to display.\n")
        return
Line by line:
pythondef display_tasks(tasks, title="ALL TASKS"):

Function: Show tasks in table format
Default parameter: title="ALL TASKS"

python    if not tasks:
        print(f"\n  No tasks to display.\n")
        return

Early exit: If list empty, show message and stop

python    print("\n" + "="*80)

String concatenation: Newline + 80 equals signs
Creates top border

python    print(f"{title:^80}")

f-string formatting: {value:^width}
^80: Center text in 80 characters
Example: "       ALL TASKS       "

python    print(f"{'ID':<5} {'Status':<10} {'Priority':<10} {'Due Date':<15} {'Task':<40}")

Column headers: Each with specific width
<5: Left-align in 5 characters
<10: Left-align in 10 characters

python    print("-"*80)

Separator: 80 dashes

python    for task in tasks:

Loop: Display each task

python        status = "✓ Done" if task['completed'] else "○ Pending"

Ternary operator: Choose status symbol
If completed: ✓ Done
If not: ○ Pending

python        task_id = str(task['id'])

Type conversion: Convert number to string
Needed for string formatting

python        priority = task['priority']
        due = task['due_date']

Variables: Store values for easy access

python        title_text = task['title'][:37] + "..." if len(task['title']) > 40 else task['title']

String slicing: task['title'][:37] gets first 37 characters
Conditional: If title too long, truncate and add "..."
Example: "Very long task title here"[:10] → "Very long "

Breakdown:
pythonif len(task['title']) > 40:
    title_text = task['title'][:37] + "..."
else:
    title_text = task['title']
python        print(f"{task_id:<5} {status:<10} {priority:<10} {due:<15} {title_text:<40}")

f-string: Format and print row
Each column aligned according to header

python    print("="*80 + "\n")

Bottom border: 80 equals signs + newline


Function 8: get_task_by_id()
pythondef get_task_by_id(tasks, task_id):
    ###Find task by ID###
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None
Line by line:
pythondef get_task_by_id(tasks, task_id):

Function: Search for specific task

python    for task in tasks:
        if task['id'] == task_id:
            return task

Loop: Check each task
Early return: Stop as soon as found

python    return None

Not found: Return None if no match


Main Program:
pythontasks = []

List: Empty list to store all tasks

pythonprint("=== TO-DO LIST MANAGER ===")
print("Commands: add, list, pending, completed, complete, delete, sort, quit\n")

Output: Welcome message and instructions

pythonwhile True:

Infinite loop: Keep running until break

python    command = input("Command: ").lower().strip()

Input: Get user command
.lower(): Convert to lowercase
.strip(): Remove extra spaces

python    if command == 'quit':
        print("Goodbye!")
        break

Exit condition: Stop program


ADD COMMAND:
python    elif command == 'add':
        title = input("  Task title: ").strip()

Input: Get task description

python        if not title:
            print("  ✗ Task title cannot be empty\n")
            continue

Validation: Reject empty titles
continue: Skip to next loop iteration

python        print("  Priority: High, Medium, or Low")
        priority = input("  Priority: ").strip().capitalize()

Input: Get priority
.capitalize(): First letter uppercase
Example: "high" → "High"

python        if priority not in ['High', 'Medium', 'Low']:
            print("  ✗ Invalid priority. Using 'Medium'\n")
            priority = 'Medium'

Validation: Check if priority is valid
List membership: in ['High', 'Medium', 'Low']
Fallback: Use 'Medium' if invalid

python        due_date = input("  Due date (or press Enter to skip): ").strip()
        
        if not due_date:
            due_date = None

Optional input: Allow empty
Convert empty string to None

python        task = add_task(tasks, title, priority, due_date)
        print(f"  ✓ Task #{task['id']} added\n")

Function call: Create and add task
Confirmation: Show task ID


LIST COMMAND:
python    elif command == 'list':
        display_tasks(tasks)

Simple: Just display all tasks


PENDING COMMAND:
python    elif command == 'pending':
        pending = get_pending_tasks(tasks)
        display_tasks(pending, "PENDING TASKS")

Function call: Get incomplete tasks
Display: Show with custom title


COMPLETED COMMAND:
python    elif command == 'completed':
        completed = get_completed_tasks(tasks)
        display_tasks(completed, "COMPLETED TASKS")

Similar to pending: Filter and display


COMPLETE COMMAND:
python    elif command == 'complete':
        if not tasks:
            print("  ✗ No tasks available\n")
            continue

Validation: Check if tasks exist

python        pending = get_pending_tasks(tasks)
        
        if not pending:
            print("  ✓ All tasks are completed!\n")
            continue

Check: If all tasks done

python        print("\n  Pending tasks:")
        for task in pending:
            print(f"    #{task['id']}: {task['title']}")

Display: Show pending tasks with IDs

python        try:
            task_id = int(input("\n  Enter task ID to mark complete: "))

try block: Handle conversion error
int(): Convert string to number

python            success, task = mark_complete(tasks, task_id)

Function call: Mark task as done
Tuple unpacking: Get success status and task

python            if success:
                print(f"  ✓ Task #{task_id} marked as complete\n")
            else:
                print(f"  ✗ Task #{task_id} not found\n")

Conditional: Show appropriate message

python        except ValueError:
            print("  ✗ Please enter a valid task ID\n")

Exception: Handle invalid input


DELETE COMMAND:
python    elif command == 'delete':
        if not tasks:
            print("  ✗ No tasks to delete\n")
            continue

Validation: Check tasks exist

python        print("\n  All tasks:")
        for task in tasks:
            status = "✓" if task['completed'] else "○"
            print(f"    #{task['id']} {status} {task['title']}")

Display: Show all tasks with status symbols

python        try:
            task_id = int(input("\n  Enter task ID to delete: "))
            
            success, task = delete_task(tasks, task_id)
            
            if success:
                print(f"  ✓ Task deleted: {task['title']}\n")
            else:
                print(f"  ✗ Task #{task_id} not found\n")

Similar pattern: Get ID, call function, show result


SORT COMMAND:
python    elif command == 'sort':
        if not tasks:
            print("  ✗ No tasks to sort\n")
            continue
        
        sorted_tasks = sort_by_priority(tasks)
        display_tasks(sorted_tasks, "TASKS SORTED BY PRIORITY")

Function call: Get sorted list
Display: Show sorted view
Important: Doesn't change original list




"""