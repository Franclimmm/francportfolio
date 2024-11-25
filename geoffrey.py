#!/usr/bin/env python3
if __name__ == '__main__':
    matches_played = 609
    times_batted = 1014
    not_out = 162
    runs_scored = 48426
    completed_innings = times_batted - not_out
    batting_average = runs_scored / completed_innings
    print(f"Geoffrey Boycott's batting average is: {batting_average:.2f}")
