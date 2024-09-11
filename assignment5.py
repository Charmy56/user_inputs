# file_handling_assignment.py

def create_file():
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Hello, this is my first line.\n")
            file.write("Here is a number: 42\n")
            file.write("This is the third line of text.\n")
        print("File created and written successfully.")
    except (PermissionError, OSError) as e:
        print(f"Error creating file: {e}")
    finally:
        print("Create file operation completed.")

def read_file():
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except (PermissionError, OSError) as e:
        print(f"Error reading file: {e}")
    finally:
        print("Read file operation completed.")

def append_to_file():
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending a new line.\n")
            file.write("Another line with a number: 100\n")
            file.write("Final line of the file.\n")
        print("File appended successfully.")
    except (PermissionError, OSError) as e:
        print(f"Error appending to file: {e}")
    finally:
        print("Append file operation completed.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  