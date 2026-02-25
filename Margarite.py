"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1080/B --------------------------------------------

Little girl Margarita is a big fan of competitive programming. She especially loves problems about arrays and queries on them.

Recently, she was presented with an array a of the size of 109 elements that is filled as follows:

a1=−1
a2=2
a3=−3
a4=4
a5=−5
And so on ...
That is, the value of the i-th element of the array a is calculated using the formula ai=i⋅(−1)i.

She immediately came up with q queries on this array. Each query is described with two numbers: l and r. 
The answer to a query is the sum of all the elements of the array at positions from l to r inclusive.

Margarita really wants to know the answer to each of the requests. She doesn't want to count all this manually, but unfortunately, she couldn't write the program that solves the problem either. 
She has turned to you — the best programmer.

Help her find the answers!

Input
The first line contains a single integer q (1 ≤ q ≤ 10^3) — the number of the queries.

Each of the next q lines contains two integers l and r (1 ≤ l ≤ r ≤ 10^9) — the descriptions of the queries.

Output
Print q lines, each containing one number — the answer to the query.

Input:
5
1 3
2 5
5 5
4 4
2 3

Output:
-2
-2
-5
4
-1
"""
cases = int(input())
for _ in range(cases):
    l, r = map(int, input().split())
    evens = r // 2
    odds = (r + 1) // 2
    even_sum = evens * (evens + 1) * -1
    odd_sum = odds**2
    one_to_r = even_sum + odd_sum
    
    evens = (l - 1) // 2
    odds = l // 2
    even_sum = evens * (evens + 1) * -1
    odd_sum = odds**2
    one_to_l_min_1 = even_sum + odd_sum
    ans = one_to_r - one_to_l_min_1
    print(ans * -1)