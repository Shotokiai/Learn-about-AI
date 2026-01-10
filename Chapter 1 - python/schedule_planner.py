
def parse_time(time_str):
    """Parse time string (HH:MM format) and validate"""
    try:
        parts = time_str.split(':')
        if len(parts) != 2:
            return None
        
        hour = int(parts[0])
        minute = int(parts[1])
        
        if 0 <= hour <= 23 and 0 <= minute <= 59:
            return hour, minute
        return None
    except ValueError:
        return None

def time_to_minutes(hour, minute):
    """Convert time to minutes since midnight"""
    return hour * 60 + minute

def format_time(hour, minute):
    """Format time as HH:MM"""
    return f"{hour:02d}:{minute:02d}"

def check_time_conflict(events, new_start_time, new_end_time):
    """Check if new event conflicts with existing events"""
    new_start_min = time_to_minutes(*new_start_time)
    new_end_min = time_to_minutes(*new_end_time)
    
    for event in events:
        event_start_min = time_to_minutes(*event['start_time'])
        event_end_min = time_to_minutes(*event['end_time'])
        
        # Check for overlap
        if (new_start_min < event_end_min and new_end_min > event_start_min):
            return True, event
    
    return False, None

def add_event(events, title, start_time, end_time):
    """Add new event to schedule"""
    event = {
        'title': title,
        'start_time': start_time,
        'end_time': end_time,
        'start_minutes': time_to_minutes(*start_time)
    }
    events.append(event)
    return event

def sort_events(events):
    """Sort events by start time"""
    return sorted(events, key=lambda x: x['start_minutes'])

def display_schedule(events):
    """Display all scheduled events"""
    if not events:
        print("\n  No events scheduled.\n")
        return
    
    sorted_events = sort_events(events)
    
    print("\n" + "="*70)
    print(f"{'DAILY SCHEDULE':^70}")
    print("="*70)
    print(f"{'Time':<20} {'Event':<50}")
    print("-"*70)
    
    for event in sorted_events:
        start = format_time(*event['start_time'])
        end = format_time(*event['end_time'])
        time_range = f"{start} - {end}"
        print(f"{time_range:<20} {event['title']:<50}")
    
    print("="*70 + "\n")

def delete_event(events, title):
    """Delete event by title"""
    for i, event in enumerate(events):
        if event['title'].lower() == title.lower():
            deleted = events.pop(i)
            return True, deleted
    return False, None

# Main program
events = []

print("=== DAILY SCHEDULE PLANNER ===")
print("Commands: add, view, delete, quit\n")

while True:
    command = input("Command: ").lower().strip()
    
    if command == 'quit':
        print("Goodbye!")
        break
    
    elif command == 'add':
        title = input("  Event title: ").strip()
        
        if not title:
            print("  ✗ Event title cannot be empty\n")
            continue
        
        start_str = input("  Start time (HH:MM): ").strip()
        start_time = parse_time(start_str)
        
        if not start_time:
            print("  ✗ Invalid start time format. Use HH:MM (e.g., 09:30)\n")
            continue
        
        end_str = input("  End time (HH:MM): ").strip()
        end_time = parse_time(end_str)
        
        if not end_time:
            print("  ✗ Invalid end time format. Use HH:MM (e.g., 10:30)\n")
            continue
        
        # Check if end time is after start time
        if time_to_minutes(*end_time) <= time_to_minutes(*start_time):
            print("  ✗ End time must be after start time\n")
            continue
        
        # Check for conflicts
        has_conflict, conflicting_event = check_time_conflict(events, start_time, end_time)
        
        if has_conflict:
            print(f"  ✗ Time conflict with: {conflicting_event['title']}")
            print(f"    ({format_time(*conflicting_event['start_time'])} - "
                  f"{format_time(*conflicting_event['end_time'])})\n")
            continue
        
        event = add_event(events, title, start_time, end_time)
        print(f"  ✓ Event '{title}' added successfully")
        print(f"    Time: {format_time(*start_time)} - {format_time(*end_time)}\n")
    
    elif command == 'view':
        display_schedule(events)
    
    elif command == 'delete':
        if not events:
            print("  ✗ No events to delete\n")
            continue
        
        print("\n  Current events:")
        for event in sort_events(events):
            print(f"    • {event['title']}")
        
        title = input("\n  Enter event title to delete: ").strip()
        
        success, deleted = delete_event(events, title)
        
        if success:
            print(f"  ✓ Event '{deleted['title']}' deleted\n")
        else:
            print(f"  ✗ Event '{title}' not found\n")
    
    else:
        print("  ✗ Unknown command. Use: add, view, delete, quit\n")