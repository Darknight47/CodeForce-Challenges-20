"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1182/A -----------------------------------

You have a given integer n. 
Find the number of ways to fill all 3×n tiles with the shape described in the picture below. Upon filling, no empty spaces are allowed. Shapes cannot overlap.

You have a given integer n. 
Find the number of ways to fill all 3×n tiles with the shape described in the picture below. Upon filling, no empty spaces are allowed. Shapes cannot overlap.

Input:
4

Output:
4
"""
n = int(input())
if(n % 2 == 0):
    print(int(2**(n/2))) # Positions are paired; choosing one side of the pair forces the other.
else:
    print(0)