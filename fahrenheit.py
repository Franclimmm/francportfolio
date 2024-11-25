#!/usr/bin/env python3
if __name__ == '__main__':
    celsius_temperature = (float(input("Enter temperature in Celsius: ")))
    fahrenheit_temperature = (celsius_temperature * 9 / 5) + 32
    print(f"{celsius_temperature}C is equal to {fahrenheit_temperature:.1f}F.")
