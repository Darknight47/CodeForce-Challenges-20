"""

--------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1138/A ---------------------------------------

Arkady invited Anna for a dinner to a sushi restaurant. The restaurant is a bit unusual: 
it offers n pieces of sushi aligned in a row, and a customer has to choose a continuous subsegment of these sushi to buy.

The pieces of sushi are of two types: either with tuna or with eel. Let's denote the type of the i-th from the left sushi as ti, where ti=1 means it is with tuna, and ti=2 means it is with eel.

Arkady does not like tuna, Anna does not like eel. Arkady wants to choose such a continuous subsegment of sushi that it has equal number of sushi of each type and each half of the 
subsegment has only sushi of one type. For example, subsegment [2,2,2,1,1,1] is valid, but subsegment [1,2,1,2,1,2] is not, because both halves contain both types of sushi.

Find the length of the longest continuous subsegment of sushi Arkady can buy.

Input
The first line contains a single integer n (2 ≤ n ≤ 100000) — the number of pieces of sushi.

The second line contains n integers t1, t2, ..., tn (ti=1, denoting a sushi with tuna or ti=2, denoting a sushi with eel), representing the types of sushi from left to right.

It is guaranteed that there is at least one piece of sushi of each type. Note that it means that there is at least one valid continuous segment.

Output
Print a single integer — the maximum length of a valid continuous segment.

Input:
7
2 2 2 1 1 2 2

Output:
4
"""
sze = int(input())
arr = list(map(int, input().split()))
idx = 0
ans = 0
while idx < sze:
    current = arr[idx]
    first_counter = 0
    while idx < sze and current == arr[idx]:
        idx += 1
        first_counter += 1
    if(idx >= sze):
        break
    temp_next = arr[idx]
    idx_reset = idx
    second_counter = 0
    while idx < sze and temp_next == arr[idx]:
        idx += 1
        second_counter += 1
    temp_max = min(first_counter, second_counter) * 2
    if(temp_max > ans):
        ans = temp_max
    idx = idx_reset
print(ans)