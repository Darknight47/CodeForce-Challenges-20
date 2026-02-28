"""

------------------------------------------ Link for the challenge: https://codeforces.com/contest/2203/problem/B -----------------------------------

Let's define F(x) as the sum of the digits of x. An integer x is considered beautiful if F(F(x))=F(x).

You are given an integer x. 
In one move, you can choose any digit in the number and replace it with another. The resulting number cannot have leading zeros.

Your task is to calculate the minimum number of moves (possibly zero) required to make the given number beautiful.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The only line of each test case contains a single integer x (1 ≤ x ≤ 10^18).

Output
For each test case, print a single integer — the minimum number of moves (possibly zero) required to make the given number beautiful.

Input:
4
1
37
645
2374236843276813

Output:
0
1
2
12
"""
cases = int(input())
for _ in range(cases):
    s = input().strip()
    total = 0
    a = []

    for i, ch in enumerate(s):
        x = int(ch)
        total += x
        a.append(x - (i == 0))

    a.sort()
    ans = 0

    i = len(a) - 1
    while total > 9:
        total -= a[i]
        i -= 1
        ans += 1

    print(ans)