#!/usr/bin/env python3

if __name__ == '__main__':
    import sys
    from statistics import mean
    cat_visits = 0
    intruder_cats = 0
    total_time_in_house = 0
    visit_lengths = []
    hours = 1
    minutes = 60
    file_path = "cat_shelter_1.txt"
    file_path = "cat_shelter_2.txt"
    file_path = "cat_shelter_3.txt"
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            if cat_visits > 0:
                average_visit_length = mean(visit_lengths)
                longest_visit = max(visit_lengths)
                shortest_visit = min(visit_lengths)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

    print("=================")
    logfile = "Log File Analysis"
    x = logfile.title()
    print(logfile)
    print("=================")
    print()

    print(f'Correct Cat Visits: {cat_visits}')
    print(f'Intruding Cats: {intruder_cats}')
    print(f'Total Time in House by Correct Cat: {total_time_in_house}')
    print(f'Average Visit Length: {average_visit_length}')
    print(f'Longest Visit: {longest_visit}')
    print(f'Shortest Visit: {shortest_visit}')