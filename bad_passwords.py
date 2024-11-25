#!/usr/bin/env python3
if __name__ == '__main__':
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    password1 = input("Enter a new password (8-12 characters): ")
    password2 = input("Enter the password again: ")
    if 8 <= len(password1) <= 12 and password1 == password2 and password1 not in BAD_PASSWORDS:
        print("Password Set")
    else:
        print("Error: Password does not meet length requirements, passwords do not match, or it is a common password.")
