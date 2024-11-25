#!/usr/bin/env python3
from statistics import mean


def chomp(s):
    return s[:-1]


def c2f(c):
    return c * (9 / 5) + 32


def f2c(f):
    return (f - 32) * 5 / 9


if __name__ == '__main__':
    temps = []
    for _ in range(3):
        temp = float(chomp(input('Enter temperature in celsius (e.g. 11C): ')))
        temps.append(temp)

    print(f'Max temp: {max(temps)}C, or {c2f(max(temps)):.1f}F')
    print(f'Min temp: {min(temps)}C, or {c2f(min(temps)):.1f}F')
    print(f'Mean temp: {mean(temps)}C, or {c2f(mean(temps)):.1f}F')
