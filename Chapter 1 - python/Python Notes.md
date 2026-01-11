# Python Basics Beginner Friendly Notes

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
- It is beginnerΓÇæfriendly
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
- `age` ΓåÆ `25`

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

4. **CaseΓÇæsensitive**
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

ΓÜá∩╕Å **Floating point precision issue:**

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

## 12. Dictionary (KeyΓÇæValue Data)

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

### SingleΓÇæline Comment

```python
# This is a comment
```

### MultiΓÇæline Comment

```python
"""
This is a multiΓÇæline comment
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

**Explanation:** 5! = 5 ├ù 4 ├ù 3 ├ù 2 ├ù 1 = 120

**If n = 4:**

**Output:**

```
The factorial is: 24
```

**Explanation:** 4! = 4 ├ù 3 ├ù 2 ├ù 1 = 24

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

# Functions in Python

Functions are a block of statements that perform a specific task.

## Why Do We Use Functions?

- To avoid repetition of code
- To make code reusable
- To reduce redundancy
- To make code more organized and readable
- To break down complex problems into smaller, manageable parts

---

## Function Definition and Function Call

### Basic Structure:

```python
def function_name(parameters):
    # code block
    return value
```

- **def** - keyword to define a function
- **function_name** - name of the function
- **parameters** - variables that receive values (optional)
- **return** - sends back a result (optional)

---

### Example 1: Function with Parameters

```python
def calc_sum(a, b):  # a and b are parameters
    sum = a + b
    print("The sum is:", sum)
    return sum

# Function call
calc_sum(3, 5)  # 3 and 5 are arguments
```

**Output:**

```
The sum is: 8
```

**Explanation:**
- Parameters (a, b) are the variables in the function definition
- Arguments (3, 5) are the actual values passed when calling the function

---

### Example 2: Function without Parameters

```python
def print_hello():
    print("Hello, World!")

print_hello()
```

**Output:**

```
Hello, World!
```

---

### Example 3: Average of Three Numbers

```python
def average_of_three(x, y, z):
    avg = (x + y + z) / 3
    return avg

result = average_of_three(10, 20, 30)
print("The average is:", result)
```

**Output:**

```
The average is: 20.0
```

**Explanation:**
- The function calculates the average: (10 + 20 + 30) / 3 = 20.0
- The result is stored in the variable `result` and then printed

---

## Types of Functions

### 1. Built-in Functions

These are functions that are pre-defined in Python and can be used directly without any need for definition.

**Examples:**

```python
print("Hello, World!")  # print() is a built-in function
length = len("Python")  # len() is a built-in function
print(length)

numbers = range(5)      # range() is a built-in function
print(list(numbers))

data_type = type(42)    # type() is a built-in function
print(data_type)
```

**Output:**

```
Hello, World!
6
[0, 1, 2, 3, 4]
<class 'int'>
```

**Common Built-in Functions:**
- `print()` - displays output
- `len()` - returns length
- `type()` - returns data type
- `range()` - generates sequence of numbers
- `input()` - takes user input
- `int()`, `float()`, `str()` - type conversion

---

### 2. User-Defined Functions

These are functions that are defined by us (the user) to perform specific tasks.

**Example:**

```python
def greet_user(name):
    print("Hello,", name)

greet_user("Sushant")
```

**Output:**

```
Hello, Sushant
```

---

## Default Parameters

We can assign default values to parameters in the function definition. If no argument is passed, the default value is used.

**Example:**

```python
def cal_prod(b, a=5):  # a has default value 5
    print(a * b)
    return a * b

cal_prod(3)      # uses default value of a (5)
cal_prod(3, 10)  # overrides default value of a with 10
```

**Output:**

```
15
30
```

**Explanation:**
- First call: `cal_prod(3)` → uses a=5 (default), so 5 * 3 = 15
- Second call: `cal_prod(3, 10)` → uses a=10, so 10 * 3 = 30

---

## Practice Questions for Functions

### Question 1: Write a function to print the length of a list

```python
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

def print_list_length(list):
    print(len(list))

print_list_length(cities)
```

**Output:**

```
5
```

---

### Question 2: WAF to print the elements of the list in a single line

```python
heros = ["Ironman", "Thor", "Hulk", "Captain America", "Black Widow"]

def print_list_elements(list):
    for item in list:
        print(item, end=" ")  # "end" parameter prints in single line with space

print_list_elements(heros)
```

**Output:**

```
Ironman Thor Hulk Captain America Black Widow
```

**Explanation:**
- `end=" "` parameter changes the default line break to a space
- By default, `print()` ends with a newline (\n)
- Here we changed it to space so all items print on one line

---

### Question 3: Find the factorial of a number using functions

```python
n = 7

def calc_factorial(i):
    fact = 1
    for j in range(1, i+1):
        fact = fact * j
    print("The factorial of", i, "is", fact)

calc_factorial(n)
```

**Output:**

```
The factorial of 7 is 5040
```

**Explanation:** 7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040

---

### Question 4: WAF to convert USD to INR

```python
def converter(usd_val):
    inr_val = (usd_val * 82.74)
    print(usd_val, "USD =", inr_val, "INR")

converter(2)
converter(10)
converter(100)
```

**Output:**

```
2 USD = 165.48 INR
10 USD = 827.4 INR
100 USD = 8274.0 INR
```

---

## Recursion in Functions

Recursion is when a function calls itself to solve a problem.

**Key Points about Recursion:**
- A recursive function must have a base case (stopping condition)
- Without a base case, the function will call itself infinitely (infinite recursion)
- Each recursive call should move closer to the base case

---

### Example 1: Print Numbers in Descending Order

```python
def show(n):
    if n == -2:  # Base case
        return
    print(n)
    show(n-1)    # Recursive call - function calling itself

show(5)
```

**Output:**

```
5
4
3
2
1
0
-1
```

**How it works:**
- `show(5)` prints 5, then calls `show(4)`
- `show(4)` prints 4, then calls `show(3)`
- `show(3)` prints 3, then calls `show(2)`
- `show(2)` prints 2, then calls `show(1)`
- `show(1)` prints 1, then calls `show(0)`
- `show(0)` prints 0, then calls `show(-1)`
- `show(-1)` prints -1, then calls `show(-2)`
- `show(-2)` hits the base case and returns (stops)

---

### Example 2: Factorial Using Recursion

**Recurrence Relation:** It is an equation that recursively defines a sequence where the next term is a function of the previous terms.

For factorial: **n! = n × (n-1)!**

```python
def fact(n):
    if (n == 1 or n == 0):  # Base case
        return 1
    return fact(n-1) * n    # Recursive call

print(fact(5))
print(fact(7))
print(fact(0))
```

**Output:**

```
120
5040
1
```

**Explanation for fact(5):**
- `fact(5)` = 5 × `fact(4)`
- `fact(4)` = 4 × `fact(3)`
- `fact(3)` = 3 × `fact(2)`
- `fact(2)` = 2 × `fact(1)`
- `fact(1)` = 1 (base case)
- Working backwards: 2 × 1 = 2 → 3 × 2 = 6 → 4 × 6 = 24 → 5 × 24 = 120





Recursion in Functions
Recursion is when a function calls itself to solve a problem.
Key Points about Recursion:
A recursive function must have a base case (stopping condition)
Without a base case, the function will call itself infinitely (infinite recursion)
Each recursive call should move closer to the base case

Example 1: Print Numbers in Descending Order
def show(n):
    if n == -2:  # Base case
        return
    print(n)
    show(n-1)    # Recursive call - function calling itself

show(5)
```

**Output:**
```
5
4
3
2
1
0
-1
How it works:
show(5) prints 5, then calls show(4)
show(4) prints 4, then calls show(3)
show(3) prints 3, then calls show(2)
show(2) prints 2, then calls show(1)
show(1) prints 1, then calls show(0)
show(0) prints 0, then calls show(-1)
show(-1) prints -1, then calls show(-2)
show(-2) hits the base case and returns (stops)

Example 2: Factorial Using Recursion
Recurrence Relation: It is an equation that recursively defines a sequence where the next term is a function of the previous terms.
For factorial: n! = n × (n-1)!
def fact(n):
    if (n == 1 or n == 0):  # Base case
        return 1
    return fact(n-1) * n    # Recursive call

print(fact(5))
print(fact(7))
print(fact(0))
```

**Output:**
```
120
5040
1
```

**Explanation for fact(5):**
- `fact(5)` = 5 × `fact(4)`
- `fact(4)` = 4 × `fact(3)`
- `fact(3)` = 3 × `fact(2)`
- `fact(2)` = 2 × `fact(1)`
- `fact(1)` = 1 (base case)
- Working backwards: 2 × 1 = 2 → 3 × 2 = 6 → 4 × 6 = 24 → 5 × 24 = 120

---

## Call Stack

The **call stack** is a data structure that stores information about the active functions of a program.

### How Call Stack Works:

1. When a function is called, a new **frame** is created and **pushed** onto the call stack
2. The frame contains:
   - Function parameters
   - Local variables
   - Return address (where to go back after function completes)
3. When a function completes, its frame is **popped** from the stack
4. Control returns to the previous function

### Visual Example with fact(3):
```
Call Stack Visualization:

Step 1: fact(3) is called
┌──────────────┐
│   fact(3)    │
└──────────────┘

Step 2: fact(3) calls fact(2)
┌──────────────┐
│   fact(2)    │
├──────────────┤
│   fact(3)    │
└──────────────┘

Step 3: fact(2) calls fact(1)
┌──────────────┐
│   fact(1)    │
├──────────────┤
│   fact(2)    │
├──────────────┤
│   fact(3)    │
└──────────────┘

Step 4: fact(1) returns 1, popped from stack
┌──────────────┐
│   fact(2)    │  ← receives 1, calculates 2*1=2
├──────────────┤
│   fact(3)    │
└──────────────┘

Step 5: fact(2) returns 2, popped from stack
┌──────────────┐
│   fact(3)    │  ← receives 2, calculates 3*2=6
└──────────────┘

Step 6: fact(3) returns 6, final result
```

**Simple Understanding:** Think of the call stack like a stack of plates:
- When you call a function, you add a plate on top (push)
- When a function finishes, you remove the top plate (pop)
- You always work with the top plate first (Last In, First Out - LIFO)

---

## Practice Questions on Recursion

### Question 5: Write a recursive function to calculate the sum of n natural numbers

**Problem:** Find sum of first n natural numbers (1 + 2 + 3 + ... + n)

**Recurrence Relation:** `sum(n) = n + sum(n-1)`

```python
def cal_sum(n):
    if (n == 0):  # Base case
        return 0
    return cal_sum(n-1) + n  # Recursive call

sum = cal_sum(5)
print(sum)

sum2 = cal_sum(10)
print(sum2)
```

**Output:**

```
15
55
```

**Explanation for cal_sum(5):**
- `cal_sum(5)` = 5 + `cal_sum(4)`
- `cal_sum(4)` = 4 + `cal_sum(3)`
- `cal_sum(3)` = 3 + `cal_sum(2)`
- `cal_sum(2)` = 2 + `cal_sum(1)`
- `cal_sum(1)` = 1 + `cal_sum(0)`
- `cal_sum(0)` = 0 (base case)
- Working backwards: 1 + 0 = 1 → 2 + 1 = 3 → 3 + 3 = 6 → 4 + 6 = 10 → 5 + 10 = 15

**For cal_sum(10):**
Sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

---

## Comparison: Iteration vs Recursion

### Factorial Using Loop (Iteration)

```python
def fact_iterative(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

print(fact_iterative(5))
```

**Output:**

```
120
```

---

### Factorial Using Recursion

```python
def fact_recursive(n):
    if (n == 1 or n == 0):
        return 1
    return fact_recursive(n-1) * n

print(fact_recursive(5))
```

**Output:**
```
120
---

### When to Use Iteration vs Recursion

**Use Iteration when:**
- The problem is simple and straightforward
- You need better performance (faster, uses less memory)
- You want to avoid stack overflow errors

**Use Recursion when:**
- The problem naturally fits a recursive structure (tree traversal, divide and conquer)
- The code is more readable and elegant with recursion
- You're working with recursive data structures

---

# Lists and Tuples in Python

## What is a List?

A list is a built-in data type that stores a set of values.

### Key Features of Lists:

- Can store elements of different data types (int, float, string, boolean, etc.)
- **Lists are mutable** (can be changed/modified)
- Created using square brackets `[ ]`
- Elements are ordered and can be accessed by index

---

## Why Use Lists?

Without lists, we would need to store each value in a separate variable:

```python
marks1 = 94.2
marks2 = 88.5
marks3 = 76.5
marks4 = 82.0
marks5 = 91.3
marks6 = 79.5
```

This is inefficient and difficult to manage!

With lists, we can store all values in one variable:

```python
marks = [94.2, 88.5, 76.5, 82.0, 91.3, 79.5]
print(marks)
```

**Output:**

```
[94.2, 88.5, 76.5, 82.0, 91.3, 79.5]
```

---

## Accessing List Elements

List elements can be accessed using their index (position). Index starts from 0.

```python
marks = [94.2, 88.5, 76.5, 82.0, 91.3, 79.5]
print(marks[0])  # First element
print(marks[2])  # Third element
print(marks[5])  # Last element
```

**Output:**

```
94.2
76.5
79.5
```

---

## Lists Can Store Different Data Types

```python
students = ["Rahul", 95, 23, "Delhi"]
print(students)
```

**Output:**

```
['Rahul', 95, 23, 'Delhi']
```

**Explanation:** This list contains strings, integers - all different data types in one list.

---

## Lists are Mutable (Can Be Changed)

```python
students = ["Rahul", 95, 23, "Delhi"]
students[0] = "Arjun"  # Changing first element
print(students)
```

**Output:**

```
['Arjun', 95, 23, 'Delhi']
```

**Explanation:** We successfully changed "Rahul" to "Arjun". This is possible because lists are mutable.

---

## Strings vs Lists: Immutable vs Mutable

### Strings are Immutable (Cannot Be Changed)

```python
str = "Hello" 
print(str[0])
str[0] = "y"  # This will give an error
```

**Output:**

```
H
TypeError: 'str' object does not support item assignment
```

**Explanation:** Strings cannot be modified after creation. This is called immutability.

---

### Lists are Mutable (Can Be Changed)

```python
list = ["Hello", "World"]
print(list[0])
list[0] = "Hi"  # This works fine
print(list)
```

**Output:**

```
Hello
['Hi', 'World']
```



---

## List Slicing

List slicing allows us to access a portion of the list.

**Syntax:** `list[start:end]`
- **start** index is inclusive (included)
- **end** index is exclusive (not included)

```python
marks = [94.2, 88.5, 76.5, 82.0, 91.3, 79.5, 85.0, 90.5]
```

---

### Example 1: Slice from index 1 to 5

```python
marks = [94.2, 88.5, 76.5, 82.0, 91.3, 79.5, 85.0, 90.5]
print(marks[1:5])
```

**Output:**

```
[88.5, 76.5, 82.0, 91.3]
```

**Explanation:** Elements from index 1 to 4 (5-1) are included.

---

### Example 2: Slice from index 1 to end

```python
marks = [94.2, 88.5, 76.5, 82.0, 91.3, 79.5, 85.0, 90.5]
print(marks[1:])
```

**Output:**

```
[88.5, 76.5, 82.0, 91.3, 79.5, 85.0, 90.5]
```

**Explanation:** `marks[1:]` is same as `marks[1:len(marks)]` - from index 1 to the end.

---

### Example 3: Slice from start to index 4

```python
marks = [94.2, 88.5, 76.5, 82.0, 91.3, 79.5, 85.0, 90.5]
print(marks[:4])
```

**Output:**

```
[94.2, 88.5, 76.5, 82.0]
```

**Explanation:** Elements from index 0 to 3 (4-1) are included.

---

### Example 4: Negative Indexing

```python
marks = [94.2, 88.5, 76.5, 82.0, 91.3, 79.5, 85.0, 90.5]
print(marks[-3:-1])
```

**Output:**

```
[79.5, 85.0]
```

**Explanation:**
- Index -3 is 79.5
- Index -1 is 90.5
- But end index is exclusive, so we get elements from -3 to -2

---

## List Methods

List methods are built-in functions to perform operations on lists.

### 1. append() - Add Element at End

```python
list = [10, 20, 30, 40, 50]
list.append(100)
print(list)
```

**Output:**

```
[10, 20, 30, 40, 50, 100]
```

**Explanation:** `append()` adds the element 100 at the end of the list.

---

### 2. sort() - Sort in Ascending Order

```python
list = [50, 10, 40, 20, 30]
list.sort()
print(list)
```

**Output:**

```
[10, 20, 30, 40, 50]
```

**Explanation:** `sort()` arranges elements from smallest to largest.

---

### 3. sort(reverse=True) - Sort in Descending Order

```python
list = [10, 20, 30, 40, 50]
list.sort(reverse=True)
print(list)
```

**Output:**

```
[50, 40, 30, 20, 10]
```

**Explanation:** Sorts from largest to smallest.

---

### 4. reverse() - Reverse the List

```python
list = [10, 20, 30, 40, 50]
list.reverse()
print(list)
```

**Output:**

```
[50, 40, 30, 20, 10]
```

**Important:** `reverse()` just reverses the current order. It is NOT the same as sorting in descending order.

**Example to show the difference:**

```python
list1 = [50, 10, 30, 20, 40]
list1.reverse()
print("Reversed:", list1)

list2 = [50, 10, 30, 20, 40]
list2.sort(reverse=True)
print("Sorted Descending:", list2)
```

**Output:**

```
Reversed: [40, 20, 30, 10, 50]
Sorted Descending: [50, 40, 30, 20, 10]
```

---

### 5. insert() - Insert Element at Specific Index

```python
list = [10, 20, 30, 40, 50]
list.insert(2, 73)
print(list)
```

**Output:**

```
[10, 20, 73, 30, 40, 50]
```

**Explanation:** `insert(2, 73)` inserts 73 at index 2. The existing elements shift to the right.

---

### 6. remove() - Remove Specific Element

```python
list = [10, 20, 30, 40, 50]
list.remove(30)
print(list)
```

**Output:**

```
[10, 20, 40, 50]
```

**Explanation:** `remove(30)` removes the first occurrence of 30 from the list.

---

### 7. pop() - Remove Element at Specific Index

```python
list = [10, 20, 73, 30, 40, 50]
list.pop(2)
print(list)
```

**Output:**

```
[10, 20, 30, 40, 50]
```

**Explanation:** `pop(2)` removes the element at index 2 (which is 73).

If no index is given, `pop()` removes the last element:

```python
list = [10, 20, 30, 40, 50]
list.pop()
print(list)
```

**Output:**

```
[10, 20, 30, 40]
```




---

# Tuples in Python

A tuple is a built-in data type that stores a set of values.

## Key Features of Tuples:

- Similar to lists
- **Tuples are immutable** (cannot be changed/modified)
- Created using parentheses `( )`
- Elements are ordered and can be accessed by index

---

## Creating Tuples

```python
tuple1 = (10, 20, 30, 40, 50)
print(tuple1)
print(tuple1[2])  # Accessing element at index 2
```

**Output:**

```
(10, 20, 30, 40, 50)
30
```
---

## Single Value Tuple - Important Note!

If we write only a single value in a tuple, we need to add a comma after that value. Otherwise, it will be considered as a normal variable, not a tuple.

### Correct Way - Single Value Tuple:

```python
tuple2 = (100,)  # Note the comma
print(type(tuple2))
```

**Output:**

```
<class 'tuple'>
```

---

### Wrong Way - Without Comma:

```python
tuple3 = (100)  # No comma - treated as integer
print(type(tuple3))
```

**Output:**

```
<class 'int'>
```

**Explanation:** Without the comma, Python treats (100) as just an integer with parentheses, not a tuple.

---

## Tuples are Immutable

```python
tuple1 = (10, 20, 30, 40, 50)
tuple1[2] = 100  # This will give an error
```

**Output:**

```
TypeError: 'tuple' object does not support item assignment
```

**Explanation:** Unlike lists, tuples cannot be modified after creation.

---

## Tuple Methods

### 1. index() - Find Index of Element

```python
tuple1 = (10, 20, 30, 40, 50, 20, 30)
print(tuple1.index(30))
print(tuple1.index(20))
```

**Output:**

```
2
1
```

**Explanation:**
- `index(30)` returns 2 (the first occurrence of 30 is at index 2)
- `index(20)` returns 1 (the first occurrence of 20 is at index 1)

### 2. count() - Count Occurrences of Element

```python
tuple1 = (10, 20, 30, 40, 50, 20, 30)
print(tuple1.count(20))
print(tuple1.count(30))
print(tuple1.count(10))
```

**Output:**

```
2
2
1
```

**Explanation:**
- 20 appears 2 times in the tuple
- 30 appears 2 times in the tuple
- 10 appears 1 time in the tuple

---

## Practice Questions

### Question 1: WAP to ask the user to enter names of their 3 favourite movies and store them in a list

```python
enter_movies = input("Enter your 1st favourite movie: ")
enter_movies2 = input("Enter your 2nd favourite movie: ")
enter_movies3 = input("Enter your 3rd favourite movie: ")

totalmovies = [enter_movies, enter_movies2, enter_movies3]
print("Your favourite movies are:", totalmovies)
print(type(totalmovies))
```

**If user enters:**
- 1st movie: Inception
- 2nd movie: Interstellar
- 3rd movie: The Dark Knight

**Output:**

```
Your favourite movies are: ['Inception', 'Interstellar', 'The Dark Knight']
<class 'list'>
```

---

### Question 2: WAP to check if a list contains a palindrome of elements

A palindrome list reads the same forwards and backwards (like [1, 2, 1]).

```python
list1 = [1, 2, 1]  # Palindrome
copy_list1 = list1.copy()
copy_list1.reverse()

if list1 == copy_list1:
    print("Palindrome")
else:
    print("Not a Palindrome")
```

**Output:**

```
Palindrome
```

**Testing with non-palindrome:**

```python
list1 = [1, 2, 3]  # Not palindrome
copy_list1 = list1.copy()
copy_list1.reverse()

if list1 == copy_list1:
    print("Palindrome")
else:
    print("Not a Palindrome")
```

**Output:**

```
Not a Palindrome
```

**Explanation:**
- We create a copy of the list
- Reverse the copy
- If original and reversed are the same, it's a palindrome
- [1, 2, 1] reversed is [1, 2, 1] → Palindrome ✓
- [1, 2, 3] reversed is [3, 2, 1] → Not a Palindrome ✗

---

### Question 3: WAP to count the number of students with grade 'A' from the given tuple

```python
tuple = ('c', 'd', 'a', 'c', 'b', 'a', 'a', 'a', 'b')
print(tuple.count('a'))
```

**Output:**

```
4
```

**Explanation:** The grade 'a' appears 4 times in the tuple.

---

### Question 4: Store the above values in a list and sort them from A to D

```python
list = ['c', 'd', 'a', 'c', 'b', 'a', 'a', 'a', 'b']
list.sort()
print(list)
```

**Output:**

```
['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'd']
```

**Explanation:** The `sort()` method arranges the grades in alphabetical order from A to D.

---

## Comparison: Lists vs Tuples

| Feature | Lists | Tuples |
|---------|-------|--------|
| Syntax | Square brackets `[]` | Parentheses `()` |
| Mutability | Mutable (can be changed) | Immutable (cannot be changed) |
| Methods | Many methods (append, remove, sort, etc.) | Few methods (index, count) |
| Speed | Slower | Faster |
| Use Case | When data needs to change | When data should remain constant |
| Example | `[1, 2, 3]` | `(1, 2, 3)` |

---

## When to Use Lists vs Tuples?

**Use Lists when:**
- You need to add, remove, or modify elements
- Data changes over time
- **Example:** Shopping cart items, student grades

**Use Tuples when:**
- Data should not change
- You want to protect data from accidental modification
- **Example:** Coordinates (x, y), RGB colors (255, 0, 0), dates

---

# Dictionary and Sets in Python

## What is a Dictionary?

A dictionary is used to store data in key-value pairs.

### Key Features of Dictionaries:

- **Unordered** - No index positions like lists or tuples
- **Changeable (Mutable)** - Values can be modified
- **No Duplicates** - Keys must be unique
- Created using curly braces `{ }` with key-value pairs

---

## Creating a Dictionary

```python
info = {
    "name": "John",
    "age": 30
}

print(info)
```

**Output:**

```
{'name': 'John', 'age': 30}
```

**Explanation:**
- "name" and "age" are keys
- "John" and 30 are values
- Keys can be strings, numbers, or tuples
- Values can be any data type

---

## Why Dictionaries are Unordered?

**Strings, lists, and tuples have index positions:**
- `list[0]`, `list[1]`, `list[2]` etc.

**Dictionaries don't have index positions:**
- You cannot access dictionary elements using index numbers
- You access them using keys instead

---

## Accessing Dictionary Values

To access a value, use the key inside square brackets.

```python
info = {
    "name": "John",
    "age": 30
}

print(info["name"])
print(info["age"])
```

**Output:**

```
John
30
```

**Explanation:** We use the key to get its corresponding value.

---

## Updating Dictionary Values

```python
info = {
    "name": "John",
    "age": 30
}

info["age"] = 31  # Updating existing value
print(info)
```

**Output:**

```
{'name': 'John', 'age': 31}
```

**Explanation:** The age is updated from 30 to 31.

---

## Adding New Key-Value Pairs

```python
info = {
    "name": "John",
    "age": 30
}

info["city"] = "New York"  # Adding new key-value pair
print(info)
```

**Output:**

```
{'name': 'John', 'age': 30, 'city': 'New York'}
```

**Explanation:** A new key "city" with value "New York" is added to the dictionary.

---

## Nested Dictionaries

A dictionary can contain another dictionary as a value. This is called a nested dictionary.

```python
student = {
    "name": "Alice",
    "age": 22,
    "courses": {
        "math": 90,
        "science": 85
    }
}

print(student)
```

**Output:**

```
{'name': 'Alice', 'age': 22, 'courses': {'math': 90, 'science': 85}}
```

---

## Accessing Nested Dictionary Values

```python
student = {
    "name": "Alice",
    "age": 22,
    "courses": {
        "math": 90,
        "science": 85
    }
}

print(student["courses"]["math"])
print(student["courses"]["science"])
```

**Output:**

```
90
85
```

**Explanation:**
- `student["courses"]` accesses the nested dictionary
- `["math"]` then accesses the math score from that nested dictionary

---

## Dictionary Methods

### 1. keys() - Get All Keys

```python
student = {
    "name": "Alice",
    "age": 22,
    "courses": {
        "math": 90,
        "science": 85
    }
}

print(student.keys())
```

**Output:**

```
dict_keys(['name', 'age', 'courses'])
```

**Explanation:** Returns all the keys in the dictionary.

---

### 2. values() - Get All Values

```python
student = {
    "name": "Alice",
    "age": 22,
    "courses": {
        "math": 90,
        "science": 85
    }
}

print(student.values())
```

**Output:**

```
dict_values(['Alice', 22, {'math': 90, 'science': 85}])
```

**Explanation:** Returns all the values in the dictionary.

---

### 3. items() - Get All Key-Value Pairs

```python
student = {
    "name": "Alice",
    "age": 22,
    "courses": {
        "math": 90,
        "science": 85
    }
}

print(student.items())
```

**Output:**

```
dict_items([('name', 'Alice'), ('age', 22), ('courses', {'math': 90, 'science': 85})])
```

**Explanation:** Returns all key-value pairs as tuples.

---

### 4. get() - Get Value for Specified Key

```python
student = {
    "name": "Alice",
    "age": 22
}

print(student.get("name"))
print(student.get("age"))
```

**Output:**

```
Alice
22
```

---

**Difference between get() and [ ]:**

```python
student = {
    "name": "Alice",
    "age": 22
}

print(student.get("city"))      # Returns None if key doesn't exist
print(student["city"])           # Throws KeyError if key doesn't exist
```

**Output:**

```
None
KeyError: 'city'
```

**Explanation:** `get()` is safer because it returns None instead of causing an error.

---

### 5. update() - Add or Update Key-Value Pairs

```python
student = {
    "name": "Alice",
    "age": 22,
    "courses": {
        "math": 90,
        "science": 85
    }
}

student.update({"College": "KJ"})
print(student)
```

**Output:**

```
{'name': 'Alice', 'age': 22, 'courses': {'math': 90, 'science': 85}, 'College': 'KJ'}
```

**Explanation:** `update()` adds the new key-value pair "College": "KJ" to the dictionary.

**Updating existing value:**

```python
student = {
    "name": "Alice",
    "age": 22
}

student.update({"age": 23})
print(student)
```

**Output:**

```
{'name': 'Alice', 'age': 23}
```

---

# Sets in Python

A set is a collection of unordered items. Every element in a set is:
- **Unique** (no duplicates allowed)
- **Immutable** (set elements themselves cannot be changed)

## Key Features of Sets:

- Created using curly braces `{ }`
- Unordered (no index positions)
- No duplicate values
- Useful for removing duplicates and mathematical operations
---

## Creating a Set

```python
nums = {1, 2, 3, 4, 5}
print(nums)
```

**Output:**

```
{1, 2, 3, 4, 5}
```

---

## Sets Automatically Remove Duplicates

```python
num = {1, 2, 2, 3, 4, 4, 5}
print(num)
```

**Output:**

```
{1, 2, 3, 4, 5}
```

**Explanation:** Duplicate values (2, 2 and 4, 4) are automatically removed. Each element appears only once.

---

## Creating an Empty Set

**Important Note:** You cannot use `{}` to create an empty set!

```python
collection = {}
print(type(collection))
```

**Output:**

```
<class 'dict'>
```

**Explanation:** `{}` creates an empty dictionary, not a set!

**Correct way to create an empty set:**

```python
collection = set()
print(type(collection))
```

**Output:**

```
<class 'set'>
```

---

## Set Methods

**Sets are Mutable:**
- We can add or remove elements from a set
- But set elements themselves are immutable (cannot be lists or dictionaries)

### 1. add() - Add Element to Set

```python
num = {1, 2, 3, 4, 5}
num.add(6)
print(num)
```

**Output:**

```
{1, 2, 3, 4, 5, 6}
```

**Explanation:** Element 6 is added to the set.

---

### 2. remove() - Remove Specific Element

```python
num = {1, 2, 3, 4, 5}
num.remove(3)
print(num)
```

**Output:**

```
{1, 2, 4, 5}
```

**Explanation:** Element 3 is removed from the set.

**Note:** If you try to remove an element that doesn't exist, it will throw an error:

```python
num = {1, 2, 3, 4, 5}
num.remove(10)  # This will give KeyError
```

---

### 3. clear() - Remove All Elements

```python
num = {1, 2, 3, 4, 5}
num.clear()
print(num)
```

**Output:**

```
set()
```

**Explanation:** All elements are removed, leaving an empty set.

---

### 4. pop() - Remove a Random Element

```python
num = {1, 2, 3, 4, 5}
removed_element = num.pop()
print("Removed element:", removed_element)
print("Remaining set:", num)
```

**Output (may vary):**

```
Removed element: 1
Remaining set: {2, 3, 4, 5}
```

**Explanation:** `pop()` removes and returns a random element. Since sets are unordered, you don't know which element will be removed.

---

### 5. len() - Get Number of Elements

```python
num = {1, 2, 3, 4, 5}
print(len(num))
```

**Output:**

```
5
```
---

## Set Operations

### Union - Combine Two Sets

Union combines all elements from both sets (removing duplicates).

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 2, 9, 7, 8}

print(set1.union(set2))
```

**Output:**

```
{1, 2, 3, 4, 5, 7, 8, 9}
```

**Explanation:** All unique elements from both sets are combined. Duplicates (2 and 4) appear only once.

**Visual representation:**

```
set1: {1, 2, 3, 4, 5}
set2: {4, 2, 9, 7, 8}
Union: {1, 2, 3, 4, 5, 7, 8, 9}
```

---

### Intersection - Common Elements

Intersection returns only the elements that are present in both sets.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 2, 9, 7, 8}

print(set1.intersection(set2))
```

**Output:**

```
{2, 4}
```

**Explanation:** Only 2 and 4 are present in both sets.

**Visual representation:**

```
set1: {1, 2, 3, 4, 5}
set2: {4, 2, 9, 7, 8}
Intersection: {2, 4}
```

---

## Practice Questions

### Question 1: Store word meanings in Python dictionary

```python
info = {
    "table": ["A piece of furniture", "list of facts and figures"],
    "cat": "a small animal"
}

print(info)
print(type(info))
```

**Output:**

```
{'table': ['A piece of furniture', 'list of facts and figures'], 'cat': 'a small animal'}
<class 'dict'>
```

**Explanation:**
- The key "table" has multiple meanings stored in a list
- The key "cat" has a single meaning as a string

**Accessing the meanings:**

```python
print(info["table"])
print(info["table"][0])  # First meaning
print(info["cat"])
```

**Output:**

```
['A piece of furniture', 'list of facts and figures']
A piece of furniture
a small animal
```

---

### Question 2: How many classrooms are needed by all students?

**Problem:** You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students?

```python
subjects = ["Math", "Science", "English", "History", "Geography", "Math", "Science"]

count = len(set(subjects))
print("Number of classrooms needed:", count)
```

**Output:**

```
Number of classrooms needed: 5
```

**Explanation:**
- Original list has 7 subjects with duplicates
- Converting to set removes duplicates: {"Math", "Science", "English", "History", "Geography"}
- Only 5 unique subjects exist
- Therefore, only 5 classrooms are needed

**Step-by-step breakdown:**

```python
subjects = ["Math", "Science", "English", "History", "Geography", "Math", "Science"]

print("Original list:", subjects)
print("Length of list:", len(subjects))

unique_subjects = set(subjects)
print("Unique subjects:", unique_subjects)
print("Number of unique subjects:", len(unique_subjects))
```

**Output:**

```
Original list: ['Math', 'Science', 'English', 'History', 'Geography', 'Math', 'Science']
Length of list: 7
Unique subjects: {'Geography', 'History', 'English', 'Math', 'Science'}
Number of unique subjects: 5
---

## Comparison: Dictionary vs Set

| Feature | Dictionary | Set |
|---------|-----------|-----|
| Syntax | `{"key": "value"}` | `{1, 2, 3}` |
| Structure | Key-value pairs | Only values |
| Duplicates | Keys must be unique | No duplicates allowed |
| Ordering | Unordered | Unordered |
| Accessing | Using keys | Cannot access individual elements |
| Use Case | Store related data | Remove duplicates, mathematical operations |

---

## When to Use Dictionary vs Set?

**Use Dictionary when:**
- You need to store related information (key-value pairs)
- You need to quickly look up values using keys
- **Example:** Student records, word meanings, configuration settings

**Use Set when:**
- You need to remove duplicates from a list
- You need to perform mathematical operations (union, intersection)
- You want to check if an element exists (very fast)
- **Example:** Unique tags, unique visitors, finding common elements

---

# Modules and File Handling in Python

## What are Modules?

A module is a file containing Python definitions and statements.

### Key Points about Modules:

- Modules use the `.py` extension
- They promote code reusability
- Can be imported and used in other Python programs
- Help organize code into logical units

---

## Creating and Using Modules

### How to Create a Module:

When you save any code using the `.py` extension, it becomes a module that can be used in other Python programs.

**Example: Creating a calculator module**

Save this code as `calculator.py`:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
```

---

### How to Import and Use a Module:

In your main program file:

```python
import calculator

result1 = calculator.add(10, 5)
result2 = calculator.multiply(4, 3)

print("Addition:", result1)
print("Multiplication:", result2)
```

**Output:**

```
Addition: 15
Multiplication: 12
```

**Explanation:** The calculator module is imported, and we can use its functions using `calculator.function_name()`.

---

## File I/O in Python

File I/O (Input/Output) allows Python to perform operations on files such as:
- Create a file
- Read data from a file
---

## Types of Files

### 1. Text Files
- Human-readable files
- **Examples:** `.txt`, `.docx`, `.log`, `.csv`, `.py`

### 2. Binary Files (Non-text files)
- Not human-readable, contain binary data
- **Examples:** `.bin`, `.dat`, `.mp4`, `.mov`, `.jpeg`, `.png`

---

## File Operations

### Opening, Reading, and Closing Files

**Basic syntax:**

```python
f = open("filename", "mode")
data = f.read()
f.close()
```

**File Modes:**
- **r** - Read mode (default)
- **w** - Write mode (overwrites existing content)
- **a** - Append mode (adds to existing content)
- **r+** - Read and write
- **w+** - Write and read
- **a+** - Append and read

---

## Reading from a File

### Example 1: Reading Entire File

First, create a file named `demo.txt` with this content:

```
Hello World!
This is my first file.
I am learning Python.
Python is awesome!
```

**Code:**

```python
f = open("demo.txt", "r")  # Open file in read mode
data = f.read()             # Read entire file
print(data)
print(type(data))
f.close()                   # Close file
```

**Output:**

```
Hello World!
This is my first file.
I am learning Python.
Python is awesome!
<class 'str'>
```

**Explanation:**
- `open("demo.txt", "r")` opens the file in read mode
- `f.read()` reads the entire file content as a string
- `f.close()` closes the file

---

### Example 2: Reading Line by Line

```python
f = open("demo.txt", "r")

line1 = f.readline()   # Reads only one line
print(line1)

line2 = f.readline()   # Reads next line
print(line2)

print(type(line1))

f.close()
```

**Output:**

```
Hello World!

This is my first file.

<class 'str'>
```

**Explanation:** `readline()` reads one line at a time. Each call moves to the next line.

---

## Writing to a File

### Using Write Mode (w)

**Important:** Write mode overwrites the existing content completely!

```python
f = open("demo.txt", "w")

f.write("This is first line written using python file handling")

f.close()
```

**After running this code, demo.txt will contain:**

```
This is first line written using python file handling
```

**Explanation:** The previous content is completely replaced with the new content.

---

## Appending to a File

### Using Append Mode (a)

Append mode adds new content to the existing content without deleting anything.

```python
f = open("demo.txt", "a")

f.write("\nI am learning python file handling")

f.close()
```

**Now demo.txt will contain:**

```
This is first line written using python file handling
I am learning python file handling
```

**Explanation:** `\n` adds a new line, and the text is appended to the end.

---

## Understanding Different File Modes

### Comparison of r+, w+, and a+

| Mode | Description | Pointer Position | Truncate? |
|------|-------------|------------------|-------------|
| r+ | Read and Write | Beginning | No - keeps existing content |
| w+ | Write and Read | Beginning | Yes - deletes all content |
| a+ | Append and Read | End | No - keeps existing content |

---

### Examples:

**r+ Mode:**

```python
f = open("demo.txt", "r+")
f.write("NEW TEXT")  # Overwrites from the beginning
f.close()
```

**If demo.txt had:** `Hello World!`  
**After r+:** `NEW TEXTrld!`

**Explanation:** It overwrites from the beginning but doesn't delete the rest.

---

**w+ Mode:**

```python
f = open("demo.txt", "w+")
f.write("NEW TEXT")
f.close()
```

**If demo.txt had:** `Hello World!`  
**After w+:** `NEW TEXT`

**Explanation:** Everything is deleted, then new text is written.

---

**a+ Mode:**

```python
f = open("demo.txt", "a+")
f.write("\nNEW TEXT")
f.close()
```

**If demo.txt had:** `Hello World!`  
**After a+:**

```
Hello World!
NEW TEXT
```

**Explanation:** New text is added at the end without deleting anything.

---

## Using "with" Statement

The `with` statement is the recommended way to work with files because:
- It automatically closes the file after the code block
- No need to call `f.close()`
- Safer and cleaner code

### Reading with "with":

```python
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
# File is automatically closed here
```

**Output:**

```
Hello World!
This is my first file.
I am learning Python.
```

---

### Writing with "with":

```python
with open("demo.txt", "w") as f:
    f.write("This is me sushant")
# File is automatically closed here
```

**Explanation:** The file is automatically closed when the with block ends, even if an error occurs.

---

## Deleting a File

To delete a file, we use the `os` module.

```python
import os
os.remove("emptyfile.py")  # Deletes the file named emptyfile.py
```

**Output:** The file `emptyfile.py` will be deleted from the directory.

**Note:** If the file doesn't exist, this will throw an error.

### Safe way to delete:

```python
import os

if os.path.exists("emptyfile.py"):
    os.remove("emptyfile.py")
    print("File deleted successfully")
else:
    print("File does not exist")
```

---

## Installing External Modules

To install external modules (like pandas, numpy, etc.), use pip:

```bash
pip install module_name
```

**Example:**

```bash
pip install pandas
pip install numpy
```

**Note:** The `os` module is built-in, so you don't need to install it.

---

## Practice Questions

### Question 1: Create a new file "practice.txt" and add data

```python
with open("practice.txt", "w") as f:
    f.write("Hello World!\n")
    f.write("This is my first file handling practice.\n")
    f.write("I am learning python programming.\n")
    f.write("File handling is very important in programming.\n")
    f.write("Thank you!")
```

**After running, practice.txt will contain:**

```
Hello World!
This is my first file handling practice.
I am learning python programming.
File handling is very important in programming.
Thank you!
```

**Explanation:** The file is created (if it doesn't exist) and all lines are written to it.

---

### Question 2: Replace all occurrences of "Handling" with "python"

```python
# Step 1: Read the file
with open("practice.txt", "r") as f:
    data = f.read()

# Step 2: Replace the word
new_data = data.replace("Handling", "python")
print(new_data)

# Step 3: Write back to the file
with open("practice.txt", "w") as f:
    f.write(new_data)
```

**Original content:**

```
Hello World!
This is my first file Handling practice.
I am learning python programming.
File Handling is very important in programming.
Thank you!
```

**After replacement:**

```
Hello World!
This is my first file python practice.
I am learning python programming.
File python is very important in programming.
Thank you!
```

**Explanation:**
- Read the entire file content
- Use `replace()` to change "Handling" to "python"
- Write the modified content back to the file

---

### Question 3: Find which line the word "Hello" occurs first

```python
def check_for_lines():
    word = "Hello"
    data = True
    line_no = 1
    
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print("Word found at line:", line_no)
                return line_no
            line_no += 1
    
    return -1

check_for_lines()
```

**Output:**

```
Word found at line: 1
```

**Explanation:**
- The function reads the file line by line
- Checks if the word "Hello" is in each line
- Returns the line number when found
- If word is not found, returns -1

**Step-by-step breakdown:**
- Line 1: "Hello World!" - Contains "Hello" ✓ → Stop and return 1

---

### Question 4: Count even numbers from a file

First, create a file `numbers.txt` with this content:

```
1,2,3,4,5,6,7,8,9,10
```

```python
count = 0

with open("numbers.txt", "r") as f:
    data = f.read()
    
    nums = data.split(",")  # Split by comma
    
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print("Count of even numbers:", count)
```

**Output:**

```
Count of even numbers: 5
```

**Explanation:**
- Read the file content: `"1,2,3,4,5,6,7,8,9,10"`
- Split by comma: `['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']`
- Convert each to integer and check if even
- Even numbers: 2, 4, 6, 8, 10 → Count = 5

**Detailed breakdown:**

```
Numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Checking each:
1 % 2 = 1 (odd)
2 % 2 = 0 (even) ✓ count = 1
3 % 2 = 1 (odd)
4 % 2 = 0 (even) ✓ count = 2
5 % 2 = 1 (odd)
6 % 2 = 0 (even) ✓ count = 3
7 % 2 = 1 (odd)
8 % 2 = 0 (even) ✓ count = 4
9 % 2 = 1 (odd)
10 % 2 = 0 (even) ✓ count = 5

Final count: 5
```

---

## Common File Operations - Complete Examples

### Example 1: Creating a Log File

```python
import datetime

with open("log.txt", "a") as f:
    current_time = datetime.datetime.now()
    f.write(f"\n[{current_time}] User logged in")
```

**log.txt will contain:**

```
[2026-01-08 14:30:25.123456] User logged in
```
---

### Example 2: Reading and Processing Data

```python
# Reading student marks and calculating average
with open("marks.txt", "r") as f:
    marks = f.read().split(",")
    marks = [int(m) for m in marks]
    
    average = sum(marks) / len(marks)
    print(f"Average marks: {average}")
```

**If marks.txt contains:** `85,90,78,92,88`

**Output:**

```
Average marks: 86.6
```

---

### Example 3: Copying File Content

```python
# Copy content from one file to another
with open("source.txt", "r") as source:
    content = source.read()

with open("destination.txt", "w") as dest:
    dest.write(content)

print("File copied successfully!")
```

---

## Best Practices for File Handling

1. **Always use "with" statement** - It automatically closes files
2. **Check if file exists** before deleting or reading
3. **Handle exceptions** to avoid program crashes
4. **Close files** if not using "with" statement
5. **Use appropriate mode** (r, w, a) based on your needs

### Example with error handling:

```python
try:
    with open("demo.txt", "r") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("File does not exist!")
except Exception as e:
    print(f"An error occurred: {e}")
```

---

## Summary

In this section, we learned:

### Modules
- Files containing Python code that can be reused
- Created by saving code with `.py` extension
- Imported using `import module_name`

### File Types:
- **Text files** (readable)
- **Binary files** (non-readable)

### File Modes:
- **r** - Read
- **w** - Write (overwrites)
- **a** - Append
- **r+, w+, a+** - Read and write combinations

### File Operations:
- `open()` - Open a file
- `read()` - Read entire file
- `readline()` - Read one line
- `write()` - Write to file
- `close()` - Close file

### Key Concepts:
- **with Statement** - Automatically handles file closing
- **OS Module** - Used for file deletion and other system operations

### Practice Applications:
- Creating and writing files
- Finding and replacing text
- Searching for words in files
- Processing data from files

**File handling is essential for storing and retrieving data permanently in Python programs!** 🚀

---

