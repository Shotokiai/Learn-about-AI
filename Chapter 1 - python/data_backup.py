"""
Question: Data Backup Simulator
Task: Simulate file backup by creating a backup list with timestamps and file sizes.
Concepts Covered: Dictionaries, Lists, Functions, Modules (datetime), String formatting

"""


from datetime import datetime

def format_file_size(size_bytes):
    """Convert bytes to human-readable format"""
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = float(size_bytes)
    unit_index = 0
    
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    
    return f"{size:.2f} {units[unit_index]}"

def create_backup_entry(filename, size_bytes):
    """Create a backup record"""
    timestamp = datetime.now()
    
    backup = {
        'filename': filename,
        'size_bytes': size_bytes,
        'size_formatted': format_file_size(size_bytes),
        'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'status': 'Completed'
    }
    
    return backup

def calculate_total_size(backups):
    """Calculate total size of all backups"""
    total = 0
    for backup in backups:
        total += backup['size_bytes']
    return total

def display_backup_summary(backups):
    """Display backup summary table"""
    if not backups:
        print("\nNo backups recorded yet.\n")
        return
    
    print("\n" + "="*80)
    print(f"{'BACKUP SUMMARY':^80}")
    print("="*80)
    print(f"{'File Name':<30} {'Size':<15} {'Timestamp':<20} {'Status':<10}")
    print("-"*80)
    
    for backup in backups:
        print(f"{backup['filename']:<30} {backup['size_formatted']:<15} "
              f"{backup['timestamp']:<20} {backup['status']:<10}")
    
    print("-"*80)
    total_bytes = calculate_total_size(backups)
    total_formatted = format_file_size(total_bytes)
    print(f"{'Total:':<30} {total_formatted:<15} ({total_bytes:,} bytes)")
    print(f"{'Files backed up:':<30} {len(backups)}")
    print("="*80 + "\n")

def search_backups(backups, search_term):
    """Search backups by filename"""
    results = []
    search_term = search_term.lower()
    
    for backup in backups:
        if search_term in backup['filename'].lower():
            results.append(backup)
    
    return results

# Main program
backups = []

print("=== FILE BACKUP SIMULATOR ===")
print("Commands: add, list, search, total, quit\n")

while True:
    command = input("Command: ").lower().strip()
    
    if command == 'quit':
        print("Exiting backup system. Goodbye!")
        break
    
    elif command == 'add':
        filename = input("  Filename: ").strip()
        
        if not filename:
            print("  ✗ Filename cannot be empty\n")
            continue
        
        try:
            size_input = input("  File size (bytes): ").strip()
            size_bytes = int(size_input)
            
            if size_bytes < 0:
                print("  ✗ File size cannot be negative\n")
                continue
            
            backup = create_backup_entry(filename, size_bytes)
            backups.append(backup)
            
            print(f"  ✓ Backup created for '{filename}' ({backup['size_formatted']})")
            print(f"  Timestamp: {backup['timestamp']}\n")
            
        except ValueError:
            print("  ✗ Please enter a valid number for file size\n")
    
    elif command == 'list':
        display_backup_summary(backups)
    
    elif command == 'search':
        search_term = input("  Search filename: ").strip()
        
        if not search_term:
            print("  ✗ Search term cannot be empty\n")
            continue
        
        results = search_backups(backups, search_term)
        
        if results:
            print(f"\n  Found {len(results)} matching file(s):")
            for backup in results:
                print(f"    • {backup['filename']} - {backup['size_formatted']} - {backup['timestamp']}")
            print()
        else:
            print(f"  ✗ No files found matching '{search_term}'\n")
    
    elif command == 'total':
        if backups:
            total_bytes = calculate_total_size(backups)
            total_formatted = format_file_size(total_bytes)
            print(f"\n  Total backup size: {total_formatted} ({total_bytes:,} bytes)")
            print(f"  Files backed up: {len(backups)}\n")
        else:
            print("  ✗ No backups recorded yet\n")
    
    else:
        print("  ✗ Unknown command. Use: add, list, search, total, quit\n")

