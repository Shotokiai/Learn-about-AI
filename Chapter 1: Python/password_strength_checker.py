#Question - Password Strength Checker
#Task: Check password strength based on length, uppercase, lowercase, digits, and special characters.


import string


def check_password_strength(password):
    "Analyze password and return strength score and feedback"
    score = 0  # integer to track strength (0-6)
    feedback = [] #list to store improvement suggestions

    #check length
    if len(password) >=8:
        score += 2
    elif len(password) >=6:
        score +=1
    else:
        feedback.append("Password too short (min 8 characters is required)")


    #check for uppercase
    has_upper = False #Variable: Boolean flag (True/False)
    for char in password:
        if char.isupper():
            has_upper = True
            break

    if has_upper:
        score +=1
    else:
        feedback.append("Add uppercase letters")

        
    #check for lowercase

    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break


    if has_lower:
        score +=1
    else:
        feedback.append("Add lowercase letters")

    
    #check for digits
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit =True
            break
    
    if has_digit:
        score +=1
    else:
        feedback.append("Add numbers please!")

    
    #check for special characters
    has_special = False
    for char in password:
        if char in string.punctuation:
            has_special = True
            break
    
    if has_special:
        score +=1
    else:
        feedback.append("Add special character from (!@#$%^&*)")

    return score,feedback


def get_strength_level(score):
    """Convert score to strength description"""
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

#Main Program

password = input("Enter password to check: ")

score, feedback = check_password_strength(password)
strength = get_strength_level(score)

print(f"\n{'='*40}")  #'='*40 repeats = 40 times
print(f"Password Strength: {strength}")
print(f"Score: {score}/6")
print(f"{'='*40}")

if feedback:
    print("\nSuggestions:") #\n print on next line the word "Suggestion"
    for suggestion in feedback:
        print(f"{suggestion}")

        """
        - **Conditional:** `if feedback:` checks if list is not empty
        - **Loop:** Display each suggestion

        """
else:
    print("\n Excellent Password!")



##################################









