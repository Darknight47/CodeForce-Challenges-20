"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/450/A -----------------------------------------

There are n children in Jzzhu's school. Jzzhu is going to give some candies to them. Let's number all the children from 1 to n. The i-th child wants to get at least ai candies.

Jzzhu asks children to line up. Initially, the i-th child stands at the i-th place of the line. Then Jzzhu start distribution of the candies. He follows the algorithm:

Give m candies to the first child of the line.
If this child still haven't got enough candies, then the child goes to the end of the line, else the child go home.
Repeat the first two steps while the line is not empty.
Consider all the children in the order they go home. Jzzhu wants to know, which child will be the last in this order?

Input
The first line contains two integers n, m (1 ≤ n ≤ 100; 1 ≤ m ≤ 100). The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 100).

Output
Output a single integer, representing the number of the last child.

Input:
5 2
1 3 1 4 2

Output:
4
"""
import math
sze, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
ans_idx = 0
for i in range(sze):
    needed = arr[i]
    temp = math.ceil(needed / m)
    if(temp > ans):
        ans = temp
        ans_idx = i + 1
    elif(temp == ans):
        ans_idx = i + 1
print(ans_idx)