"""

--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1763/A -------------------------------

You are given an array a of length n. You can perform the following operation several (possibly, zero) times:

Choose i, j, b: Swap the b-th digit in the binary representation of ai and aj.
Find the maximum possible value of max(a)−min(a).

In a binary representation, bits are numbered from right (least significant) to left (most significant). 
Consider that there are an infinite number of leading zero bits at the beginning of any binary representation.

For example, swap the 0-th bit for 4=1002 and 3=112 will result 1012=5 and 102=2. 
Swap the 2-nd bit for 4=1002 and 3=112 will result 0002=02=0 and 1112=7.

Here, max(a) denotes the maximum element of array a and min(a) denotes the minimum element of array a.

The binary representation of x is x written in base 2. 
For example, 9 and 6 written in base 2 are 1001 and 110, respectively.

Input
The first line contains a single integer t (1 ≤ t ≤ 128) — the number of testcases.

The first line of each test case contains a single integer n (3 ≤ n ≤ 512) — the length of array a.

The second line of each test case contains n integers a1,a2,…,an (0 ≤ ai < 1024) — the elements of array a.

It's guaranteed that the sum of n over all testcases does not exceed 512.

Output
For each testcase, print one integer — the maximum possible value of max(a)−min(a).

Input:
4
3
1 0 1
4
5 5 5 5
5
1 2 3 4 5
7
20 85 100 41 76 49 36

Output:
1
0
7
125
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    ts = set(arr)
    if(len(ts) == 1):
        print(0)
        continue
    total_or = 0
    for x in arr:
        total_or |= x # or
    total_and = arr[0]
    for x in arr[1:]:
        total_and &= x
    print(total_or - total_and)    