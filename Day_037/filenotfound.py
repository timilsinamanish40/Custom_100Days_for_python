try:
    # Trying to open a file that may not exist
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
        print(content)

# Handling the FileNotFoundError exception
except FileNotFoundError:
    print("Error: The file was not found. Please check the file path or name.")
