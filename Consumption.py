"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/10/A ---------------------------------------------

Tom is interested in power consumption of his favourite laptop. His laptop has three modes. In normal mode laptop consumes P1 watt per minute. 
T1 minutes after Tom moved the mouse or touched the keyboard for the last time, a screensaver starts and power consumption changes to P2 watt per minute. 
Finally, after T2 minutes from the start of the screensaver, laptop switches to the "sleep" mode and consumes P3 watt per minute. 
If Tom moves the mouse or touches the keyboard when the laptop is in the second or in the third mode, it switches to the first (normal) mode. 
Tom's work with the laptop can be divided into n time periods [l1, r1], [l2, r2], ..., [ln, rn]. During each interval Tom continuously moves the mouse and presses buttons on the keyboard. 
Between the periods Tom stays away from the laptop. Find out the total amount of power consumed by the laptop during the period [l1, rn].

Input
The first line contains 6 integer numbers n, P1, P2, P3, T1, T2 (1 ≤ n ≤ 100, 0 ≤ P1, P2, P3 ≤ 100, 1 ≤ T1, T2 ≤ 60). The following n lines contain description of Tom's work. 
Each i-th of these lines contains two space-separated integers li and ri (0 ≤ li < ri ≤ 1440, ri < li + 1 for i < n), which stand for the start and the end of the i-th period of work.

Output
Output the answer to the problem.

Input:
1 3 2 1 5 10
0 10

Output:
30
"""
n, p1, p2, p3, t1, t2 = map(int, input().split())
total = 0
prev_r = -1

for i in range(n):
    l, r = map(int, input().split())
    diff = r - l
    off_time_consumption = 0

    if prev_r != -1:
        idle = l - prev_r

        # Mode 1: first t1 minutes at P1
        t = min(idle, t1)
        off_time_consumption += t * p1
        idle -= t

        # Mode 2: next t2 minutes at P2
        t = min(idle, t2)
        off_time_consumption += t * p2
        idle -= t

        # Mode 3: remaining time at P3
        off_time_consumption += idle * p3

    total += diff * p1 + off_time_consumption
    prev_r = r

print(total)