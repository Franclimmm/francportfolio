#!/usr/bin/env python3
if __name__ == '__main__':
    num_sweets = int(input("How many sweets? "))
    num_pupils = int(input("How many pupils? "))
    sweets_per_pupil = num_sweets // num_pupils
    remaining_sweets = num_sweets % num_pupils
    print(f"The teacher should give each pupil {sweets_per_pupil} sweets, with {remaining_sweets} sweets left over.")
