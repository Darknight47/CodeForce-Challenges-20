"""

--------------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/653/A ----------------------------------

Limak is a little polar bear. He has n balls, the i-th ball has size ti.

Limak wants to give one ball to each of his three friends. Giving gifts isn't easy — there are two rules Limak must obey to make friends happy:

No two friends can get balls of the same size.
No two friends can get balls of sizes that differ by more than 2.
For example, Limak can choose balls with sizes 4, 5 and 3, or balls with sizes 90, 91 and 92. 
But he can't choose balls with sizes 5, 5 and 6 (two friends would get balls of the same size), and he can't choose balls with sizes 30, 31 and 33 (because sizes 30 and 33 differ by more than 2).

Your task is to check whether Limak can choose three balls that satisfy conditions above.

Input
The first line of the input contains one integer n (3 ≤ n ≤ 50) — the number of balls Limak has.

The second line contains n integers t1, t2, ..., tn (1 ≤ ti ≤ 1000) where ti denotes the size of the i-th ball.

Output
Print "YES" (without quotes) if Limak can choose three balls of distinct sizes, such that any two of them differ by no more than 2. Otherwise, print "NO" (without quotes).

Input:
4
18 55 16 17

Output:
YES
"""
sze = int(input())
temp_set = sorted(set(map(int, input().split())))
ok = False
for i in range(len(temp_set) - 2):
    first = temp_set[i]
    second = temp_set[i + 1]
    third = temp_set[i + 2]
    diff1 = second - first
    diff2 = third - second
    diff3 = third - first
    if(diff1 <= 2 and diff2 <= 2 and diff3 <= 2):
        ok = True
        break
print("YES" if ok else "NO")