#!/usr/bin/env python3
if __name__ == '__main__':
    students = [113, 175, 12]
    lab_group_size = 24
    for num_students in students:
        full_groups = num_students // lab_group_size
        remaining_students = num_students % lab_group_size
        print(f"For {num_students} students {full_groups} full groups are needed, and there will be {remaining_students} students left over.")
