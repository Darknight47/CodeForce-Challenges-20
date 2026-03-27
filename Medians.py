"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1440/B -------------------------------

A median of an array of integers of length n is the number standing on the ⌈n2⌉ (rounding up) position in the non-decreasing ordering of its elements. 
Positions are numbered starting with 1. 
For example, a median of the array [2,6,4,1,3,5] is equal to 3. 
There exist some other definitions of the median, but in this problem, we will use the described one.

Given two integers n and k and non-decreasing array of nk integers. Divide all numbers into k arrays of size n, such that each number belongs to exactly one array.

You want the sum of medians of all k arrays to be the maximum possible. Find this maximum possible sum.

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases. The next 2t lines contain descriptions of test cases.

The first line of the description of each test case contains two integers n, k (1 ≤ n, k ≤ 1000).

The second line of the description of each test case contains nk integers a1,a2,…,ank (0 ≤ ai ≤ 10^9) — given array. 
It is guaranteed that the array is non-decreasing: a1≤a2≤…≤ank.

It is guaranteed that the sum of nk for all test cases does not exceed 2⋅10^5.

Output
For each test case print a single integer — the maximum possible sum of medians of all k arrays.

Input:
6
2 4
0 24 34 58 62 64 69 78
2 2
27 61 81 91
4 3
2 4 16 18 21 27 36 53 82 91 92 95
3 4
3 11 12 22 33 35 38 67 69 71 94 99
2 1
11 41
3 3
1 1 1 1 1 1 1 1 1

Output:
165
108
145
234
11
3
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    m = (n + 1) // 2
    step = n - m + 1

    idx = len(arr) - step
    ans = 0

    for _ in range(k):
        ans += arr[idx]
        idx -= step
    print(ans)