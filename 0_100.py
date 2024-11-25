#!/usr/bin/env python3
def valid_number(number):
    if 0 <= number <= 100:
        return True
    else:
        return False


test_number = int(input("Enter a number: "))
print(valid_number(test_number))
