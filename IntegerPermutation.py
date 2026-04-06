"""

----------------------------------------- Link for the challenge: https://codeforces.com/contest/2218/problem/C -----------------------------------------

Upon arriving at school, Macaque was rather brusquely greeted by his friend, AG-88301, the latter having skived off his homework due to spending the entire 
night yapping to an unsuspecting stranger about his groundbreaking work on a proof of the Collatz conjecture and his 67-th unreciprocated love interest. 
So, as had become customary, AG-88301, with ever decreasing levels of gratitude or appreciation, made Macaque do his homework for him. 
At this point, Macaque had had enough, and turned to his minions (you guys!) to solve AG-88301's homework task.

You are given an integer n. 
You must construct a permutation∗ of length 3n such that, if you partition the permutation into n contiguous blocks with 3 elements, the sum of the medians† of these blocks is maximised.

More formally, you must construct a permutation p of length 3n such that ∑n−1i=0median(a3i+1,a3i+2,a3i+3) is maximised. If there are multiple possible p, output any.

∗ A permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array), and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

† The median of an array b containing 3 elements is the 2-nd element after b is sorted in non-decreasing order.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first and only line of each test case contains an integer n (1 ≤ n ≤ 10^5).

It is guaranteed that the sum of 3n does not exceed 3⋅10^5 over all test cases.

Output
For each test case, output a permutation p such that the sum of the medians of the contiguous blocks is maximised. If there are multiple possible p, output any.

Input:
3
2
1
3

Output:
1 3 4 2 5 6 
3 1 2
5 2 4 8 3 9 7 1 6
"""
cases = int(input())
for _ in range(cases):
    n = int(input()) * 3
    arr = list(range(1, n + 1))
    l, r = 0, len(arr) - 1
    out = []

    while l <= r:
        # take 1 from the left
        out.append(arr[l])
        l += 1

        # take 2 from the right
        if l <= r:
            out.append(arr[r])
            r -= 1
        if l <= r:
            out.append(arr[r])
            r -= 1
    print(*out)