def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("First line\n")
            file.write("Second line\n")
            file.write("12345\n")
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("File created successfully.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to open the file.")
    except Exception as e:
        print("An error occurred:", e)

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Third line\n")
            file.write("Fourth line\n")
            file.write("67890\n")
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("Content appended successfully.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
