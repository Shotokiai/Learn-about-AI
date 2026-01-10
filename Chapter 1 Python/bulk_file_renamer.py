# Question - Bulk File Renamer Simulator
#Task: Given a list of filenames, rename them by adding a prefix and sequential numbers.

def rename_files(filesnames, prefix):
    """Add prefix and number to rach filename"""
    renamed_files = []

    for index, filename in enumerate(filenames, start=1):
        #split filename and extension
        if "." in filename:
            name,extension = filename.rsplit(".",1) #.rsplit(".", 1) splits from right, only once
        else:
            name = filename
            extension = ""

        #Create new name
        if extension:
            new_name = f"{prefix}_{index:03d}_{name}.{extension}"
            
            '''
            f-string: Format string with variables
            {index:03d} means:
                index - the variable
                :03d - format as 3-digit number with leading zeros
                Example: 1 → 001, 42 → 042
            '''
        else:
            new_name = f"{prefix}_{index:03d}_{name}"

        renamed_files.append(new_name)

    return renamed_files

#Get filenames from user
print("Enter filesname (type'done' when finished):")
filenames = []
while True:
    filename = input("Filesname: ")
    if filename.lower() == "done":
        break
    filenames.append(filename)

#Get Prefix
prefix = input("Enter Prefix for files: ")

#Rename files
new_filenames = rename_files(filenames,prefix)

#Display results
print("\n=== RENAMED FILES ===")
for old,new in zip(filenames,new_filenames):
    print(f"{old:10s} -> {new}")

    '''
    - **Output:** Display old and new names
    - `{old:30s}` - left-align in 30 character space

    '''
