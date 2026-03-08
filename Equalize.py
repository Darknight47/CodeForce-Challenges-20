"""

---------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1183/B ---------------------------------------

There are n products in the shop. The price of the i-th product is ai. 
The owner of the shop wants to equalize the prices of all products. However, he wants to change prices smoothly.

In fact, the owner of the shop can change the price of some product i in such a way that the difference between the old price of this product ai and the new price bi is at most k. 
In other words, the condition |ai−bi|≤k should be satisfied (|x| is the absolute value of x).

He can change the price for each product not more than once. Note that he can leave the old prices for some products. 
The new price bi of each product i should be positive (i.e. bi>0 should be satisfied for all i from 1 to n).

Your task is to find out the maximum possible equal price B of all productts with the restriction that for all products the condiion |ai−B|≤k should be satisfied 
(where ai is the old price of the product and B is the same new price of all products) or report that it is impossible to find such price B.

Note that the chosen price B should be integer.

You should answer q independent queries.

Input
The first line of the input contains one integer q (1 ≤ q ≤ 100) — the number of queries. Each query is presented by two lines.

The first line of the query contains two integers n and k (1 ≤ n ≤ 100, 1 ≤ k ≤ 10^8) — the number of products and the value k. 
The second line of the query contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^8), where ai is the price of the i-th product.

Output
Print q integers, where the i-th integer is the answer B on the i-th query.

If it is impossible to equalize prices of all given products with restriction that for all products the condition |ai−B|≤k should be satisfied 
(where ai is the old price of the product and B is the new equal price of all products), print -1. Otherwise print the maximum possible equal price of all products.

Input:
4
5 1
1 1 2 3 1
4 2
6 4 8 5
2 2
1 6
3 5
5 2 5

Output:
2
6
-1
7
"""
cases = int(input())
for _ in range(cases):
    sze, k = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    ans = arr[0] + k
    ok = True
    for i in range(sze - 1, -1, -1):
        temp = abs(arr[i] - ans)
        if(temp > k):
            ok = False
            break
    if(ok):
        print(ans)
    else:
        print(-1)