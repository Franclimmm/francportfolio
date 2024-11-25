#!/usr/bin/env python3
def greetings():
    name = input("Enter your name: ")
    formatted_name = name.capitalize()
    print(f"Hello, {formatted_name}!")


if __name__ == '__main__':
    greetings()
