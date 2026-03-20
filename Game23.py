"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1141/A -------------------------------

Polycarp plays "Game 23". Initially he has a number n and his goal is to transform it to m.
In one move, he can multiply n by 2 or multiply n by 3. He can perform any number of moves.

Print the number of moves needed to transform n to m. Print -1 if it is impossible to do so.

It is easy to prove that any way to transform n to m contains the same number of moves (i.e. number of moves doesn't depend on the way of transformation).

Input
The only line of the input contains two integers n and m (1 ≤ n ≤ m ≤ 5⋅10^8).

Output
Print the number of moves to transform n to m, or -1 if there is no solution.

Input:
120 51840

Output:
7
"""
n, m = map(int, input().split())

if m % n != 0:
    print(-1)
else:
    steps = 0
    r = m // n

    while r % 2 == 0:
        r //= 2
        steps += 1

    while r % 3 == 0:
        r //= 3
        steps += 1

    if r != 1:
        print(-1)
    else:
        print(steps)