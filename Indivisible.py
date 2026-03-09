"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1818/B ------------------------------------

You're given a positive integer n.

Find a permutation a1,a2,…,an such that for any 1≤l<r≤n, the sum al+al+1+⋯+ar is not divisible by r−l+1.

A permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array), and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). Description of the test cases follows.

The first line of each test case contain a single integer n (1 ≤ n ≤ 100) — the size of the desired permutation.

Output
For each test case, if there is no such permutation print −1.

Otherwise, print n distinct integers p1,p2,…,pn (1 ≤ pi ≤ n) — a permutation satisfying the condition described in the statement.

If there are multiple solutions, print any.

Input:
3
1
2
3

Output:
1
1 2
-1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n == 1):
        print(1)
    else:
        if(n % 2 == 0):
            arr = list(range(1, n + 1))
            for i in range(0, n - 1, 2):
                print(arr[i + 1], arr[i], end=" ")
            print()
        else:
            print(-1)