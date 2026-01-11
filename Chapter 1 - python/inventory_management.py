"""

=== INVENTORY MANAGEMENT SYSTEM ===
Commands: add, list, update, search, low-stock, value, sort, quit

Command: add
  Product name: Laptop
  Quantity: 10
  Price per unit: $899.99
  Minimum stock level (default 5): 3
  ✓ Product #1 added successfully

Command: add
  Product name: Mouse
  Quantity: 50
  Price per unit: $25.50
  Minimum stock level (default 5): 
  ✓ Product #2 added successfully

Command: list

==========================================================================================
                                      INVENTORY                                          
==========================================================================================
ID    Product                   Qty      Price        Value           Status         
------------------------------------------------------------------------------------------
1     Laptop                    10       $899.99      $8999.90        ✓ In Stock     
2     Mouse                     50       $25.50       $1275.00        ✓ In Stock     
------------------------------------------------------------------------------------------
TOTAL INVENTORY VALUE:                                $10,274.90
==========================================================================================

Command: update

  Products:
    #1: Laptop (Stock: 10)
    #2: Mouse (Stock: 50)

  Enter product ID: 2
  Quantity change (+add/-remove): -46
  ✓ 46 units removed
  New stock: 4

Command: low-stock

==========================================================================================
                                 ⚠ LOW STOCK ALERT                                       
==========================================================================================
ID    Product                   Qty      Price        Value           Status         
------------------------------------------------------------------------------------------
2     Mouse                     4        $25.50       $102.00         ⚠ LOW STOCK    
------------------------------------------------------------------------------------------
TOTAL INVENTORY VALUE:                                $102.00
==========================================================================================

Command: quit
Goodbye!


"""


def add_product(inventory, name, quantity, price, min_stock=5):
    """Add new product to inventory"""
    product = {
        'name': name,
        'quantity': quantity,
        'price': price,
        'min_stock': min_stock,
        'id': len(inventory) + 1
    }
    inventory.append(product)
    return product

def update_stock(inventory, product_id, quantity_change):
    """Update product stock (positive to add, negative to remove)"""
    for product in inventory:
        if product['id'] == product_id:
            new_quantity = product['quantity'] + quantity_change
            
            if new_quantity < 0:
                return False, "Insufficient stock", product
            
            product['quantity'] = new_quantity
            return True, "Stock updated", product
    
    return False, "Product not found", None

def get_product_by_id(inventory, product_id):
    """Find product by ID"""
    for product in inventory:
        if product['id'] == product_id:
            return product
    return None

def get_low_stock_products(inventory):
    """Get products below minimum stock level"""
    low_stock = []
    
    for product in inventory:
        if product['quantity'] <= product['min_stock']:
            low_stock.append(product)
    
    return low_stock

def calculate_total_value(inventory):
    """Calculate total inventory value"""
    total = 0
    
    for product in inventory:
        value = product['quantity'] * product['price']
        total += value
    
    return total

def calculate_product_value(product):
    """Calculate value of a single product"""
    return product['quantity'] * product['price']

def display_inventory(inventory, title="INVENTORY"):
    """Display inventory in formatted table"""
    if not inventory:
        print(f"\n  No products in inventory.\n")
        return
    
    print("\n" + "="*90)
    print(f"{title:^90}")
    print("="*90)
    print(f"{'ID':<5} {'Product':<25} {'Qty':<8} {'Price':<12} {'Value':<15} {'Status':<15}")
    print("-"*90)
    
    for product in inventory:
        product_id = str(product['id'])
        name = product['name'][:22] + "..." if len(product['name']) > 25 else product['name']
        qty = str(product['quantity'])
        price = f"${product['price']:.2f}"
        value = f"${calculate_product_value(product):.2f}"
        
        if product['quantity'] == 0:
            status = "OUT OF STOCK"
        elif product['quantity'] <= product['min_stock']:
            status = "⚠ LOW STOCK"
        else:
            status = "✓ In Stock"
        
        print(f"{product_id:<5} {name:<25} {qty:<8} {price:<12} {value:<15} {status:<15}")
    
    print("-"*90)
    total_value = calculate_total_value(inventory)
    print(f"{'TOTAL INVENTORY VALUE:':<50} ${total_value:,.2f}")
    print("="*90 + "\n")

def search_products(inventory, search_term):
    """Search products by name"""
    results = []
    search_lower = search_term.lower()
    
    for product in inventory:
        if search_lower in product['name'].lower():
            results.append(product)
    
    return results

def sort_by_value(inventory):
    """Sort products by total value (descending)"""
    return sorted(inventory, key=lambda p: calculate_product_value(p), reverse=True)

# Main program
inventory = []

print("=== INVENTORY MANAGEMENT SYSTEM ===")
print("Commands: add, list, update, search, low-stock, value, sort, quit\n")

while True:
    command = input("Command: ").lower().strip()
    
    if command == 'quit':
        print("Goodbye!")
        break
    
    elif command == 'add':
        name = input("  Product name: ").strip()
        
        if not name:
            print("  ✗ Product name cannot be empty\n")
            continue
        
        try:
            quantity = int(input("  Quantity: "))
            price = float(input("  Price per unit: $"))
            min_stock = int(input("  Minimum stock level (default 5): ") or "5")
            
            if quantity < 0 or price < 0 or min_stock < 0:
                print("  ✗ Values cannot be negative\n")
                continue
            
            product = add_product(inventory, name, quantity, price, min_stock)
            print(f"  ✓ Product #{product['id']} added successfully\n")
            
        except ValueError:
            print("  ✗ Please enter valid numbers\n")
    
    elif command == 'list':
        display_inventory(inventory)
    
    elif command == 'update':
        if not inventory:
            print("  ✗ No products in inventory\n")
            continue
        
        print("\n  Products:")
        for p in inventory:
            print(f"    #{p['id']}: {p['name']} (Stock: {p['quantity']})")
        
        try:
            product_id = int(input("\n  Enter product ID: "))
            change = int(input("  Quantity change (+add/-remove): "))
            
            success, message, product = update_stock(inventory, product_id, change)
            
            if success:
                action = "added" if change > 0 else "removed"
                print(f"  ✓ {abs(change)} units {action}")
                print(f"  New stock: {product['quantity']}\n")
            else:
                print(f"  ✗ {message}\n")
                
        except ValueError:
            print("  ✗ Please enter valid numbers\n")
    
    elif command == 'search':
        search_term = input("  Search product name: ").strip()
        
        if not search_term:
            print("  ✗ Search term cannot be empty\n")
            continue
        
        results = search_products(inventory, search_term)
        
        if results:
            display_inventory(results, f"SEARCH RESULTS: '{search_term}'")
        else:
            print(f"  ✗ No products found matching '{search_term}'\n")
    
    elif command == 'low-stock':
        low_stock = get_low_stock_products(inventory)
        
        if low_stock:
            display_inventory(low_stock, "⚠ LOW STOCK ALERT")
        else:
            print("  ✓ All products have sufficient stock\n")
    
    elif command == 'value':
        if not inventory:
            print("  ✗ No products in inventory\n")
            continue
        
        total = calculate_total_value(inventory)
        print(f"\n  Total Inventory Value: ${total:,.2f}\n")
    
    elif command == 'sort':
        if not inventory:
            print("  ✗ No products to sort\n")
            continue
        
        sorted_inv = sort_by_value(inventory)
        display_inventory(sorted_inv, "INVENTORY SORTED BY VALUE")
    
    else:
        print("  ✗ Unknown command\n")





"""


Detailed Line-by-Line Explanation:

Function 1: add_product()
pythondef add_product(inventory, name, quantity, price, min_stock=5):
    ###Add new product to inventory###

Function: Add new product
Default parameter: min_stock=5 is optional

python    product = {
        'name': name,
        'quantity': quantity,
        'price': price,
        'min_stock': min_stock,
        'id': len(inventory) + 1
    }

Dictionary: Store product information
'name': Product name
'quantity': Current stock amount
'price': Price per unit
'min_stock': Minimum before alert
'id': Unique identifier

python    inventory.append(product)
    return product

List method: Add to inventory
Return: The created product


Function 2: update_stock()
pythondef update_stock(inventory, product_id, quantity_change):
    ###Update product stock (positive to add, negative to remove)###

Function: Modify stock quantity
quantity_change: Positive = add, Negative = remove

python    for product in inventory:
        if product['id'] == product_id:

Loop: Find the product

python            new_quantity = product['quantity'] + quantity_change

Calculate: New stock amount
Example: Current 10, change +5 → new 15
Example: Current 10, change -3 → new 7

python            if new_quantity < 0:
                return False, "Insufficient stock", product

Validation: Can't have negative stock
**Return tuple
Continue11:22 AM:** (success, message, product)
python            product['quantity'] = new_quantity
            return True, "Stock updated", product

Update: Change quantity in dictionary
Return: Success with updated product

python    return False, "Product not found", None

Not found: Return failure


Function 3: get_product_by_id()
pythondef get_product_by_id(inventory, product_id):
    ###Find product by ID###
    for product in inventory:
        if product['id'] == product_id:
            return product
    return None

Function: Search for product
Loop: Check each product
Early return: Stop when found


Function 4: get_low_stock_products()
pythondef get_low_stock_products(inventory):
    ###Get products below minimum stock level###
    low_stock = []
    
    for product in inventory:
        if product['quantity'] <= product['min_stock']:
            low_stock.append(product)
    
    return low_stock
Line by line:
python    low_stock = []

List: Store products needing restock

python        if product['quantity'] <= product['min_stock']:

Comparison: Check if at or below minimum
<= means "less than or equal to"
Example: quantity=3, min=5 → 3 <= 5 → True (low stock)

python            low_stock.append(product)

Add: Product needs restocking


Function 5: calculate_total_value()
pythondef calculate_total_value(inventory):
    ###Calculate total inventory value###
    total = 0
    
    for product in inventory:
        value = product['quantity'] * product['price']
        total += value
    
    return total
Line by line:
python    total = 0

Accumulator: Start at zero

python        value = product['quantity'] * product['price']

Calculate: Value of this product
Example: 10 units × $5.50 = $55.00

python        total += value

Add: Accumulate total value


Function 6: calculate_product_value()
pythondef calculate_product_value(product):
    ###Calculate value of a single product###
    return product['quantity'] * product['price']

Function: Simple multiplication
Return: Total value of one product


Function 7: display_inventory()
pythondef display_inventory(inventory, title="INVENTORY"):
    ###Display inventory in formatted table###
    if not inventory:
        print(f"\n  No products in inventory.\n")
        return
Line by line:
pythondef display_inventory(inventory, title="INVENTORY"):

Default parameter: title has default value

python    print("\n" + "="*90)
    print(f"{title:^90}")
    print("="*90)

Header: 90-character wide
{title:^90}: Center title

python    print(f"{'ID':<5} {'Product':<25} {'Qty':<8} {'Price':<12} {'Value':<15} {'Status':<15}")

Column headers: Each with alignment
<5: Left-align in 5 characters
<25: Left-align in 25 characters

python    print("-"*90)

Separator: 90 dashes

python    for product in inventory:
        product_id = str(product['id'])

Type conversion: Number to string for formatting

python        name = product['name'][:22] + "..." if len(product['name']) > 25 else product['name']

Truncate long names: Keep within column width
String slicing: [:22] gets first 22 characters
Ternary operator: Add "..." if too long

python        qty = str(product['quantity'])
        price = f"${product['price']:.2f}"

Format price: Dollar sign + 2 decimals
Example: f"${5.5:.2f}" → "$5.50"

python        value = f"${calculate_product_value(product):.2f}"

Function call: Calculate and format value

python        if product['quantity'] == 0:
            status = "OUT OF STOCK"
        elif product['quantity'] <= product['min_stock']:
            status = "⚠ LOW STOCK"
        else:
            status = "✓ In Stock"

Conditional chain: Determine status
Priority: Check zero first, then low, then normal

python        print(f"{product_id:<5} {name:<25} {qty:<8} {price:<12} {value:<15} {status:<15}")

Format row: Each column aligned

python    print("-"*90)
    total_value = calculate_total_value(inventory)
    print(f"{'TOTAL INVENTORY VALUE:':<50} ${total_value:,.2f}")

Footer: Show total value
{total_value:,.2f}: Comma separator + 2 decimals
Example: {12345.67:,.2f} → "12,345.67"


Function 8: search_products()
pythondef search_products(inventory, search_term):
    ###Search products by name###
    results = []
    search_lower = search_term.lower()
    
    for product in inventory:
        if search_lower in product['name'].lower():
            results.append(product)
    
    return results
Line by line:
python    search_lower = search_term.lower()

Case-insensitive: Convert to lowercase once

python        if search_lower in product['name'].lower():

Substring search: Check if search term is in name
Example: "lap" in "laptop".lower() → True


Function 9: sort_by_value()
pythondef sort_by_value(inventory):
    ###Sort products by total value (descending)###
    return sorted(inventory, key=lambda p: calculate_product_value(p), reverse=True)
Line by line:
python    return sorted(inventory, key=lambda p: calculate_product_value(p), reverse=True)

sorted(): Returns new sorted list
key=lambda: Function to determine sort order
lambda p: Anonymous function with parameter p
calculate_product_value(p): Call function for each product
reverse=True: Highest value first

How it works:
python# For each product, calculate value:
Product 1: 10 × $5 = $50
Product 2: 5 × $20 = $100
Product 3: 15 × $3 = $45

# Sort by these values (high to low):
Product 2 ($100)
Product 1 ($50)
Product 3 ($45)

Main Program:
pythoninventory = []

List: Empty inventory

pythonprint("=== INVENTORY MANAGEMENT SYSTEM ===")
print("Commands: add, list, update, search, low-stock, value, sort, quit\n")

Instructions: Show commands


ADD COMMAND:
python    elif command == 'add':
        name = input("  Product name: ").strip()
        
        if not name:
            print("  ✗ Product name cannot be empty\n")
            continue

Validation: Reject empty names

python        try:
            quantity = int(input("  Quantity: "))
            price = float(input("  Price per unit: $"))
            min_stock = int(input("  Minimum stock level (default 5): ") or "5")

Input with default: or "5" provides fallback
How it works: If user presses Enter, input is "", which is falsy, so or "5" gives "5"

python            if quantity < 0 or price < 0 or min_stock < 0:
                print("  ✗ Values cannot be negative\n")
                continue

Validation: All values must be non-negative

python            product = add_product(inventory, name, quantity, price, min_stock)
            print(f"  ✓ Product #{product['id']} added successfully\n")

Function call: Create product
Confirmation: Show ID


UPDATE COMMAND:
python    elif command == 'update':
        if not inventory:
            print("  ✗ No products in inventory\n")
            continue

Validation: Check inventory not empty

python        print("\n  Products:")
        for p in inventory:
            print(f"    #{p['id']}: {p['name']} (Stock: {p['quantity']})")

Display: Show products with current stock

python        try:
            product_id = int(input("\n  Enter product ID: "))
            change = int(input("  Quantity change (+add/-remove): "))

Input: Get ID and change amount
Signed number: Positive or negative

python            success, message, product = update_stock(inventory, product_id, change)

Function call: Update stock
Tuple unpacking: Get three return values

python            if success:
                action = "added" if change > 0 else "removed"
                print(f"  ✓ {abs(change)} units {action}")
                print(f"  New stock: {product['quantity']}\n")

Ternary: Choose "added" or "removed"
abs(): Absolute value (removes negative sign)
Example: abs(-5) → 5


SEARCH COMMAND:
python    elif command == 'search':
        search_term = input("  Search product name: ").strip()
        
        if not search_term:
            print("  ✗ Search term cannot be empty\n")
            continue
        
        results = search_products(inventory, search_term)
        
        if results:
            display_inventory(results, f"SEARCH RESULTS: '{search_term}'")
        else:
            print(f"  ✗ No products found matching '{search_term}'\n")

Function call: Search products
Display: Show results or error message


LOW-STOCK COMMAND:
python    elif command == 'low-stock':
        low_stock = get_low_stock_products(inventory)
        
        if low_stock:
            display_inventory(low_stock, "⚠ LOW STOCK ALERT")
        else:
            print("  ✓ All products have sufficient stock\n")

Function call: Get low stock items
Display: Show alert or all-clear message


VALUE COMMAND:
python    elif command == 'value':
        if not inventory:
            print("  ✗ No products in inventory\n")
            continue
        
        total = calculate_total_value(inventory)
        print(f"\n  Total Inventory Value: ${total:,.2f}\n")

Function call: Calculate total
Format: Comma separator for thousands


"""