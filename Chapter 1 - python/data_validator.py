"""

=== DATA VALIDATOR ===
Validation types: email, phone, card, postal, password, quit

What to validate? email
  Enter email: user@example.com

  Email: user@example.com
  Status: ✓ VALID
  Message: Valid email

What to validate? phone
  Enter phone number: (555) 123-4567

  Phone: (555) 123-4567
  Status: ✓ VALID
  Message: Valid phone number

What to validate? password
  Enter password: hello

  Password: *****
  Status: ✗ INVALID
  Message: Very weak password. Issues: At least 8 characters required, Add uppercase letters, Add numbers, Add special characters

What to validate? quit
Goodbye!



"""


def validate_email(email):
    """Validate email format"""
    # Basic validation: contains @ and . after @
    if '@' not in email:
        return False, "Missing @ symbol"
    
    parts = email.split('@')
    if len(parts) != 2:
        return False, "Invalid @ usage"
    
    local, domain = parts
    
    if not local or not domain:
        return False, "Empty local or domain part"
    
    if '.' not in domain:
        return False, "Domain must contain a dot"
    
    domain_parts = domain.split('.')
    if len(domain_parts[-1]) < 2:
        return False, "Invalid domain extension"
    
    return True, "Valid email"

def validate_phone(phone):
    """Validate phone number (10 digits)"""
    # Remove common separators
    cleaned = phone.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
    
    if not cleaned.isdigit():
        return False, "Contains non-digit characters"
    
    if len(cleaned) != 10:
        return False, f"Must be 10 digits (got {len(cleaned)})"
    
    return True, "Valid phone number"

def validate_credit_card(card_number):
    """Validate credit card format (16 digits)"""
    # Remove spaces and dashes
    cleaned = card_number.replace(' ', '').replace('-', '')
    
    if not cleaned.isdigit():
        return False, "Contains non-digit characters"
    
    if len(cleaned) != 16:
        return False, f"Must be 16 digits (got {len(cleaned)})"
    
    # Luhn algorithm (basic check)
    total = 0
    reverse_digits = cleaned[::-1]
    
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        
        if i % 2 == 1:  # Every second digit
            n = n * 2
            if n > 9:
                n = n - 9
        
        total += n
    
    if total % 10 != 0:
        return False, "Failed Luhn algorithm check"
    
    return True, "Valid credit card number"

def validate_postal_code(postal_code, country='US'):
    """Validate postal code"""
    cleaned = postal_code.replace(' ', '').replace('-', '')
    
    if country.upper() == 'US':
        # US ZIP code: 5 or 9 digits
        if not cleaned.isdigit():
            return False, "ZIP code must contain only digits"
        
        if len(cleaned) not in [5, 9]:
            return False, "ZIP code must be 5 or 9 digits"
        
        return True, "Valid US ZIP code"
    
    elif country.upper() == 'IN':
        # India PIN code: 6 digits
        if not cleaned.isdigit():
            return False, "PIN code must contain only digits"
        
        if len(cleaned) != 6:
            return False, "PIN code must be 6 digits"
        
        return True, "Valid Indian PIN code"
    
    else:
        return False, "Unsupported country code"

def validate_password_strength(password):
    """Check password strength"""
    issues = []
    score = 0
    
    if len(password) >= 8:
        score += 1
    else:
        issues.append("At least 8 characters required")
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password)
    
    if has_upper:
        score += 1
    else:
        issues.append("Add uppercase letters")
    
    if has_lower:
        score += 1
    else:
        issues.append("Add lowercase letters")
    
    if has_digit:
        score += 1
    else:
        issues.append("Add numbers")
    
    if has_special:
        score += 1
    else:
        issues.append("Add special characters")
    
    if score == 5:
        return True, "Strong password"
    elif score >= 3:
        return False, f"Weak password. Issues: {', '.join(issues)}"
    else:
        return False, f"Very weak password. Issues: {', '.join(issues)}"

def display_validation_result(data_type, data, is_valid, message):
    """Display validation result"""
    status = "✓ VALID" if is_valid else "✗ INVALID"
    print(f"\n  {data_type}: {data}")
    print(f"  Status: {status}")
    print(f"  Message: {message}\n")

# Main program
print("=== DATA VALIDATOR ===")
print("Validation types: email, phone, card, postal, password, quit\n")

while True:
    data_type = input("What to validate? ").lower().strip()
    
    if data_type == 'quit':
        print("Goodbye!")
        break
    
    elif data_type == 'email':
        email = input("  Enter email: ").strip()
        is_valid, message = validate_email(email)
        display_validation_result("Email", email, is_valid, message)
    
    elif data_type == 'phone':
        phone = input("  Enter phone number: ").strip()
        is_valid, message = validate_phone(phone)
        display_validation_result("Phone", phone, is_valid, message)
    
    elif data_type == 'card':
        card = input("  Enter credit card number: ").strip()
        is_valid, message = validate_credit_card(card)
        display_validation_result("Credit Card", card, is_valid, message)
    
    elif data_type == 'postal':
        postal = input("  Enter postal code: ").strip()
        country = input("  Country (US/IN): ").strip()
        
        if not country:
            country = 'US'
        
        is_valid, message = validate_postal_code(postal, country)
        display_validation_result(f"Postal Code ({country})", postal, is_valid, message)
    
    elif data_type == 'password':
        password = input("  Enter password: ").strip()
        is_valid, message = validate_password_strength(password)
        display_validation_result("Password", "*" * len(password), is_valid, message)
    
    else:
        print("  ✗ Unknown validation type\n")





"""

Detailed Line-by-Line Explanation:

Function 1: validate_email()
pythondef validate_email(email):
    ###Validate email format###

Function: Check if email format is correct
Parameter: Email string to validate

python    if '@' not in email:
        return False, "Missing @ symbol"

Conditional: Check if @ symbol exists
String operator: in checks if substring exists
return tuple: (is_valid, error_message)
Example: '@' not in "testgmail.com" → True (missing @)

python    parts = email.split('@')

String method: .split('@') separates by @ symbol
Example: "user@example.com".split('@') → ["user", "example.com"]

python    if len(parts) != 2:
        return False, "Invalid @ usage"

Validation: Should have exactly 2 parts
len(): Count number of parts
Example: "user@@example.com".split('@') → ["user", "", "example.com"] (3 parts = invalid)

python    local, domain = parts

Tuple unpacking: Assign both parts to variables
local = part before @
domain = part after @
Example: ["user", "example.com"] → local="user", domain="example.com"

python    if not local or not domain:
        return False, "Empty local or domain part"

Conditional: Check both parts have content
not local is True if local is empty string
or operator: True if either condition is True
Example: "@example.com" → local="" (empty, invalid)

python    if '.' not in domain:
        return False, "Domain must contain a dot"

Validation: Domain must have a dot
Example: "user@example" → no dot in domain (invalid)

python    domain_parts = domain.split('.')

Split domain: Separate by dots
Example: "example.com".split('.') → ["example", "com"]

python    if len(domain_parts[-1]) < 2:
        return False, "Invalid domain extension"

List indexing: [-1] gets last element
Validation: Extension must be at least 2 characters
Example: "example.c" → extension "c" (too short)

python    return True, "Valid email"

Success: Email passed all checks


Function 2: validate_phone()
pythondef validate_phone(phone):
    ###Validate phone number (10 digits)###
    cleaned = phone.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
Line by line:
pythondef validate_phone(phone):

Function: Validate phone number format

python    cleaned = phone.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')

Chained replacements: Remove common separators
String method: .replace(old, new) replaces all occurrences
Chaining: Each .replace() works on result of previous

Step-by-step example:
pythonphone = "(555) 123-4567"
.replace('-', '')   → "(555) 123 4567"
.replace(' ', '')   → "(555)1234567"
.replace('(', '')   → "555)1234567"
.replace(')', '')   → "5551234567"
# cleaned = "5551234567"
python    if not cleaned.isdigit():
        return False, "Contains non-digit characters"

String method: .isdigit() checks if all characters are digits
not reverses the result
Example: "5551234567".isdigit() → True
Example: "555abc4567".isdigit() → False

python    if len(cleaned) != 10:
        return False, f"Must be 10 digits (got {len(cleaned)})"

Validation: Must be exactly 10 digits
f-string: Insert actual length in message
Example: If 9 digits → "Must be 10 digits (got 9)"

python    return True, "Valid phone number"

Success: Phone number is valid


Function 3: validate_credit_card()
pythondef validate_credit_card(card_number):
    ###Validate credit card format (16 digits)###
    cleaned = card_number.replace(' ', '').replace('-', '')
Line by line:
pythondef validate_credit_card(card_number):

Function: Validate credit card using Luhn algorithm

python    cleaned = card_number.replace(' ', '').replace('-', '')

Clean input: Remove spaces and dashes
Example: "4532 0151 1283 0366" → "4532015112830366"

python    if not cleaned.isdigit():
        return False, "Contains non-digit characters"

Validation: Only digits allowed

python    if len(cleaned) != 16:
        return False, f"Must be 16 digits (got {len(cleaned)})"

Validation: Credit cards are 16 digits

python    # Luhn algorithm (basic check)
    total = 0
    reverse_digits = cleaned[::-1]

Luhn algorithm: Industry standard validation
String slicing: [::-1] reverses the string
Example: "1234"[::-1] → "4321"

Why reverse?
Luhn algorithm processes from right to left
python    for i, digit in enumerate(reverse_digits):

Loop: Process each digit with its position
enumerate(): Get index and character

python        n = int(digit)

Type conversion: Convert character to integer
Example: int('5') → 5

python        if i % 2 == 1:  # Every second digit

Modulo operator: % gives remainder
i % 2 gives 0 (even) or 1 (odd)
Position 1, 3, 5... are "every second digit" from right

python            n = n * 2

Double the digit: Part of Luhn algorithm

python            if n > 9:
                n = n - 9

Adjustment: If doubled digit is > 9, subtract 9
Example: 8 × 2 = 16, then 16 - 9 = 7

Why subtract 9?
It's equivalent to adding the digits: 1 + 6 = 7
python        total += n

Accumulate: Add to running total

python    if total % 10 != 0:
        return False, "Failed Luhn algorithm check"

Final check: Total must be divisible by 10
Example: If total = 70 → 70 % 10 = 0 (valid)
Example: If total = 73 → 73 % 10 = 3 (invalid)

python    return True, "Valid credit card number"
```
- **Success:** Passed Luhn check

**Luhn Algorithm Example:**
```
Card: 4532015112830366
Reverse: 6630382115105324

Position: 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
Digit:    6  6  3  0  3  8  2  1  1  5  1  0  5  3  2  4
Double:   6  12 3  0  3  16 2  2  1  10 1  0  5  6  2  8
Adjust:   6  3  3  0  3  7  2  2  1  1  1  0  5  6  2  8

Sum: 6+3+3+0+3+7+2+2+1+1+1+0+5+6+2+8 = 50
50 % 10 = 0 → Valid!

Function 4: validate_postal_code()
pythondef validate_postal_code(postal_code, country='US'):
    ###Validate postal code###
    cleaned = postal_code.replace(' ', '').replace('-', '')
Line by line:
pythondef validate_postal_code(postal_code, country='US'):

Function: Validate postal code
Default parameter: country defaults to 'US'

python    cleaned = postal_code.replace(' ', '').replace('-', '')

Clean input: Remove spaces and dashes

python    if country.upper() == 'US':

String method: .upper() converts to uppercase
Makes comparison case-insensitive

python        if not cleaned.isdigit():
            return False, "ZIP code must contain only digits"

US rule: Only digits allowed

python        if len(cleaned) not in [5, 9]:
            return False, "ZIP code must be 5 or 9 digits"

List membership: Check if length is 5 or 9
List: [5, 9] contains valid lengths
Example: 5 in [5, 9] → True
Example: 7 in [5, 9] → False

python        return True, "Valid US ZIP code"

Success: Valid US ZIP

python    elif country.upper() == 'IN':

India validation: Different rules

python        if not cleaned.isdigit():
            return False, "PIN code must contain only digits"
        
        if len(cleaned) != 6:
            return False, "PIN code must be 6 digits"
        
        return True, "Valid Indian PIN code"

India rule: Exactly 6 digits

python    else:
        return False, "Unsupported country code"

Unknown country: Return error


Function 5: validate_password_strength()
pythondef validate_password_strength(password):
    ###Check password strength###
    issues = []
    score = 0
Line by line:
pythondef validate_password_strength(password):

Function: Evaluate password strength

python    issues = []
    score = 0

List: Store problems found
Integer: Track strength score (0-5)

python    if len(password) >= 8:
        score += 1
    else:
        issues.append("At least 8 characters required")

Length check: Minimum 8 characters
score += 1: Increment score
List method: Add issue if too short

python    has_upper = any(c.isupper() for c in password)

any() function: Returns True if any item is True
Generator expression: c.isupper() for c in password
How it works: Checks each character, stops at first uppercase

Breakdown:
pythonpassword = "Hello123"
# Generator creates: False, True, False, False, False, False, False, False
# any() returns True (found at least one True)
python    has_lower = any(c.islower() for c in password)

Check lowercase: Same pattern
Example: "H".islower() → False
Example: "h".islower() → True

python    has_digit = any(c.isdigit() for c in password)

Check digits: Same pattern
Example: "5".isdigit() → True

python    has_special = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password)

Check special characters: Different syntax
c in '!@#...' checks if character is in special chars string

python    if has_upper:
        score += 1
    else:
        issues.append("Add uppercase letters")

Conditional: Add point if has uppercase
Otherwise record issue

Pattern repeats for:

Lowercase check
Digit check
Special character check

python    if score == 5:
        return True, "Strong password"
    elif score >= 3:
        return False, f"Weak password. Issues: {', '.join(issues)}"
    else:
        return False, f"Very weak password. Issues: {', '.join(issues)}"

Grading: Based on score
String method: ', '.join(issues) combines list items
Example: ['Issue1', 'Issue2'] → "Issue1, Issue2"


Function 6: display_validation_result()
pythondef display_validation_result(data_type, data, is_valid, message):
    ###Display validation result###
    status = "✓ VALID" if is_valid else "✗ INVALID"
    print(f"\n  {data_type}: {data}")
    print(f"  Status: {status}")
    print(f"  Message: {message}\n")
Line by line:
pythondef display_validation_result(data_type, data, is_valid, message):

Function: Format and display validation result

python    status = "✓ VALID" if is_valid else "✗ INVALID"

Ternary operator: Choose status symbol

python    print(f"\n  {data_type}: {data}")
    print(f"  Status: {status}")
    print(f"  Message: {message}\n")

Output: Three-line formatted result


Main Program:
pythonprint("=== DATA VALIDATOR ===")
print("Validation types: email, phone, card, postal, password, quit\n")

Instructions: Show available validations

pythonwhile True:
    data_type = input("What to validate? ").lower().strip()

Loop: Keep running
Input: Get validation type

python    if data_type == 'quit':
        print("Goodbye!")
        break

Exit condition:

python    elif data_type == 'email':
        email = input("  Enter email: ").strip()
        is_valid, message = validate_email(email)
        display_validation_result("Email", email, is_valid, message)

Email validation: Get input, validate, display result
Tuple unpacking: Get both return values

Pattern repeats for:

phone
card
postal (with country input)
password (hides password with asterisks)




"""