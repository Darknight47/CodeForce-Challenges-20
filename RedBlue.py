"""

------------------------------------------------- Link for the challenge:  https://codeforces.com/problemset/problem/1469/B -------------------------------------------------

Monocarp had a sequence a consisting of n+m integers a1,a2,…,an+m. 
He painted the elements into two colors, red and blue; n elements were painted red, all other m elements were painted blue.

After painting the elements, he has written two sequences r1,r2,…,rn and b1,b2,…,bm. 
The sequence r consisted of all red elements of a in the order they appeared in a; 
similarly, the sequence b consisted of all blue elements of a in the order they appeared in a as well.

Unfortunately, the original sequence was lost, and Monocarp only has the sequences r and b. 
He wants to restore the original sequence. In case there are multiple ways to restore it, he wants to choose a way to restore that maximizes the value of

f(a)=max(0,a1,(a1+a2),(a1+a2+a3),…,(a1+a2+a3+⋯+an+m))

Help Monocarp to calculate the maximum possible value of f(a).

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of test cases. Then the test cases follow. Each test case consists of four lines.

The first line of each test case contains one integer n (1 ≤ n ≤ 100).

The second line contains n integers r1,r2,…,rn (−100 ≤ ri ≤ 100).

The third line contains one integer m (1 ≤ m ≤ 100).

The fourth line contains m integers b1,b2,…,bm (−100 ≤ bi ≤ 100).

Output
For each test case, print one integer — the maximum possible value of f(a).

Input:
4
4
6 -5 7 -3
3
2 3 -4
2
1 1
4
10 -3 2 2
5
-1 -2 -3 -4 -5
5
-1 -2 -3 -4 -5
1
0
1
0

Output:
13
13
0
0
"""
cases = int(input())
for _ in range(cases):
    a = int(input())
    arr = list(map(int, input().split()))
    b = int(input())
    brr = list(map(int, input().split()))
    sum_a = 0
    best_a = 0
    for num in arr:
        sum_a += num
        if(sum_a > best_a):
            best_a = sum_a
    sum_b = 0
    best_b = 0
    for num in brr:
        sum_b += num
        if(sum_b > best_b):
            best_b = sum_b
    print(best_a + best_b)