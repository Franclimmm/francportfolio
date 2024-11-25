#!/usr/bin/env python3
if __name__ == '__main__':
    password1 = input("Enter a new password (8-12 characters): ")
    password2 = input("Enter the password again: ")
    if password1 == password2 and 8 <= len(password1) <= 12:
        print("Password Set")
    else:
        print("Error: Password does not meet length requirements or passwords do not match.")
