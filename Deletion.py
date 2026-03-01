"""

----------------------------------------------- Link for the challenge: https://codeforces.com/contest/2200/problem/B ------------------------------------------

AksLolCoding is playing a game on an array a of n positive integers. During each turn:

If a is non-decreasing∗, the game ends.
Otherwise, AksLolCoding can choose any single element and remove it from the array.
Determine the minimum possible number of elements that can be remaining in the array after the game ends.

∗ a is non-decreasing if ai≤ai+1 for all 1≤i≤m−1, where m is the length of a.

Input
The first line contains an integer t (1 ≤ t ≤ 1000), the number of test cases.

The first line of each test case contains an integer n (1 ≤ n ≤ 10).

The second line of each test case contains n integers, the elements of a (1 ≤ ai ≤ 100).

Output
For each test case, output an integer: the minimum possible number of elements left once the array is sorted.

Input:
3
4
1 4 2 3
1
100
2
6 7

Output:
1
1
2
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    ans = sze
    for i in range(sze - 1):
        if(arr[i] > arr[i + 1]):
            ans = 1
            break
    if(sze == 1):
        print(1)
    else:
        print(ans)