"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/16/B -------------------------------------

A burglar got into a matches warehouse and wants to steal as many matches as possible. 
In the warehouse there are m containers, in the i-th container there are ai matchboxes, and each matchbox contains bi matches. 
All the matchboxes are of the same size. The burglar's rucksack can hold n matchboxes exactly. 
Your task is to find out the maximum amount of matches that a burglar can carry away. 
He has no time to rearrange matches in the matchboxes, that's why he just chooses not more than n matchboxes so that the total amount of matches in them is maximal.

Input
The first line of the input contains integer n (1 ≤ n ≤ 2·10^8) and integer m (1 ≤ m ≤ 20). 
The i + 1-th line contains a pair of numbers ai and bi (1 ≤ ai ≤ 10^8,  1 ≤ bi ≤ 10). All the input numbers are integer.

Output
Output the only number — answer to the problem.

Input:
7 3
5 10
2 5
3 6

Output:
62
"""
rucksack, containers = map(int, input().split())
diction = {}
arr = []
for i in range(containers):
    a, b = map(int, input().split())
    diction[i] = b
    arr.append(a)
sorted_dict = sorted(diction.items(), key=lambda x: x[1], reverse=True)
ans = 0
for idx, amount in sorted_dict:
    temp_box = arr[idx]
    if(rucksack > 0):
        if(rucksack >= temp_box):
            ans += temp_box * amount
            rucksack = rucksack - temp_box
        else:
            ans += rucksack * amount
            rucksack = 0
    else:
        break
print(ans)