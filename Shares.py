"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/793/A ----------------------------------------

Oleg the bank client checks share prices every day. There are n share prices he is interested in. 
Today he observed that each second exactly one of these prices decreases by k rubles (note that each second exactly one price changes, but at different seconds different prices can change). 
Prices can become negative. Oleg found this process interesting, and he asked Igor the financial analyst, 
what is the minimum time needed for all n prices to become equal, or it is impossible at all? Igor is busy right now, so he asked you to help Oleg. Can you answer this question?

Input
The first line contains two integers n and k (1 ≤ n ≤ 105, 1 ≤ k ≤ 109) — the number of share prices, and the amount of rubles some price decreases each second.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 109) — the initial prices.

Output
Print the only line containing the minimum number of seconds needed for prices to become equal, of «-1» if it is impossible.

Input:
3 3
12 9 15

Output:
3
"""
n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))
first = arr[0]
ok = True
ans = 0
for i in range(1, n):
    diff = arr[i] - first
    if(diff % k != 0):
        ok = False
        break
    ans += diff // k
print(ans if ok else -1)