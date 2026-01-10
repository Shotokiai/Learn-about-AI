def add_expense(expenses, category, amount, description):
    """Add a new expense"""
    expense = {
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    return expense

def calculate_total(expenses):
    """Calculate total of all expenses"""
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

def calculate_by_category(expenses):
    """Calculate total spending per category"""
    category_totals = {}
    
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    
    return category_totals

def get_expenses_by_category(expenses, category):
    """Get all expenses in a specific category"""
    filtered = []
    
    for expense in expenses:
        if expense['category'].lower() == category.lower():
            filtered.append(expense)
    
    return filtered

def display_all_expenses(expenses):
    """Display all expenses in a table"""
    if not expenses:
        print("\n  No expenses recorded.\n")
        return
    
    print("\n" + "="*70)
    print(f"{'ALL EXPENSES':^70}")
    print("="*70)
    print(f"{'Category':<15} {'Amount':<12} {'Description':<43}")
    print("-"*70)
    
    for expense in expenses:
        print(f"{expense['category']:<15} ${expense['amount']:<11.2f} {expense['description']:<43}")
    
    print("-"*70)
    total = calculate_total(expenses)
    print(f"{'TOTAL:':<15} ${total:<11.2f}")
    print("="*70 + "\n")

def display_category_summary(expenses):
    """Display spending breakdown by category"""
    if not expenses:
        print("\n  No expenses recorded.\n")
        return
    
    category_totals = calculate_by_category(expenses)
    total = calculate_total(expenses)
    
    # Sort categories by spending (highest first)
    sorted_categories = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
    
    print("\n" + "="*60)
    print(f"{'SPENDING BY CATEGORY':^60}")
    print("="*60)
    print(f"{'Category':<20} {'Amount':<15} {'Percentage':<15}")
    print("-"*60)
    
    for category, amount in sorted_categories:
        percentage = (amount / total) * 100
        print(f"{category:<20} ${amount:<14.2f} {percentage:>5.1f}%")
    
    print("-"*60)
    print(f"{'TOTAL:':<20} ${total:<14.2f} {100.0:>5.1f}%")
    print("="*60 + "\n")

# Main program
expenses = []

print("=== EXPENSE TRACKER ===")
print("Commands: add, list, summary, category, total, quit\n")

while True:
    command = input("Command: ").lower().strip()
    
    if command == 'quit':
        print("Goodbye!")
        break
    
    elif command == 'add':
        category = input("  Category (e.g., Food, Transport, Bills): ").strip()
        
        if not category:
            print("  ✗ Category cannot be empty\n")
            continue
        
        try:
            amount = float(input("  Amount: $"))
            
            if amount <= 0:
                print("  ✗ Amount must be positive\n")
                continue
            
            description = input("  Description: ").strip()
            
            if not description:
                print("  ✗ Description cannot be empty\n")
                continue
            
            expense = add_expense(expenses, category, amount, description)
            print(f"  ✓ Expense added: {category} - ${amount:.2f}\n")
            
        except ValueError:
            print("  ✗ Please enter a valid number for amount\n")
    
    elif command == 'list':
        display_all_expenses(expenses)
    
    elif command == 'summary':
        display_category_summary(expenses)
    
    elif command == 'category':
        if not expenses:
            print("  ✗ No expenses recorded\n")
            continue
        
        # Show available categories
        categories = set()
        for expense in expenses:
            categories.add(expense['category'])
        
        print("\n  Available categories:")
        for cat in sorted(categories):
            print(f"    • {cat}")
        
        category = input("\n  Enter category name: ").strip()
        
        if not category:
            print("  ✗ Category cannot be empty\n")
            continue
        
        filtered = get_expenses_by_category(expenses, category)
        
        if filtered:
            print(f"\n  Expenses in '{category}':")
            print(f"  {'Amount':<12} {'Description':<50}")
            print("  " + "-"*62)
            
            total = 0
            for expense in filtered:
                print(f"  ${expense['amount']:<11.2f} {expense['description']:<50}")
                total += expense['amount']
            
            print("  " + "-"*62)
            print(f"  Total: ${total:.2f}\n")
        else:
            print(f"  ✗ No expenses found in category '{category}'\n")
    
    elif command == 'total':
        if expenses:
            total = calculate_total(expenses)
            print(f"\n  Total expenses: ${total:.2f}\n")
        else:
            print("  ✗ No expenses recorded\n")
    
    else:
        print("  ✗ Unknown command. Use: add, list, summary, category, total, quit\n")


