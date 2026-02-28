"""


---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2203/A -------------------------------------

Monocarp has n identical boxes. The weight of each box is m, and the durability of each box is d.

To save space, Monocarp wants to build several "towers" of boxes by stacking them on top of each other. Each tower will consist of a positive (greater than 0) 
integer number of boxes stacked on top of each other. To ensure that no box breaks, the following condition must be met:

for each box, the total weight of all boxes above it must not exceed the durability of that box.
Help Monocarp calculate the minimum number of towers he can achieve, given that each of the n boxes must be used.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case consists of a single line containing three integers n,m,d (1 ≤ n, m, d ≤ 50).

Output
For each test case, print one integer — the minimum number of towers.

Input:
3
8 10 20
8 1 20
5 3 2

Output:
3
1
5
"""
import math
cases = int(input())
for _ in range(cases):
    n, m, d = map(int, input().split())
    if(m > d):
        print(n)
    else:
        tower_boxes = d // m
        tower_height = tower_boxes + 1
        temp = math.ceil(n / tower_height)
        print(temp)