"""

---------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/127/A -----------------------------------------

Mr. Scrooge, a very busy man, decided to count the time he wastes on all sorts of useless stuff to evaluate the lost profit. He has already counted the time he wastes sleeping and eating. 
And now Mr. Scrooge wants to count the time he has wasted signing papers.

Mr. Scrooge's signature can be represented as a polyline A1A2... An. Scrooge signs like that: 
first it places a pen at the point A1, then draws a segment from point A1 to point A2, then he draws a segment from point A2 to point A3 and so on to point An, where he stops signing and takes the pen off the paper. 
At that the resulting line can intersect with itself and partially repeat itself but Scrooge pays no attention to it and never changes his signing style. 
As Scrooge makes the signature, he never takes the pen off the paper and his writing speed is constant — 50 millimeters per second.

Scrooge signed exactly k papers throughout his life and all those signatures look the same.

Find the total time Scrooge wasted signing the papers.

Input
The first line contains two integers n and k (2 ≤ n ≤ 100, 1 ≤ k ≤ 1000). Each of the following n lines contains the coordinates of the polyline's endpoints. 
The i-th one contains coordinates of the point Ai — integers xi and yi, separated by a space.

All points Ai are different. The absolute value of all coordinates does not exceed 20. The coordinates are measured in millimeters.

Output
Print one real number — the total time Scrooges wastes on signing the papers in seconds. The absolute or relative error should not exceed 10^ - 6.

Input:
2 1
0 0
10 0

Output:
0.200000000
"""
import math
n, k = map(int, input().split())
coor = []
for _ in range(n):
    x, y = map(int, input().split())
    coor.append((x, y))
dist = 0
for i in range(n - 1):
    p1 = coor[i]
    p2 = coor[i + 1]
    dist += math.dist(p1, p2)
dist = k * dist
ans = dist / 50
print(ans)