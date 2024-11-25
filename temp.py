#!/usr/bin/env python3
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


if __name__ == "__main__":
    celsius_temp = float(input("Enter temperature in Celsius: "))
    print(f"{celsius_temp}C is equivalent to {celsius_to_fahrenheit(celsius_temp):.1f}F")
    fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit_temp}F is equivalent to {fahrenheit_to_celsius(fahrenheit_temp):.1f}C")
