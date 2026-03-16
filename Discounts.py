"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1132/B ---------------------------------------

You came to a local shop and want to buy some chocolate bars. There are n bars in the shop, i-th of them costs ai coins (and you want to buy all of them).

You have m different coupons that allow you to buy chocolate bars. i-th coupon allows you to buy qi chocolate bars while you have to 
pay only for the qi−1 most expensive ones (so, the cheapest bar of those qi bars is for free).

You can use only one coupon; if you use coupon i, you have to choose qi bars and buy them using the coupon, and buy all the remaining n−qi bars without any discounts.

To decide which coupon to choose, you want to know what will be the minimum total amount of money you have to pay if you use one of the coupons optimally.

Input
The first line contains one integer n (2 ≤ n ≤ 3⋅10^5) — the number of chocolate bars in the shop.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 10^9), where ai is the cost of i-th chocolate bar.

The third line contains one integer m (1 ≤ m ≤ n−1) — the number of coupons you have.

The fourth line contains m integers q1, q2, ..., qm (2 ≤ qi ≤ n), where qi is the number of chocolate bars you have to buy using i-th coupon so 
that the least expensive of them will be for free. All values of qi are pairwise distinct.

Output
Print m integers, i-th of them should be the minimum amount of money you have to pay if you buy qi bars with i-th coupon, and all the remaining bars one by one for their full price.

Input:
7
7 1 3 1 4 10 8
2
3 4

Output:
27
30
"""
n = int(input())
arr = sorted(list(map(int, input().split())))
total_sum = sum(arr)
q = int(input())
discounts = list(map(int, input().split()))
for discount in discounts:
    idx = n - discount
    temp = arr[idx]
    print(total_sum - temp)