file_path = input("Enter the file location: ")

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("File content:\n")
        print(content)
except FileNotFoundError:
    print("File not found. Please check the path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")