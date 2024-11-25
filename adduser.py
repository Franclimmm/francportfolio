#!/usr/bin/env python3

if __name__ == '__main__':
    username = input("Enter username: ")
    name = input("Enter name: ")
    password = input("Enter password: ")
    file_path = "passwd.txt"
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            if username in file_contents:
                print(f"Username {username} already exists. Please choose a different username.")
            else:
                with open(file_path, 'a') as file:
                    file.write(f"{username}\n")
                    print(f"User '{username}' created successfully.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
