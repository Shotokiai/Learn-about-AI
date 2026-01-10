'''
Question: CSV Data Filter
Task: Read a CSV-like input and filter rows based on a condition.
Concepts Covered: Lists, Dictionaries, Loops, Conditionals, Functions, Input/Output

'''

def parse_csv_line(line):
    """Convert CSV line to list of values"""
    return[item.strip() for item in line.split(',')]

"""
Function 1: parse_csv_line()

    Function: Convert CSV string to list
    List comprehension: Create list in one line
    .split(',') - split by commas
    .strip() - remove extra spaces
    Example: "John, 25, 50000" → ["John", "25", "50000"]
"""

def filter_data(data,column_index, min_value):
    """Filter rows where colums value is >= min value"""
    filtered =[] #Store matching rows

    """
    Function: filter_data()
    Function: Filter rows based on criteria
    Parameters:
        data - list of rows
        column_index - which column to check
        min_value - minimum value to keep
    """

    for row in data:
        try:
            value = float(row[column_index]) #try block: Attempt operation that might fail || float(): Convert string to number || row[column_index] - get specific column value
            if value >= min_value:
                filtered.append(row)
        except (ValueError, IndexError):
            #except block: Handle errors || ValueError - if can't convert to number || IndexError - if column doesn't exist || continue: Skip to next iteration
            continue

    return filtered


#sample data (simulating CSV)
print("Enter CSV data(format:Name, Age, Salary)")
print("Type 'done' when finished")
print()

data = []
headers = None

while True: 
    line = input("Row: ") #Collect rows until user types "done"
    if line.lower() == 'done':
        break

    row = parse_csv_line(line)

    if headers is None:
        headers = row #first row is headers
    else:
        data.append(row)

#Display headers with indices
print("\n=== COLUMNS ===")
for i, header in enumerate(headers):
    print(f"{i}: {header}")


#Get filter criteria
try:
    column = int(input("\Which column you want to filter: "))
    min_value = float(input("Enter minimum value: "))

    #Filter data
    filtered_data = filter_data(data,column, min_value)

    #Display Results
    print(f"\n== FILTERED RESULTS(>= {min_value}) ===")
    print(",".join(headers))
    print("-"*40)

    for row in filtered_data:
        print(",".join(row))

    print(f"\nTotal rows: {len(filtered_data)}")


except ValueError:
    print("Error:Please enter valid numbers")

except IndexError:
    print("Error: Invalid column index")

