#!/usr/bin/env python3
if __name__ == '__main__':
    password1 = input("Enter a new password: ")
    password2 = input("Enter the password again: ")
    if password1 == password2:
        print("Password Set")
    else:
        print("Error: Passwords do not match.")
