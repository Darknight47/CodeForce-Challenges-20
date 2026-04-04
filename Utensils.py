"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1032/A ---------------------------------------------

The king's birthday dinner was attended by k guests. 
The dinner was quite a success: every person has eaten several dishes (though the number of dishes was the same for every person) and every dish was served alongside with a new set of kitchen utensils.

All types of utensils in the kingdom are numbered from 1 to 100. 
It is known that every set of utensils is the same and consist of different types of utensils, although every particular type may appear in the set at most once. For example, a valid set of utensils can be composed of one fork, one spoon and one knife.

After the dinner was over and the guests were dismissed, the king wondered what minimum possible number of utensils could be stolen. 
Unfortunately, the king has forgotten how many dishes have been served for every guest but he knows the list of all the utensils left after the dinner. 
Your task is to find the minimum possible number of stolen utensils.

Input
The first line contains two integer numbers n and k (1 ≤ n ≤ 100, 1 ≤ k ≤ 100)  — the number of kitchen utensils remaining after the dinner and the number of guests correspondingly.

The next line contains n integers a1,a2,…,an (1 ≤ ai ≤ 100)  — the types of the utensils remaining. Equal values stand for identical utensils while different values stand for different utensils.

Output
Output a single value — the minimum number of utensils that could be stolen by the guests.

Input:
5 2
1 2 2 1 3

Output:
1
"""
from collections import Counter
import math
n, k = map(int, input().split())
arr = list(map(int, input().split()))
counts = Counter(arr)
# compute minimum dishes per person
minimum_dishes = 0
for c in counts.values():
    minimum_dishes = max(minimum_dishes, math.ceil(c / k))
stolen = 0
for c in counts.values():
    stolen += minimum_dishes * k - c
print(stolen)