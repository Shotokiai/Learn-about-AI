"""
Question - Log File Analyzer
Task - Analyze log entries, count error types, and display statistics.
Concepts Covered: Dictionaries, Lists, Loops, Conditionals, Functions, String methods

"""

def parse_log_entries(log_line): #Parameter: log_line - raw log string
    """Extract timestamp, level and message from log line"""
    parts = log_line.split(" - ",2) #.split(" - ", 2) splits by " - " separator || The 2 means: split maximum 2 times (creates 3 parts)
    if len(parts) == 3:
        return {
            'timestamp': parts[0],
            'level':parts[1],
            'message':parts[2]
        }
    return None


def analyze_logs(log_entries): #Count each log level
    """Count occurences of each log level"""
    stats = {} #Empty dict to store counts

    for entry in log_entries:
        level = entry['level']
        if level in stats:
            stats[level] += 1
        else:
            stats[level] = 1

    return stats


def display_statistics(stats,total):
    """Display log statistics with percentage"""
    print("\n=== LOG STATISTICS===")
    print(f"{'Level':<15} {'Count':<10} {'Percentage'}")
    print("-"*40)

    for level, count in stats.items():
        percentage = (count/total)*100
        print(f"{level:<15} {count:<10} {percentage:1f}%")

    print(f"\nTotal entries: {total}")

#Main Program
print("Enter log entries (format:timestamp - LEVEL - message)")
print("Example: 2024-01-10 10:30:45 - ERROR - Database Connection failed")
print("Type 'done' when finished\n")

log_entries = []

while True:
    log_line = input("Log: ")
    if log_line.lower() == 'done':
        break

    entry = parse_log_entries(log_line)
    if entry:
        log_entries.append(entry)
    else:
        print("Invalid format,skipping...")


if log_entries:
    stats = analyze_logs(log_entries)
    display_statistics(stats, len(log_entries))

    #show error specifically
    print("\n=== ERROR MESSAGES ===")
    error_count=0
    for entry in log_entries:
        if entry['level'] == 'Error':
            print(f"[{entry['timestamp']}] {entry['message']}")
            error_count +=1

    if error_count == 0:
        print("No errrors found!")
else:
    print("No valid log entries provided")





"""
Detailed Explanation of code - 


Explanation:
Function 1: parse_log_entry()
pythondef parse_log_entry(log_line):

Function: Extract structured data from log string
Parameter: log_line - raw log string

python    parts = log_line.split(" - ", 2)

String method: .split(" - ", 2) splits by " - " separator
The 2 means: split maximum 2 times (creates 3 parts)
Example: "2024-01-10 - ERROR - Connection failed"
→ ["2024-01-10", "ERROR", "Connection failed"]

Why limit splits?
If the message contains " - ", we don't want to split it further:

"10:30 - ERROR - Database - timeout" with split(" - ", 2):
→ ["10:30", "ERROR", "Database - timeout"] ✓ (message kept intact)
Without limit: ["10:30", "ERROR", "Database", "timeout"] ✗ (message broken)

python    if len(parts) == 3:
        return {
            'timestamp': parts[0],
            'level': parts[1],
            'message': parts[2]
        }

Conditional: Check if split worked correctly
Dictionary: Return structured data with keys
Dictionary creation: Uses {} with key-value pairs
Example result: {'timestamp': '2024-01-10', 'level': 'ERROR', 'message': 'Connection failed'}

python    return None

Return: If invalid format, return None (special value meaning "nothing")


Function 2: analyze_logs()
pythondef analyze_logs(log_entries):
    stats = {}

Function: Count each log level
Dictionary: Empty dict to store counts

python    for entry in log_entries:
        level = entry['level']

Loop: Process each log entry
Dictionary access: entry['level'] gets the level value
Example: {'level': 'ERROR'} → level = 'ERROR'

python        if level in stats:
            stats[level] += 1
        else:
            stats[level] = 1

Conditional: Check if level already counted
Dictionary check: level in stats checks if key exists
If exists: Increment counter: stats['ERROR'] += 1
If new: Initialize counter: stats['ERROR'] = 1

Example flow:
python# Processing logs:
Entry 1: ERROR   → stats = {'ERROR': 1}
Entry 2: INFO    → stats = {'ERROR': 1, 'INFO': 1}
Entry 3: ERROR   → stats = {'ERROR': 2, 'INFO': 1}
Entry 4: WARNING → stats = {'ERROR': 2, 'INFO': 1, 'WARNING': 1}
python    return stats

Return: Dictionary with counts


Function 3: display_statistics()
pythondef display_statistics(stats, total):

Function: Display formatted statistics
Parameters: stats dict and total count

python    print(f"{'Level':<15} {'Count':<10} {'Percentage'}")

f-string formatting:

{'Level':<15} - left-align text in 15 character space
< means left-align, > would be right-align



python    for level, count in stats.items():

Loop: Iterate through dictionary
Dictionary method: .items() returns key-value pairs
Example: {'ERROR': 5, 'INFO': 3}.items() → ('ERROR', 5), ('INFO', 3)

python        percentage = (count / total) * 100

Math operation: Calculate percentage
Example: (5 / 10) * 100 = 50.0

python        print(f"{level:<15} {count:<10} {percentage:.1f}%")

f-string formatting:

{percentage:.1f} - format float with 1 decimal place
.1f means "1 digit after decimal point"




Main Program:
pythonlog_entries = []

List: Store all parsed log entries

pythonwhile True:
    log_line = input("Log: ")
    if log_line.lower() == 'done':
        break

Loop: Collect logs until user types "done"

python    entry = parse_log_entry(log_line)
    if entry:
        log_entries.append(entry)
    else:
        print("  ⚠ Invalid format, skipping...")

Function call: Parse the log line
Conditional: Only add valid entries
if entry: checks if entry is not None

pythonif log_entries:
    stats = analyze_logs(log_entries)
    display_statistics(stats, len(log_entries))

Conditional: Only analyze if we have data
Function calls: Analyze and display

python    for entry in log_entries:
        if entry['level'] == 'ERROR':
            print(f"[{entry['timestamp']}] {entry['message']}")
            error_count += 1
```
- **Loop:** Show only ERROR level logs
- **Conditional:** Filter by level
- **Dictionary access:** Get timestamp and message

**Example Run:**
```
Enter log entries (format: timestamp - LEVEL - message)
Example: 2024-01-10 10:30:45 - ERROR - Database connection failed
Type 'done' when finished

Log: 2024-01-10 10:30:45 - ERROR - Database connection failed
Log: 2024-01-10 10:31:12 - INFO - Application started
Log: 2024-01-10 10:32:05 - ERROR - Timeout occurred
Log: 2024-01-10 10:33:20 - WARNING - Low memory
Log: 2024-01-10 10:34:15 - INFO - Request processed
Log: done

=== LOG STATISTICS ===
Level           Count      Percentage
----------------------------------------
ERROR           2          40.0%
INFO            2          40.0%
WARNING         1          20.0%

Total entries: 5

=== ERROR MESSAGES ===
[2024-01-10 10:30:45] Database connection failed
[2024-01-10 10:32:05] Timeout occurred

"""






