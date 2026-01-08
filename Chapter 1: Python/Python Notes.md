# Python Basics – Beginner Friendly Notes

[Youtube Link](https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)

These notes are written in a simple and detailed way, so even someone with no technical background can understand Python just by reading them. Examples are kept very practical and easy to follow.

## 1. What is Python?

Python is a programming language that helps us give instructions to a computer in a simple, readable way. 

You can use Python to:
- Build websites
- Work with data
- Create AI & Machine Learning models
- Automate boring tasks
- Build apps and tools

Python is popular because: 
- It is easy to read (almost like English)
- It is beginner‑friendly
- It is very powerful

## 2. Check Python Version (Very First Step)

After installing Python, you should check which version is installed on your laptop. 

**Command to check version:**

Type this in the terminal / command prompt: 

```bash
python3 --version
```

This will show something like: 

```
Python 3.12.1
```

That means Python is successfully installed. 

## 3. Your First Python Program - Open VS Code

In programming, the first program is usually Hello World. 

**Example:**

```python
print("Hello World")
```

**What does print() mean?**

`print()` tells Python to display something on the screen

## 4. Printing Text (Strings)

Text written inside quotes is called a string.

**Example:**

```python
print("I am Sushant Here")
print("Learning about AI stuff")
```

**Output:**

```
I am Sushant Here
Learning about AI stuff
```

Each `print()` statement prints on a new line.

## 5. Printing Multiple Values Together

You can print multiple things in one line using commas. 

**Example:**

```python
print("I am Sushant here,", "Learning about AI stuff.")
```

**Output:**

```
I am Sushant here, Learning about AI stuff.
```

Python automatically adds a space between items separated by commas.

## 6. Printing Numbers

Python can also print numbers directly.

**Example:**

```python
print(26)
```

**Output:**

```
26
```

**Printing Calculations**

```python
print(26 + 4)
```

**Output:**

```
30
```

Python first calculates the result and then prints it.

## 7. Variables (Very Important Concept)

A variable is a container that stores data so Python can remember it.

Think of a variable like a labeled box. 

**Example:**
- Box name: `age`
- Value inside box: `25`

**Creating a Variable**

```python
age = 25
```

Now Python remembers: 
- `age` → `25`

**Using a Variable**

```python
print(age)
```

**Output:**

```
25
```

## 8. More Variable Examples

```python
name = "Sushant"
age = 23
price = 1999

print("My name is:", name)
print("My age is:", age)
```

**Output:**

```
My name is: Sushant
My age is: 23
```

## 9. Rules for Python Variable Names

You must follow these rules when naming variables:

1. **Use only letters, numbers, and underscore `_`**
   - Valid: `user_age`, `total2`

2. **Must start with a letter or underscore**
   - Valid:  `name`, `_count`
   - Invalid: `1name`

3. **No spaces allowed**
   - Valid: `first_name`
   - Invalid: `first name`

4. **Case‑sensitive**
   - `age`, `Age`, `AGE` are different variables

5. **Do not use Python keywords**
   - Invalid: `if`, `for`, `while`

## 10. Data Types in Python

Data type tells Python what kind of value is stored.

### 10.1 Integer (int)

Whole numbers without decimal points.

```python
age = 25
count = -10
```

### 10.2 Floating Point Numbers (float)

Numbers with decimal points.

```python
pi = 3.14159
temperature = -2.5
```

⚠️ **Floating point precision issue:**

```python
print(0.1 + 0.2)
```

**Output:**

```
0.30000000000000004
```

This happens because computers store decimals approximately. 

### 10.3 String (str)

Strings store text.

```python
name = "Alice"
message = 'Hello, World!'
```

**String Operations**

```python
full_name = "John " + "Doe"   # Concatenation
first_char = name[0]           # Indexing:  'A'
substring = message[0:5]       # Slicing: 'Hello'
```

### 10.4 Boolean (bool)

Boolean values are `True` or `False`.

```python
is_student = True
has_license = False
```

Used in decision making: 

```python
if is_student: 
    print("You are a student")
else:
    print("You are not a student")
```

## 11. Sequence Data Types

### 11.1 Lists

Lists are: 
- Ordered
- Changeable (mutable)
- Can store different data types

```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, [4, 5]]
```

**Operations:**

```python
numbers. append(6)
first_item = numbers[0]
```

### 11.2 Tuples

Tuples are:
- Ordered
- Not changeable (immutable)

```python
coordinates = (10, 20)
rgb = (255, 0, 0)

x, y = coordinates
```

## 12. Dictionary (Key‑Value Data)

Dictionaries store data in `key :  value` pairs.

```python
person = {
  'name': 'Alice',
  'age': 30,
  'city': 'New York'
}
```

**Access value:**

```python
print(person['name'])
```

**Add new data:**

```python
person['job'] = 'Engineer'
```

## 13. Set Data Type

Sets store: 
- Unique values only
- No duplicates

```python
unique_numbers = {1, 2, 3, 4, 5}
unique_numbers.add(6)
unique_numbers.add(1)
```

`1` will not be added again.

## 14. None Data Type

`None` means no value.

```python
empty_value = None

if empty_value is None:
    print("No value assigned")
```

## 15. Python Keywords

Keywords are reserved words with special meaning.

You cannot use them as variable names. 

**Examples:**
- `True`, `False`, `None`
- `and`, `or`, `not`
- `if`, `else`, `elif`
- `for`, `while`, `break`, `continue`
- `try`, `except`, `finally`
- `def`, `return`, `class`
- `import`, `from`, `as`
- `async`, `await`

## 16. Printing Sum of Numbers

```python
num1 = 23
num2 = 45
sum = num1 + num2
print(sum)
```

**Output:**

```
68
```

## 17. Comments in Python

Comments are used to explain code.  Python ignores them.

### Single‑line Comment

```python
# This is a comment
```

### Multi‑line Comment

```python
"""
This is a multi‑line comment
Used for documentation
"""
```

### VS Code Shortcut

Select code and press: 
```
Ctrl + /
```

This will comment or uncomment the selected lines.

## 18. Types of operator

### Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

```python
a = 10
b = 5

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a % b)   # Modulus (remainder)
print(a ** b)  # Power (a to the power b)
```

**Output:**

```
15
5
50
2.0
0
100000
```

### Relational Operators

Relational operators are used to compare two values.

```python
a = 10
b = 5

print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
```

**Output:**

```
False
True
True
False
```

### Assignment Operators

Assignment operators are used to assign values to variables.  They can also perform operations and assign the result at the same time.

#### += Operator (Add and Assign)

```python
num = 10
num += 10  # This is same as num = num + 10
print(num)
```

**Output:**

```
20
```

#### -= Operator (Subtract and Assign)

```python
num = 10
num -= 10  # This is same as num = num - 10
print(num)
```

**Output:**

```
0
```

#### *= Operator (Multiply and Assign)

```python
num = 10
num *= 10  # This is same as num = num * 10
print(num)
```

**Output:**

```
100
```

#### /= Operator (Divide and Assign)

```python
num = 10
num /= 5  # This is same as num = num / 5
print(num)
```

**Output:**

```
2.0
```

#### %= Operator (Modulus and Assign)

```python
num = 10
num %= 5  # This is same as num = num % 5
print(num)
```

**Output:**

```
0
```

#### **= Operator (Power and Assign)

```python
num = 10
num **= 5  # This is same as num = num ** 5 (10 to the power 5)
print(num)
```

**Output:**

```
100000
```

### Logical Operators

Logical operators are used to combine conditional statements. 

#### NOT Operator

The NOT operator reverses the boolean value.  `True` becomes `False` and `False` becomes `True`.

**Example 1:**

```python
print(not False)
print(not True)
```

**Output:**

```
True
False
```

**Example 2:**

```python
a = 50
b = 30
print(not False)
print(not (a > b))
```

**Output:**

```
True
False
```

**Explanation:** `a>b` is `True` (because 50>30), so `not(True)` becomes `False`.

#### AND Operator

The AND operator returns `True` only when both conditions are `True`.

**Rules for AND operator:**
- `True AND False = False`
- `True AND True = True`
- `False AND False = False`
- `False AND True = False`

**Example 1:**

```python
val1 = True
val2 = False
print("AND Operator:", val1 and val2)
```

**Output:**

```
AND Operator: False
```

**Example 2:**

```python
val1 = True
val2 = True
print("AND Operator:", val1 and val2)
```

**Output:**

```
AND Operator: True
```

**Example 3:**

```python
val1 = False
val2 = False
print("AND Operator:", val1 and val2)
```

**Output:**

```
AND Operator: False
```

**Example 4:**

```python
val1 = False
val2 = True
print("AND Operator:", val1 and val2)
```

**Output:**

```
AND Operator: False
```

#### OR Operator

The OR operator returns `True` when at least one condition is `True`.

**Rules for OR operator:**
- `True OR False = True`
- `True OR True = True`
- `False OR False = False`
- `False OR True = True`

**Example 1:**

```python
val1 = True
val2 = False
print("OR Operator:", val1 or val2)
```

**Output:**

```
OR Operator: True
```

**Example 2:**

```python
val1 = True
val2 = True
print("OR Operator:", val1 or val2)
```

**Output:**

```
OR Operator: True
```

**Example 3:**

```python
val1 = False
val2 = False
print("OR Operator:", val1 or val2)
```

**Output:**

```
OR Operator: False
```

**Example 4:**

```python
val1 = False
val2 = True
print("OR Operator:", val1 or val2)
```

**Output:**

```
OR Operator: True
```

---

## 19. Type Conversion

There are two types of type conversion in Python:

### a.  Implicit Type Conversion

Python automatically converts types in some cases.

**Example:**

```python
a = 8
b = 2.5
sum = a + b  # 8. 0 + 2.5 = 10.5 (int + float = float)
print("Sum:", sum)
```

**Output:**

```
Sum: 10.5
```

Here Python automatically converts the integer `8` to float `8.0` and then adds it with `2.5` to give `10.5`.

### b. Explicit Type Conversion

You can manually convert types using built-in functions.

If we try to add an integer and a string, Python will raise an error because it cannot implicitly convert between these types.  So we use explicit type conversion.

**Example (This will give error):**

```python
a = str("Sushant")
b = 2. 5
print(type(a))
print(a + b)  # This will give error
```

**Output:**

```
<class 'str'>
TypeError: can only concatenate str (not "float") to str
```

## 20. Input in Python

The `input()` function is used to take input from the user.  We can directly take input from the user using `input()` function and store it in a variable.  The result of `input()` function is always a string.

**Example:**

```python
name = input("Enter your name: ")
print(type(name), "Hello", name)
```

**If user enters:** Sushant

**Output:**

```
<class 'str'> Hello Sushant
```

### Converting Input to Different Data Types

If we want to convert the input to whatever data type we want, we can use type conversion functions like `int()`, `float()`, `str()` etc.

**Example 1 (Converting to integer):**

```python
name = int(input("Enter your age: "))
print(type(name), "Hello", name)
```

**If user enters:** 24

**Output:**

```
<class 'int'> Hello 24
```

**Example 2 (Converting to float):**

```python
name = float(input("Enter your age: "))
print(type(name), "Hello", name)
```

**If user enters:** 24

**Output:**

```
<class 'float'> Hello 24.0
```

### Taking Multiple Inputs

**Example:**

```python
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))
print("Hello", name)
print("Your age is", age)
print("Your marks are", marks)
```

**If user enters:**
- Name: Sushant
- Age: 20
- Marks: 95.5

**Output:**

```
Hello Sushant
Your age is 20
Your marks are 95.5
```

## 21. Practice Programs

### Program 1: Add two numbers by taking input from user

```python
int1 = int(input("Enter first number: "))
int2 = int(input("Enter second number: "))
sum = int1 + int2
print("The sum of", int1, "and", int2, "is", sum)
```

**If user enters:**
- First number:  10
- Second number: 20

**Output:**

```
The sum of 10 and 20 is 30
```

**Note:** `int1` is a variable to store the first number.  We can use it or not, but it is better to write it to understand which data type we are using.

### Program 2: Find the area of square by taking input from user

```python
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
print("area of square is", side1 * side2)
```

**If user enters:**
- First side: 5
- Second side: 5

**Output:**

```
area of square is 25.0
```

**If user enters:**
- First side:  4. 5
- Second side: 4.5

**Output:**

```
area of square is 20.25
```

---

# Strings in Python

[Youtube Video](https://www.youtube.com/watch?v=DR4NRlj9kK8)

## What is a String?

A string is a data type that stores a series of characters (text).

### Defining Strings

We can use single quotes, double quotes, or triple quotes to define a string.

**Example:**

```python
str1 = "Hello, World!"
str2 = 'Python Programming'
str3 = """This is a string example."""

print(str1)
print(str2)
print(str3)
```

**Output:**

```
Hello, World!
Python Programming
This is a string example. 
```

### Why Different Quotes?

If a string contains single quotes, we can define it using double quotes to avoid errors.

**Right Example:**

```python
str4 = "It's a beautiful day!"
print(str4)
```

**Output:**

```
It's a beautiful day!
```

**Wrong Example:**

```python
str5 = 'It's a beautiful day!'  # This throws error
```

**Output:**

```
SyntaxError: invalid syntax
```

This is wrong because Python thinks the string ends at the second single quote (after "It").

### Escape Sequence Character

Sometimes we need some words or sentences to be on a new line. We can't just use space or click enter to do that. 

In Python, we use the escape sequence character `\n` to add a new line in a string.

**Example:**

```python
str1 = "Hello, World!\nWelcome to Python Programming."
print(str1)
```

**Output:**

```
Hello, World!
Welcome to Python Programming.
```

## String Operations

### Concatenation

Concatenation means joining two or more strings together. 

**Example:**

```python
str2 = "Hello"
str3 = "World"      
str4 = str2 + " " + str3
print(str4)
```

**Output:**

```
Hello World
```

### Length of String

The `len()` function returns the number of characters in a string.

**Example:**

```python
str5 = "Python Programming"
length = len(str5)
print("Length of the string is:", length)
```

**Output:**

```
Length of the string is: 18
```

---

### Indexing

Every character in a string has a unique index starting from **0** for the first character.

**Example:**

```
String:  "This is Python"
Index:   0123456789... 
```

**Example 1:**

```python
str6 = "This is Python"
ch = str6[6]
print(ch)
```

**Output:**

```
s
```

**Explanation:** Index 6 refers to the character 's' (after the space).

**Example 2:**

```python
str6 = "This is Python"
ch = str6[2]
print(ch)
```

**Output:**

```
i
```

**Explanation:** Index 2 refers to the character 'i'. 

### Slicing

It is used to access a part of a string.

**Syntax:**

```python
str[starting_index:ending_index]
```

- Starting index is inclusive (included in output)
- Ending index is exclusive (not included in output)

**Example:**

```python
str = "PythonProgramming"
print(str[1:4])
```

**Output:**

```
yth
```

**Explanation:** Characters from index 1 to 3 are printed (index 4 is excluded).

### Negative Indexing

In negative indexing, the last character has index -1, second last has -2, and so on.

**Example:**

```python
str = "PythonProgramming"
print(str[-7:-1])
```

**Output:**

```
rammin
```

**Explanation:**
- Index -7 is 'r'
- Index -1 is 'g'
- But since ending index is exclusive, 'g' is not included, so output is "rammin"

## String Functions

### . capitalize() Function

Converts the first character to uppercase and rest to lowercase.

**Example:**

```python
str1 = "hello world"
print(str1.capitalize())
```

**Output:**

```
Hello world
```

### .upper() Function

Converts all characters to uppercase. 

**Example:**

```python
str1 = "hello world"
print(str1.upper())
```

**Output:**

```
HELLO WORLD
```

### .lower() Function

Converts all characters to lowercase.

**Example:**

```python
str1 = "hello world"
print(str1.lower())
```

**Output:**

```
hello world
```

### .count() Function

Returns the number of occurrences of a substring in the given string.  Basically, how many times that value is present in the string.

**Example:**

```python
str1 = "hello world"
print(str1.count('l'))
```

**Output:**

```
3
```

**Explanation:** The character 'l' appears 3 times in "hello world".

### .find() Function

Returns the lowest index of the substring if found in the given string. If not found, it returns -1.

Basically, it checks whatever substring we give is present in the string or not, and if present, then how many characters are present before it (also includes spaces).

**Example 1:**

```python
str1 = "hello world"
print(str1.find('o'))
```

**Output:**

```
4
```

**Explanation:** The first occurrence of 'o' is at index 4.

**Example 2:**

```python
str1 = "hello world"
print(str1.find('z'))
```

**Output:**

```
-1
```

**Explanation:** Since 'z' is not present in the string, it returns -1.

### .replace() Function

Replaces a substring with another substring.

**Example 1:**

```python
str1 = "hello world"
print(str1.replace('world', 'Python'))
```

**Output:**

```
hello Python
```

**Example 2:**

```python
str1 = "hello world"
print(str1.replace('l', 'x'))
```

**Output:**

```
hexxo worxd
```

**Explanation:** All occurrences of 'l' are replaced with 'x'. 

### .split() Function

Splits the string into a list of words.

**Example:**

```python
str1 = "hello world"
print(str1.split())
```

**Output:**

```
['hello', 'world']
```

### .startswith() Function

Checks whether the string starts with the given substring.  Returns `True` or `False`.

**Example:**

```python
str1 = "hello world"
print(str1.startswith('hello'))
```

**Output:**

```
True
```

### .endswith() Function

Checks whether the string ends with the given substring. Returns `True` or `False`.

**Example 1:**

```python
str1 = "hello world"
print(str1.endswith('world'))
```

**Output:**

```
True
```

**Example 2:**

```python
str1 = "hello world"
print(str1.endswith('or'))
```

**Output:**

```
False
```

**Explanation:** The string doesn't end with 'or', it ends with 'world'.

## Practice Questions

### Question 1: WAP to input user's first name and print its length

```python
user_name = input("Enter your first name: ")
length = len(user_name)
print("Length of your first name is:", length)
```

**If user enters:** Sushant

**Output:**

```
Length of your first name is: 7
```

### Question 2: Count the number of times '$' appears in a string

```python
str = "Hello I have $100000 in my bank account."
print(str.count('$'))
```

**Output:**

```
1
```

---

# Conditional Statements

Conditional statements allow us to execute different code based on certain conditions.

## if, elif, else

**Syntax:** Syntax is the rule of programming. 

**Example:**

```python
light = "Pink"

if (light == 'red'):
    print("Ruk re baba")
elif (light == 'yellow'):
    print("Thoda dheeme chalo")
elif (light == 'green'):
    print("Chalo bhaiya")
else:
    print("Signal kharab hai, Bhagao")
```

**Output:**

```
Signal kharab hai, Bhagao
```

**Explanation:** Since light is "Pink", none of the if or elif conditions match, so the else block is executed.

## Using Multiple if Statements vs elif

We can use `if` also rather than `elif`, but in this case, all conditions will be checked and it can give multiple outputs.

**Example with multiple if:**

```python
num = 3

if (num > 2):
    print("Number is greater than 2")
if (num < 5):
    print("Number is less than 5")
```

**Output:**

```
Number is greater than 2
Number is less than 5
```

**Explanation:** Both conditions are checked and both are true, so both outputs are printed.

**Example with elif:**

```python
num = 3

if (num > 2):
    print("Number is greater than 2")
elif (num < 5):
    print("Number is less than 5")
```

**Output:**

```
Number is greater than 2
```

**Explanation:** When the first condition is true, the elif is not checked.  Only one output is printed.

## Grade System Example

```python
marks = int(input("Enter your marks: "))

if (marks >= 90 and marks <= 100):
    print("Grade A")
elif (marks >= 80 and marks < 90):
    print("Grade B")    
elif (marks >= 70 and marks < 80):
    print("Grade C")
else:
    print("Grade D")
```

**If user enters:** 85

**Output:**

```
Grade B
```

**If user enters:** 95

**Output:**

```
Grade A
```

**If user enters:** 65

**Output:**

```
Grade D
```

## Nesting

Writing if-else inside another if-else is called nesting. 

**Example:**

```python
age = int(input("Enter your age: "))

if (age >= 18):
    if (age >= 60):
        print("Senior citizen")
    else:
        print("Adult")
else:
    print("Minor")
```

**If user enters:** 25

**Output:**

```
Adult
```

**If user enters:** 65

**Output:**

```
Senior citizen
```

## Practice Questions

### Question 1: Check whether a number is even or odd

```python
num = int(input("Enter a number from 1 to 10: "))

if num in (2, 4, 6, 8, 10):
    print("Even number")
else:
    print("Odd number")
```

**If user enters:** 7

**Output:**

```
Odd number
```

**If user enters:** 4

**Output:**

```
Even number
```

### Question 2: Find the greatest of three numbers

```python
a = int(input("Enter first number:  "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b and a > c):
    print(a, "is the greatest number")
elif (b > a and b > c):
    print(b, "is the greatest number")  
else:
    print(c, "is the greatest number")
```

**If user enters:**
- First number: 15
- Second number: 30
- Third number: 20

**Output:**

```
30 is the greatest number
```

### Question 3: Check if a number is a multiple of 7

```python
a = int(input("Enter number: "))

if (a % 7 == 0):
    print("multiple of 7")
else:
    print("Not Multiple of 7")
```

**If user enters:** 14

**Output:**

```
multiple of 7
```

**If user enters:** 15

**Output:**

```
Not Multiple of 7
```

---

# Loops in Python

Loops are used to execute a block of code repeatedly until a certain condition is met.

## While Loop

`while` is a reserved keyword used to create a loop that runs as long as a condition is true. 

### How While Loop Works: 

1. First, we check the condition
2. If true, the block of code executes
3. Then we update the variable
4. Again we check the condition
5. This continues until the condition becomes false

### Basic While Loop Example

```python
count = 1
while count <= 5:
    print("Hello World")
    count += 1
```

**Output:**

```
Hello World
Hello World
Hello World
Hello World
Hello World
```

**Explanation:** The loop prints "Hello World" 5 times because the condition `count <= 5` is true for values 1, 2, 3, 4, and 5.

### Print Numbers from 1 to 10

```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

**Output:**

```
1
2
3
4
5
6
7
8
9
10
```

### Print Numbers from 10 to 1 (Reverse Order)

```python
j = 10
while j >= 1:
    print(j)
    j -= 1
```

**Output:**

```
10
9
8
7
6
5
4
3
2
1
```

## While Loop Practice Questions

### Question 1: Print numbers from 1 to 100

```python
i = 1
while i <= 100:
    print(i)
    i += 1
```

**Output:**

```
1
2
3
... 
99
100
```

### Question 2: Print numbers from 100 to 1

```python
j = 100
while j >= 1:  # stopping condition
    print(j)
    j -= 1
```

**Output:**

```
100
99
98
...
2
1
```

### Question 3: Print the multiplication table of 5

```python
i = 1
while i <= 10:
    print(5 * i)
    i += 1
```

**Output:**

```
5
10
15
20
25
30
35
40
45
50
```

### Question 4: Print all numbers from a list

```python
nums = [1, 4, 16, 25, 36, 49, 64, 81, 100]

index = 0
while index < len(nums):
    print(nums[index])
    index += 1
```

**Output:**

```
1
4
16
25
36
49
64
81
100
```

### Question 5: Search for a number x in a tuple using loop

```python
nums = [1, 4, 16, 25, 36, 49, 64, 81, 100]

x = 49
i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found at index:", i)
    i += 1
```

**Output:**

```
Found at index: 5
```

**Explanation:** The number 49 is present at index 5 in the list.

## Break and Continue Keywords

### Break Statement

`break` is used to terminate the loop when a certain condition is met.

**Example:**

```python
nums = [1, 4, 16, 25, 36, 49, 64, 81, 100]
x = 36
i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found at index:", i)
        break
    i += 1
```

**Output:**

```
Found at index: 4
```

**Explanation:** Once we find the number 36 at index 4, the break statement stops the loop immediately.  The loop doesn't continue checking the remaining elements.

### Continue Statement

`continue` is used to skip the current iteration and move to the next iteration of the loop.

**Example 1:**

```python
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
```

**Output:**

```
0
1
2
4
5
```

**Explanation:** When i equals 3, the continue statement skips printing 3 and moves to the next iteration.  That's why 3 is not in the output.

**Example 2:  Find odd numbers between 1 to 10 using continue**

```python
i = 1
while i <= 10:
    if (i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1
```

**Output:**

```
1
3
5
7
9
```

**Explanation:** When the number is even (`i % 2 == 0`), the continue statement skips that iteration, so only odd numbers are printed.

## For Loops

`for` loops are used to iterate over a sequence (like a list, tuple, string) or other iterable objects.

**Example:**

```python
list = [1, 4, 16, 25, 36, 49, 64, 81, 100]
for num in list:
    print(num)
```

**Output:**

```
1
4
16
25
36
49
64
81
100
```

### For Loop with String

**Example:**

```python
str = "Sushant"
for char in str:
    print(char)
```

**Output:**

```
S
u
s
h
a
n
t
```

**Explanation:** The loop iterates through each character in the string.

## For Loop Practice Questions

### Question 1: Print the elements of the following list using for loop

```python
nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
for x in nums:
    print(x)
```

**Output:**

```
2
3
5
7
11
13
17
19
23
29
```

### Question 2: Search for a number x in the list using for loop

```python
nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
x = 17
for i in range(len(nums)):
    if nums[i] == x:
        print("Found at index:", i)
```

**Output:**

```
Found at index: 6
```

**Explanation:** The number 17 is found at index 6 in the list.

## Range() Function

The `range()` function is used to generate a sequence of numbers. 

- Starts from 0 by default
- Increments by 1 by default
- Stops before a specified number

### Range with One Parameter

**Example:**

```python
seq = range(10)  # 0 to 9 (ending number 10 is never included)
for i in seq:
    print(i)
```

**Output:**

```
0
1
2
3
4
5
6
7
8
9
```

### Range with Two Parameters (start, stop)

**Example:**

```python
for i in range(5, 15):
    print(i)
```

**Output:**

```
5
6
7
8
9
10
11
12
13
14
```

**Explanation:** Starts from 5 and ends at 14 (15 is excluded).

### Range with Three Parameters (start, stop, step)

**Example:**

```python
for i in range(1, 20, 2):
    print(i)
```

**Output:**

```
1
3
5
7
9
11
13
15
17
19
```

**Explanation:** Starts from 1, ends before 20, and increments by 2 (printing only odd numbers).

## Range() Practice Questions

### Question 1: Print numbers from 1 to 50 using for and range function

```python
for i in range(1, 51):
    print(i)
```

**Output:**

```
1
2
3
... 
49
50
```

### Question 2: Print numbers from 50 to 1 using for and range function

```python
for i in range(50, 0, -1):
    print(i)
```

**Output:**

```
50
49
48
... 
2
1
```

**Explanation:** We use -1 as the step to count backwards. 

### Question 3: Print the multiplication table of any number using for and range function

```python
n = int(input("Enter a number: "))       
for i in range(1, 11):
    print(n * i)
```

**If user enters:** 7

**Output:**

```
7
14
21
28
35
42
49
56
63
70
```

## Pass Statement

`pass` is used as a placeholder for future code.  When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.

**Example:**

```python
for i in range(5):
    pass
print("This is pass statement example")
```

**Output:**

```
This is pass statement example
```

**Explanation:** The pass statement does nothing but prevents an error.  It's useful when you want to write the loop structure first and add the code later.

## Advanced Practice Questions

### Question 1: WAP to find the sum of first n numbers using while

```python
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("The sum is:", sum)
```

**Output:**

```
The sum is: 15
```

**Explanation:** 1 + 2 + 3 + 4 + 5 = 15

### Question 2: WAP to find the factorial of a number using while loop

```python
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("The factorial is:", fact)
```

**Output:**

```
The factorial is: 120
```

**Explanation:** 5! = 5 × 4 × 3 × 2 × 1 = 120

**If n = 4:**

**Output:**

```
The factorial is: 24
```

**Explanation:** 4! = 4 × 3 × 2 × 1 = 24

---

# Python Practice Programs

## Program 1: Basic Calculator

A calculator program that performs basic arithmetic operations (+, -, *, /) based on user input.

**Code:**

```python
print("Basic Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:  + - * /")
op = input("Enter operation:  ")

if op == '+':
    print("result:", num1 + num2)
elif op == '-':
    print("result:", num1 - num2)
elif op == '*':
    print("result:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("result:", num1 / num2)
    else:
        print("Undefined (cannot divide by zero)")
else:
    print("Invalid operation")
```

---

### Example Outputs:

**Example 1: Addition**

**If user enters:**
- First number: 10
- Second number: 5
- Operation: +

**Output:**

```
Basic Calculator
result: 15.0
```

---

**Example 2: Subtraction**

**If user enters:**
- First number: 20
- Second number: 8
- Operation: -

**Output:**

```
Basic Calculator
result: 12.0
```

---

**Example 3: Multiplication**

**If user enters:**
- First number: 6
- Second number: 7
- Operation: *

**Output:**

```
Basic Calculator
result: 42.0
```

---

**Example 4: Division**

**If user enters:**
- First number: 20
- Second number: 4
- Operation: /

**Output:**

```
Basic Calculator
result: 5.0
```

---

**Example 5: Division by Zero**

**If user enters:**
- First number: 10
- Second number: 0
- Operation: /

**Output:**

```
Basic Calculator
Undefined (cannot divide by zero)
```

**Explanation:** Division by zero is mathematically undefined, so we check if the second number is 0 before performing division.

---

**Example 6: Invalid Operation**

**If user enters:**
- First number: 10
- Second number: 5
- Operation: %

**Output:**

```
Basic Calculator
Invalid operation
```

**Explanation:** Since % is not one of the valid operations (+, -, *, /), the program prints "Invalid operation". 

---

## Program 2: Number Guessing Game

An interactive game where Player 1 enters a secret number, and Player 2 tries to guess it.  The program provides hints (too high/too low) until the correct number is guessed.

**Code:**

```python
print("Number Guessing Game")

# Player 1 enters a secret number
secret_number = int(input("Player 1, enter a secret number between 1 and 20: "))  
print("\n" * 50)  # Clear the screen by printing new lines

guess = None
while guess != secret_number:
    guess = int(input("Player 2, guess the number: "))
    
    if guess < secret_number: 
        print("Too low!  Try finding higher number.")
    elif guess > secret_number:
        print("Too high! Try finding lower number.")
    else:
        print("Congratulations! You've guessed the number.")
```

---

### Example Game Play:

**If Player 1 enters:** 15

**Player 2's attempts:**

```
Number Guessing Game
Player 1, enter a secret number between 1 and 20: 15
(Screen clears with 50 new lines)

Player 2, guess the number:  10
Too low! Try finding higher number.
Player 2, guess the number: 18
Too high! Try finding lower number.
Player 2, guess the number: 14
Too low! Try finding higher number.
Player 2, guess the number: 16
Too high! Try finding lower number. 
Player 2, guess the number:  15
Congratulations! You've guessed the number.
```

---
