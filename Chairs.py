"""

----------------------------------- Link for the challenge: https://codeforces.com/contest/2210/problem/B -----------------------------------

There are n chairs in a row, initially all unmarked.

You are given a permutation p∗ of length n.

Now, you play a game. You visit each chair sequentially, starting from the 1-st chair. At the i-th chair, you can do the following:

If the i-th chair is already marked, then you end the game immediately without sitting on it. 
Otherwise, you can choose to sit on the chair or skip it and move to the next chair.
If you choose to sit on the chair, then after standing up, you mark the pi -th chair and move to the next chair.
If all the n chairs are visited, the game ends.
Your task is to determine the maximum number of chairs that you can sit on.

∗ A permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array), and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the number of chairs.

The second line of each test case contains n distinct integers p1,p2,…,pn — the permutation p.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
Output a single integer — the maximum number of chairs you can sit on.

Input:
4
3
3 2 1
5
4 3 2 5 1
4
4 2 1 3
4
2 3 4 1

Output:
2
2
3
1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if(arr[i] <= i + 1):
            ans += 1
    print(ans)