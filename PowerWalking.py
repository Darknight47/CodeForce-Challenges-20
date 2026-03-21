"""

-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1642/B ------------------------------------

Sam is a kindergartener, and there are n children in his group. He decided to create a team with some of his children to play "brawl:go 2".

Sam has n power-ups, the i-th has type ai. 
A child's strength is equal to the number of different types among power-ups he has.

For a team of size k, Sam will distribute all n power-ups to k children in such a way that each of the k children receives at least one power-up, and each power-up is given to someone.

For each integer k from 1 to n, find the minimum sum of strengths of a team of k children Sam can get.

Input
Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 3⋅10^5) — the number of test cases. Description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 3⋅10^5).

The second line contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9) — types of Sam's power-ups.

It is guaranteed that the sum of n over all test cases does not exceed 3⋅10^5.

Output
For every test case print n integers.

The k-th integer should be equal to the minimum sum of strengths of children in the team of size k that Sam can get.

Input:
2
3
1 1 2
6
5 1 2 2 2 4

Output:
2 2 3 
4 4 4 4 5 6 
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    s = set(map(int, input().split()))
    d = len(s)
    arr = []
    for i in range(n):
        arr.append(max((i + 1), d))
    print(*arr)