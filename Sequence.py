"""

----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2210/A -----------------------------------

You are given an integer n. 
You need to construct a permutation∗ a1,a2,…,an using integers from 1 to n such that the following condition is satisfied:

a1 mod a2 ≥ a2 mod a3 ≥ … ≥ an-1 mod an,
where u mod v denotes the remainder of dividing u by v.

If multiple valid permutations exist, you may output any of them.

It can be shown that a valid permutation always exists for every n ≥ 2.

∗ A permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array), and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 100).

Output
For each test case, output on a single line n space-separated integers a1,a2,…an.

If multiple valid permutations exist, you may output any of them.

Input:
4
2
3
4
5

Output:
2 1
2 3 1
2 4 3 1
3 5 4 2 1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(range(1, n + 1))
    arr.reverse()
    print(*arr)