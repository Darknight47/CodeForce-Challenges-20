"""


----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1705/B ------------------------------------------------

Mark is cleaning a row of n rooms. The i-th room has a nonnegative dust level ai. 
He has a magical cleaning machine that can do the following three-step operation.

Select two indices i<j such that the dust levels ai, ai+1, …, aj−1 are all strictly greater than 0.
Set ai to ai−1.
Set aj to aj+1.
Mark's goal is to make a1=a2=…=an−1=0 so that he can nicely sweep the n-th room. Determine the minimum number of operations needed to reach his goal.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains a single integer n (2 ≤ n ≤ 2⋅10^5) — the number of rooms.

The second line of each test case contains n integers a1, a2, ..., an (0 ≤ ai ≤ 10^9) — the dust level of each room.

It is guaranteed that the sum of n across all test cases does not exceed 2⋅10^5.

Output
For each test case, print a line containing a single integer — the minimum number of operations. It can be proven that there is a sequence of operations that meets the goal.

Input:
4
3
2 0 0
5
0 2 0 2 0
6
2 0 3 0 4 6
4
0 0 0 10

Output:
3
5
11
0
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    seen = False
    ops = 0
    zeros = 0
    for i in range(sze - 1):
        temp = arr[i]
        if(temp != 0):
            seen = True
        if(seen and temp == 0):
            zeros += 1
        elif(seen and temp != 0):
            ops += temp
    print(ops + zeros)