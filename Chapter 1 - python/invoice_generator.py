"""
Question 11: Invoice Generator
Task: Generate invoices with items, quantities, prices, and calculate totals with tax.
Concepts Covered: Lists, Dictionaries, Functions, Loops, Math operations, String formatting

"""

def calculate_item_total(quantity, price):
    """Calculate total for single item"""
    return quantity * price

def calculate_subtotal(items):
    """Calculates subtotal of all items"""
    subtotal = 0
    for item in items:
        subtotal += item['total']
    return subtotal

def calculate_tax(subtotal, tax_rate):
    """Calculate final total"""
    return subtotal * (tax_rate/100)

def calculate_grand_total(subtotal, tax):
    """Calculate final total"""
    return subtotal + tax

def generate_invoice(customer_name,items, tax_rate):
    """Generate complete invoice"""
    invoice = {
        'customer': customer_name,
        'items': items,
        'subtotal': calculate_subtotal(items),
        'tax_rate': tax_rate,
        'tax': 0,
        'total': 0
    }

    invoice['tax'] = calculate_tax(invoice['subtotal'],tax_rate)
    invoice['total'] = calculate_grand_total(invoice['subtotal'], invoice['tax'])

    return invoice

def display_invoice(invoice):
    """Display formatted invoice"""
    print("\n" + "="*60)
    print(f"{'INVOICE':^60}")
    print("="*60)
    print(f"\nCustomer: {invoice['customer']}")
    print("\n"+ "-"*60)
    print(f"{'Item':<25} {'Qty':<8} {'Total':>15}")
    print ("-"*60)

    for item in invoice['items']:
        print(f"{item['name']:<25} {item['quantity']:<8} ${item['price']:<9.2f} ${item['total']:>14.2f}")


    print("-"*60)
    print(f"{'Subtotal:':<44} ${invoice['subtotal']:>14.2f}")
    print(f"{'Tax (' + str(invoice['tax_rate']) + '%):':<44} ${invoice['tax']:>14.2f}")
    print("="*60)
    print(f"{'TOTAL:':<44} ${invoice['total']:>14.2f}")
    print("="*60 + "\n")

#main program
print("+++ INVOICE GENERATOR ===\n")

customer_name = input("Customer name: ").strip()

if not customer_name:
    print("Error:Customer name is required")
else:
    items = []

    print("\nEnter Items(type 'done' when finished):")

    while True:
        item_name = input("\nItem name: ").strip()

        if item_name.lower() == 'done':
            break

        if not item_name:
            print( "x Item name cannot be empty")
            continue

        try:
            quantity = int(input("Quantity: "))
            price = float(input("Price per unit: $"))

            if quantity <= 0 or price <0:
                print(" x Quantity must be positive and price cannot be negative")
                continue
            total = calculate_item_total(quantity, price)

            item = {
                'name': item_name,
                'quantity':quantity,
                'price':price,
                'total': total
            }

            items.append(item)
            print(f" Added: {item_name} x{quantity} = ${total: 2f}")


        except ValueError:
            print(" x Please enter valud numbers")


    if items:
        try:
            tax_rate = float(input("\nTax rate (%): "))

            if tax_rate < 0:
                print(" Using 0% tax rate")
                tax_rate = 0

            invoice = generate_invoice(customer_name, items, tax_rate)
            display_invoice(invoice)

        except ValueError:
            print(" x Invalid tax rate, using 0%")
            invoice = generate_invoice(customer_name, items, 0)
            display_invoice(invoice)

    else:
        print("\nNo items added. Invoice not generated.")




"""

Code Explanation - 

Explanation:
Function 1: calculate_item_total()
pythondef calculate_item_total(quantity, price):
    return quantity * price

Function: Calculate line item total
Math: Multiply quantity by unit price
Example: 3 items × $10.50 = $31.50


Function 2: calculate_subtotal()
pythondef calculate_subtotal(items):
    subtotal = 0
    for item in items:
        subtotal += item['total']
    return subtotal

Function: Sum all item totals
Loop: Add each item's total
Variable: Accumulator pattern
Example: $31.50 + $25.00 + $15.75 = $72.25


Function 3: calculate_tax()
pythondef calculate_tax(subtotal, tax_rate):
    return subtotal * (tax_rate / 100)

Function: Calculate tax amount
Math: Percentage calculation
tax_rate / 100 converts percentage to decimal
Example: $100 × (8.5 / 100) = $100 × 0.085 = $8.50


Function 4: calculate_grand_total()
pythondef calculate_grand_total(subtotal, tax):
    return subtotal + tax

Function: Add subtotal and tax
Example: $100 + $8.50 = $108.50


Function 5: generate_invoice()
pythondef generate_invoice(customer_name, items, tax_rate):
    invoice = {
        'customer': customer_name,
        'items': items,
        'subtotal': calculate_subtotal(items),
        'tax_rate': tax_rate,
        'tax': 0,
        'total': 0
    }

Function: Create complete invoice
Dictionary: Store all invoice data
Function call: Calculate subtotal immediately

python    invoice['tax'] = calculate_tax(invoice['subtotal'], tax_rate)
    invoice['total'] = calculate_grand_total(invoice['subtotal'], invoice['tax'])

Dictionary update: Calculate and store tax and total
Chained calculations: Use previous results

python    return invoice

Return: Complete invoice dictionary


Function 6: display_invoice()
pythondef display_invoice(invoice):
    print("\n" + "="*60)
    print(f"{'INVOICE':^60}")
    print("="*60)

Function: Format and print invoice
String multiplication: "="*60 creates 60 equal signs
f-string alignment: {text:^60} centers text in 60 characters

^ = center align
< = left align
> = right align



python    print(f"\nCustomer: {invoice['customer']}")

Dictionary access: Get customer name

python    print(f"{'Item':<25} {'Qty':<8} {'Price':<10} {'Total':>15}")

f-string formatting: Column headers
{'Item':<25} - "Item" left-aligned in 25 characters
{'Total':>15} - "Total" right-aligned in 15 characters

python    for item in invoice['items']:
        print(f"{item['name']:<25} {item['quantity']:<8} ${item['price']:<9.2f} ${item['total']:>14.2f}")

Loop: Display each item
f-string: Multiple format specifiers

{value:<25} - left-align in 25 chars
{value:.2f} - 2 decimal places
${value:>14.2f} - right-align with 2 decimals



Format breakdown:
python# Format: {value:alignment width.decimals type}
{item['price']:<9.2f}
 ↑            ↑ ↑ ↑↑
 |            | | ||
 value        | | |decimal type (float)
              | | number of decimals
              | width
              alignment (< left, > right, ^ center)
python    print(f"{'Subtotal:':<44} ${invoice['subtotal']:>14.2f}")
    print(f"{'Tax (' + str(invoice['tax_rate']) + '%):':<44} ${invoice['tax']:>14.2f}")

String concatenation: Build tax label dynamically
str(): Convert number to string for concatenation

python    print(f"{'TOTAL:':<44} ${invoice['total']:>14.2f}")

Final total: Right-aligned currency format


Main Program:
pythoncustomer_name = input("Customer name: ").strip()

if not customer_name:
    print("Error: Customer name is required")

Input: Get customer name
Validation: Check not empty
not customer_name is True if string is empty

pythonelse:
    items = []

List: Store all invoice items

python    while True:
        item_name = input("\nItem name: ").strip()
        
        if item_name.lower() == 'done':
            break

Loop: Collect items
Exit condition: User types "done"

python        if not item_name:
            print("  ✗ Item name cannot be empty")
            continue

Validation: Reject empty names
continue: Skip to next iteration

python        try:
            quantity = int(input("Quantity: "))
            price = float(input("Price per unit: $"))

try block: Handle conversion errors
int(): Convert to whole number
float(): Convert to decimal

python            if quantity <= 0 or price < 0:
                print("  ✗ Quantity must be positive and price cannot be negative")
                continue

Validation: Check valid values
Logical OR: Either condition makes whole expression True

python            total = calculate_item_total(quantity, price)

Function call: Calculate line total

python            item = {
                'name': item_name,
                'quantity': quantity,
                'price': price,
                'total': total
            }
            
            items.append(item)

Dictionary: Create item record
List method: Add to items list

python            print(f"  ✓ Added: {item_name} x{quantity} = ${total:.2f}")

Confirmation: Show what was added

python        except ValueError:
            print("  ✗ Please enter valid numbers")

Exception handling: Catch conversion errors

python    if items:
        try:
            tax_rate = float(input("\nTax rate (%): "))
            
            if tax_rate < 0:
                print("  Using 0% tax rate")
                tax_rate = 0

Conditional: Only proceed if items exist
Validation: Ensure non-negative tax

python            invoice = generate_invoice(customer_name, items, tax_rate)
            display_invoice(invoice)
```
- **Function calls:** Generate and display invoice

**Example Run:**
```
=== INVOICE GENERATOR ===

Customer name: ABC Corporation

Enter items (type 'done' when finished):

Item name: Laptop
Quantity: 2
Price per unit: $899.99
  ✓ Added: Laptop x2 = $1799.98

Item name: Mouse
Quantity: 3
Price per unit: $25.50
  ✓ Added: Mouse x3 = $76.50

Item name: Keyboard
Quantity: 2
Price per unit: $75.00
  ✓ Added: Keyboard x2 = $150.00

Item name: done

Tax rate (%): 8.5

============================================================
                         INVOICE                           
============================================================

Customer: ABC Corporation

------------------------------------------------------------
Item                      Qty      Price      Total
------------------------------------------------------------
Laptop                    2        $899.99    $      1799.98
Mouse                     3        $25.50     $        76.50
Keyboard                  2        $75.00     $       150.00
------------------------------------------------------------
Subtotal:                                     $      2026.48
Tax (8.5%):                                   $       172.25
============================================================
TOTAL:                                        $      2198.73
============================================================


"""