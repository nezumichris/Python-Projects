##file_path = input("Enter the file location: ")
file_path = r"C:\Git\SQL test Imports\Test1Basic.txt"
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("File content:\n")
        print(content)
except FileNotFoundError:
   print("File not found. Please check the path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")

# This is a simple file reader that prompts the user for a file path and displays its content.
# It includes basic error handling for file not found and other exceptions.


import re

pattern = r'\b(?:from|join)\b\s+([a-zA-Z0-9_\.\[\]]+)'
matches = re.findall(pattern, content, re.IGNORECASE)

if matches:
    print("\nText after 'from' or 'join':")
    for match in matches:
        # Strip any trailing ')' and ignore alias by taking only the first word
        cleaned = match.rstrip(')')
        print(cleaned)
else:
    print("\nNo 'from' or 'join' keywords found.")
