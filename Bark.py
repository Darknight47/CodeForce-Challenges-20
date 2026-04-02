"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/868/A -------------------------------------------

As technologies develop, manufacturers are making the process of unlocking a phone as user-friendly as possible. 
To unlock its new phone, Arkady's pet dog Mu-mu has to bark the password once. The phone represents a password as a string of two lowercase English letters.

Mu-mu's enemy Kashtanka wants to unlock Mu-mu's phone to steal some sensible information, but it can only bark n distinct words, 
each of which can be represented as a string of two lowercase English letters. Kashtanka wants to bark several words (not necessarily distinct) one after another to 
pronounce a string containing the password as a substring. Tell if it's possible to unlock the phone in this way, or not.

Input
The first line contains two lowercase English letters — the password on the phone.

The second line contains single integer n (1 ≤ n ≤ 100) — the number of words Kashtanka knows.

The next n lines contain two lowercase English letters each, representing the words Kashtanka knows. The words are guaranteed to be distinct.

Output
Print "YES" if Kashtanka can bark several words in a line forming a string containing the password, and "NO" otherwise.

You can print each letter in arbitrary case (upper or lower).

Input:
ya
4
ah
oy
to
ha

Output:
YES
"""
password = input()
n = int(input())
last = False
first = False
ok = False
for _ in range(n):
    temp = input()
    if(temp == password or temp[::-1] == password):
        ok = True
    else:
        if(temp[0] == password[-1]):
            last = True
        if(temp[-1] == password[0]):
            first = True
        if(last and first):
            ok = True
print("YES" if ok else "NO")