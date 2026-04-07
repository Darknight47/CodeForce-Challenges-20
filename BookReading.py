"""

------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/820/A ------------------------------------

Mister B once received a gift: it was a book about aliens, which he started read immediately. This book had c pages.

At first day Mister B read v0 pages, but after that he started to speed up. 
Every day, starting from the second, he read a pages more than on the previous day (at first day he read v0 pages, 
at second — v0 + a pages, at third — v0 + 2a pages, and so on). But Mister B is just a human, so he physically wasn't able to read more than v1 pages per day.

Also, to refresh his memory, every day, starting from the second, Mister B had to reread last l pages he read on the previous day. 
Mister B finished the book when he read the last page for the first time.

Help Mister B to calculate how many days he needed to finish the book.

Input
First and only line contains five space-separated integers: c, v0, v1, a and l (1 ≤ c ≤ 1000, 0 ≤ l < v0 ≤ v1 ≤ 1000, 0 ≤ a ≤ 1000) — the length of the book in pages, 
the initial reading speed, the maximum reading speed, the acceleration in reading speed and the number of pages for rereading.

Output
Print one integer — the number of days Mister B needed to finish the book.

Input:
5 5 10 5 4

Output:
1
"""
c, v0, v1, a, l = map(float, input().split())
read = v0
days = 1
while read < c:
    temp = v0 + a * days
    readable = min(temp, v1) - l
    read += readable
    days += 1
print(days)