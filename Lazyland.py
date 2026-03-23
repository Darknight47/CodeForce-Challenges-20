"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1089/L ------------------------------------------

The kingdom of Lazyland is the home to n idlers. These idlers are incredibly lazy and create many problems to their ruler, the mighty King of Lazyland.

Today k important jobs for the kingdom (k≤n) should be performed. Every job should be done by one person and every person can do at most one job. 
The King allowed every idler to choose one job they wanted to do and the i-th idler has chosen the job ai.

Unfortunately, some jobs may not be chosen by anyone, so the King has to persuade some idlers to choose another job. The King knows that it takes bi minutes to persuade the i-th idler. 
He asked his minister of labour to calculate the minimum total time he needs to spend persuading the idlers to get all the jobs done. Can you help him?

Input
The first line of the input contains two integers n and k (1 ≤ k ≤ n ≤ 10^5) — the number of idlers and the number of jobs.

The second line of the input contains n integers a1,a2,…,an (1 ≤ ai ≤ k) — the jobs chosen by each idler.

The third line of the input contains n integers b1,b2,…,bn (1 ≤ bi ≤ 10^9) — the time the King needs to spend to persuade the i-th idler.

Output
The only line of the output should contain one number — the minimum total time the King needs to spend persuading the idlers to get all the jobs done.

Input:
8 7
1 1 3 1 5 3 7 1
5 7 4 8 1 3 5 2

Output:
10
"""
n, k = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
diction = {}
for i in range(n):
    if(arr[i] not in diction):
        diction[arr[i]] = [brr[i]]
    else:
        diction[arr[i]].append(brr[i])
temp_arr = []
temp_set = set()
for tk, tarr in diction.items():
    temp_set.add(tk)
    if(len(tarr) > 1):
        arr_sorted = sorted(tarr)
        temp_arr.extend(arr_sorted[:len(arr_sorted) - 1])
if(len(temp_set) == k):
    print(0)
else:
    temp_arr.sort()
    diff = k - len(temp_set)
    ans = 0
    for i in range(diff):
        ans += temp_arr[i]
    print(ans)