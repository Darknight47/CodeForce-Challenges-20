"""

------------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2207/A --------------------------------------

Let n be a positive integer. Mario has a binary string∗ s of length n. 
In one move, he can choose any position i (2 ≤ i ≤ n−1) such that it's between two 1's, i.e., si−1=si+1=1, and then set si to either 0 or 1.

Mario can perform this operation as many times as he wants (possibly zero). What's the minimum and maximum number of 1's that can be in the resulting string?

∗ A binary string is a string whose characters are either 0 or 1.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains an integer n ( 3≤ n ≤ 100) — the length of the string.

The second line of each test case contains a string s of length n consisting of characters 0 or 1.

Output
For each test case, output two integers — the minimum and maximum number of 1's in the resulting string after some number of moves.

Input:
4
3
111
6
011011
7
1011101
9
100101101

Output:
2 3
3 5
4 7
5 7
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    s = list(input())

    ones = s.count('1')
    for i in range(1, n - 1):
        if s[i - 1] == '1' and s[i + 1] == '1' and s[i] == '0':
            s[i] = '1'
            ones += 1
    minimum = ones
    for i in range(1, n - 1):
        if s[i - 1] == '1' and s[i + 1] == '1' and s[i] == '1':
            s[i] = '0'
            minimum -= 1

    print(minimum, ones)