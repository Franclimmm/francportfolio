#!/usr/bin/env python3

if __name__ == '__main__':
    username = input("Enter username to delete: ")
    file_path = "passwd2.txt"
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            if username not in file_contents:
                print(f"User '{username}' not found, nothing was changed.")
            else:
                with open(file_path, 'w') as file:
                    file.write(username)
                    print("Username has been deleted.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
