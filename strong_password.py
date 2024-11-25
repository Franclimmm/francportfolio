#!/usr/bin/env python3
if __name__ == '__main__':
    while True:
        BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
        password1 = input("Enter a new password (8-12 characters): ")
        password2 = input("Enter the password again: ")
        if password1 == password2 and 8 <= len(password1) <= 12 not in BAD_PASSWORDS:
            print("Password Set")
            break
        else:
            print("Error: Password does not meet requirements. Please try again.")
