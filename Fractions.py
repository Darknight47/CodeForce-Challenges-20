"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1720/A -------------------------------------------

Burenka came to kindergarden. This kindergarten is quite strange, so each kid there receives two fractions (ab and cd) with integer numerators and denominators. 
Then children are commanded to play with their fractions.

Burenka is a clever kid, so she noticed that when she claps once, she can multiply numerator or denominator of one of her two fractions by any integer of her choice (but she can't multiply denominators by 0).
 Now she wants know the minimal number of claps to make her fractions equal (by value). Please help her and find the required number of claps!

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases. Then follow the descriptions of each test case.

The only line of each test case contains four integers a, b, c and d (0 ≤ a, c ≤ 10^9, 1 ≤ b, d ≤ 10^9) — numerators and denominators of the fractions given to Burenka initially.

Output
For each test case print a single integer — the minimal number of claps Burenka needs to make her fractions equal.

Input:
8
2 1 1 1
6 3 2 1
1 2 2 3
0 1 0 100
0 1 228 179
100 3 25 6
999999999 300000000 666666666 100000000
33 15 0 84

Output:
1
0
2
0
1
1
1
1
"""
def min_ops(a, b, c, d):
    # Case 1: both fractions are zero
    if a == 0 and c == 0:
        return 0
    # Case 2: exactly one is zero → 1 operation (multiply numerator by 0)
    if a == 0 and c != 0:
        return 1
    if a != 0 and c == 0:
        return 1
    # Case 3: already equal
    if a * d == b * c:
        return 0

    if a * d % (b * c) == 0 or (b * c) % (a * d) == 0:
        return 1
    # Otherwise, need 2 operations
    return 2

cases = int(input())
for _ in range(cases):
    a, b, c, d = map(int, input().split())
    print(min_ops(a, b, c, d))
    print("----------------------")