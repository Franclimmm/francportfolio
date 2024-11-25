#!/usr/bin/env python3
if __name__ == '__main__':
    x = int(input("Enter a number between 0 to 12: "))
    if 0 <= x <= 12:
        result = x * 7
        print(f"{x} x 7 = {result}")
    else:
        print("Number must be between 0 and 12.")
