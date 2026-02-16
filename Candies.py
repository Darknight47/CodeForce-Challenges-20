"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1283/B --------------------------------------------

Santa has n candies and he wants to gift them to k kids. 
He wants to divide as many candies as possible between all k kids. 
Santa can't divide one candy into parts but he is allowed to not use some candies at all.

Suppose the kid who recieves the minimum number of candies has a candies and the kid who recieves the maximum number of candies has b candies. 
Then Santa will be satisfied, if the both conditions are met at the same time:

b−a≤1 (it means b=a or b=a+1);
the number of kids who has a+1 candies (note that a+1 not necessarily equals b) does not exceed ⌊k2⌋ (less than or equal to ⌊k2⌋).
⌊k2⌋ is k divided by 2 and rounded down to the nearest integer. For example, if k=5 then ⌊k2⌋=⌊52⌋=2.

Your task is to find the maximum number of candies Santa can give to kids so that he will be satisfied.

You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1 ≤ t ≤ 5⋅10^4) — the number of test cases.

The next t lines describe test cases. The i-th test case contains two integers n and k (1 ≤ n, k ≤ 10^9) — the number of candies and the number of kids.

Output
For each test case print the answer on it — the maximum number of candies Santa can give to kids so that he will be satisfied.

Input:
5
5 2
19 4
12 7
6 2
100000 50010

Output:
5
18
10
6
75015
"""
cases = int(input())
for _ in range(cases):
    candies, kids = map(int, input().split())
    # if(candies < kids):
    #     print(candies)
    #     continue
    total_candies = candies - (candies % kids)
    total_candies += min(candies % kids, kids // 2)
    print(total_candies)