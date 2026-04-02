"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/52/A ---------------------------------------

There is a given sequence of integers a1, a2, ..., an, where every number is from 1 to 3 inclusively. 
You have to replace the minimum number of numbers in it so that all the numbers in the sequence are equal to each other.

Input
The first line contains an integer n (1 ≤ n ≤ 106). The second line contains a sequence of integers a1, a2, ..., an (1 ≤ ai ≤ 3).

Output
Print the minimum number of replacements needed to be performed to make all the numbers in the sequence equal.

Input:
9
1 3 2 2 2 1 1 2 3

Output:
5
"""
from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
counter = Counter(arr)
max_freq = max(counter.values())
print(n - max_freq)