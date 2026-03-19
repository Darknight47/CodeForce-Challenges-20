"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1823/B ----------------------------------

Let's define a permutation of length n as an array p of length n, which contains every number from 1 to n exactly once.

You are given a permutation p1,p2,…,pn and a number k. 
You need to sort this permutation in the ascending order. In order to do it, you can repeat the following operation any number of times (possibly, zero):

pick two elements of the permutation pi and pj such that |i−j|=k, and swap them.
Unfortunately, some permutations can't be sorted with some fixed numbers k. 
For example, it's impossible to sort [2,4,3,1] with k=2.

That's why, before starting the sorting, you can make at most one preliminary exchange:

choose any pair pi and pj and swap them.
Your task is to:

check whether is it possible to sort the permutation without any preliminary exchanges,
if it's not, check, whether is it possible to sort the permutation using exactly one preliminary exchange.
For example, if k=2 and permutation is [2,4,3,1], then you can make a preliminary exchange of p1 and p4, which will produce permutation [1,4,3,2], which is possible to sort with given k.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains two integers n and k (2 ≤ n ≤ 2⋅10^5; 1 ≤ k ≤ n−1) — length of the permutation, and a distance between elements that can be swapped.

The second line of each test case contains n integers p1,p2,…,pn (1 ≤ pi ≤ n) — elements of the permutation p.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case print
0, if it is possible to sort the permutation without preliminary exchange;
1, if it is possible to sort the permutation with one preliminary exchange, but not possible without preliminary exchange;
-1, if it is not possible to sort the permutation with at most one preliminary exchange.

Input:
6
4 1
3 1 2 4
4 2
3 4 1 2
4 2
3 1 4 2
10 3
4 5 9 1 8 6 10 2 3 7
10 3
4 6 9 1 8 5 10 2 3 7
10 3
4 6 9 1 8 5 10 3 2 7

Output:
0
0
1
0
1
-1
"""
cases = int(input())
for _ in range(cases):
    sze, k = map(int, input().split())
    arr = list(map(int, input().split()))

    bad = 0
    for i in range(sze):
        if((i + 1) % k != arr[i] % k):
            bad += 1
    if(bad == 0):
        print(0)
    elif(bad == 2):
        print(1)
    else:
        print(-1)