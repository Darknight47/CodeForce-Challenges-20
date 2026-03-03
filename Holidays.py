"""

--------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/670/A --------------------------------

On the planet Mars a year lasts exactly n days (there are no leap years on Mars). But Martians have the same weeks as earthlings — 5 work days and then 2 days off. 
Your task is to determine the minimum possible and the maximum possible number of days off per year on Mars.

Input
The first line of the input contains a positive integer n (1 ≤ n ≤ 1 000 000) — the number of days in a year on Mars.

Output
Print two integers — the minimum possible and the maximum possible number of days off per year on Mars.


Input:
14

Output:
4 4
"""
n = int(input())
weeks = n // 7
rest = n % 7
min_holidays = weeks * 2
max_holidays = weeks * 2 
if(rest <= 2):
    max_holidays += rest
else:
    max_holidays += 2
    if(rest == 6):
        min_holidays += 1
print(min_holidays, max_holidays)