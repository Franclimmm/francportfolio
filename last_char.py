#!/usr/bin/env python3
def last_char(input_str):
    return input_str[:-1]


if __name__ == "__main__":
    string = input("Enter a string: ")
    result = last_char(string)
    print(f"{string} --> {result}")
