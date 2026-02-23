"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1216/B --------------------------------------------

Recently Vasya decided to improve his pistol shooting skills. Today his coach offered him the following exercise. 
He placed n cans in a row on a table. Cans are numbered from left to right from 1 to n. 
Vasya has to knock down each can exactly once to finish the exercise. He is allowed to choose the order in which he will knock the cans down.

Vasya knows that the durability of the i-th can is ai. 
It means that if Vasya has already knocked x cans down and is now about to start shooting the i-th one, he will need (ai⋅x+1) shots to knock it down. 
You can assume that if Vasya starts shooting the i-th can, he will be shooting it until he knocks it down.

Your task is to choose such an order of shooting so that the number of shots required to knock each of the n given cans down exactly once is minimum possible.

Input
The first line of the input contains one integer n (2 ≤ n ≤ 1000) — the number of cans.

The second line of the input contains the sequence a1,a2,…,an (1 ≤ ai ≤ 1000), where ai is the durability of the i-th can.

Output
In the first line print the minimum number of shots required to knock each of the n given cans down exactly once.

In the second line print the sequence consisting of n distinct integers from 1 to n — the order of indices of cans that minimizes the number of shots required. 
If there are several answers, you can print any of them.

Input:
3
20 10 20

Output:
43
1 3 2 
"""
sze = int(input())
arr = list(map(int, input().split()))
diction = {}
for i in range(sze):
    diction[i + 1] = arr[i]
sorted_dict = sorted(diction.items(), key=lambda x: x[1], reverse=True)
shoots = 0
orders = []
ans = 0
for tk, tv in sorted_dict:
    ans += (shoots * tv) + 1
    orders.append(tk)
    shoots += 1
print(ans)
print(*orders)