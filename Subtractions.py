"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/267/A ---------------------------------------------

You've got two numbers. As long as they are both larger than zero, they go through the same operation: subtract the lesser number from the larger one. 
If they equal substract one number from the another. For example, one operation transforms pair (4,17) to pair (4,13), it transforms (5,5) to (0,5).

You've got some number of pairs (ai, bi). How many operations will be performed for each of them?

Input
The first line contains the number of pairs n (1  ≤  n  ≤  1000). Then follow n lines, each line contains a pair of positive integers ai, bi (1  ≤  ai,  bi  ≤  10^9).

Output
Print the sought number of operations for each pair on a single line.

Input:
2
4 17
7 987654321

Output:
8
141093479
"""
cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    ans = 0
    while (a > 0 and b > 0):
        min_num = min(a, b)
        max_num = max(a, b)
        rest = max_num % min_num
        temp = max_num // min_num
        ans += temp
        a, b = min_num, rest
    print(ans)