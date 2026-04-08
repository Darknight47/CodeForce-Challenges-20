"""

---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2217/A ----------------------------------

To settle a long-time feud, Shaunak and Yash decided to play a game on an array a of n integers, with Shaunak going first. 
The players take turns, and the last player to make a move wins. On a player's turn, he chooses some ai>0 and decrements it by 1.

To make things interesting, Shaunak is allowed to use a special move at most once during the game. 
This move replaces his normal turn. When used, all elements ai (1 ≤ i ≤ n) are set to a special value k that is given initially.

Assuming that both players play optimally, determine if Shaunak can always win.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains two integers n and k (1 ≤ n ≤ 100, 1 ≤ k ≤ 500), denoting the size of the array and the special value.

The second line contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^3).

Output
For each test case, print "YES" if Shaunak can always win, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
4
1 1
1
2 67
67 67
3 2
3 3 3
11 3
1 2 3 4 5 6 7 8 9 10 11

Output:
YES
YES
YES
NO
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    temp_sum = sum(arr)
    if(temp_sum % 2 == 1):
        print("YES")
    else:
        if(n * k % 2 == 0):
            print("YES")
        else:
            print("NO")