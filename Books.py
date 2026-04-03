"""

---------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1737/A ----------------------------------------------------

n books must be split into k compartments on the bookshelf (n is divisible by k). Each book is represented by a lowercase Latin letter from 'a' to 'y' inclusively, 
which is the beginning letter in the title of the book.

Ela must stack exactly nk books in each compartment. After the books are stacked, for each compartment indexed from 1 to k, 
she takes the minimum excluded (MEX) letter of the multiset of letters formed by letters representing all books in that compartment, then combines the resulting letters into a string. 
The first letter of the resulting string is the MEX letter of the multiset of letters formed by the first compartment, 
the second letter of the resulting string is the MEX letter of the multiset of letters formed by the second compartment, ... and so on. 
Please note, under the constraint of this problem, MEX letter can always be determined for any multiset found in this problem because 'z' is not used.

What is the lexicographically greatest resulting string possible that Ela can create?

A string a is lexicographically greater than a string b if and only if one of the following holds:

b is a prefix of a, but b≠a;
in the first position where a and b differ, the string a has a letter that appears later in the alphabet than the corresponding letter in b.
The minimum excluded (MEX) letter of a multiset of letters is the letter that appears earliest in the alphabet and is not contained in the multiset. 
For example, if a multiset of letters contains 7 letters 'b', 'a', 'b', 'c', 'e', 'c', 'f' respectively, then the MEX letter of this compartment is 'd', 
because 'd' is not included in the multiset, and all letters comes before 'd' in the alphabet, namely 'a', 'b' and 'c', are included in the multiset.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). Description of the test cases follows.

The first line of each test case contains two integers n and k (1 ≤ n ≤ 200; 1 ≤ k ≤ n). It is guaranteed that n is divisible by k.

The second line of each test case contains a string of n lowercase Latin letters from 'a' to 'y' inclusively. 
Each letter represents the starting letter of the title of a book in the initial heap.

It is guaranteed that the sum of n over all test cases does not exceed 1000.

Output
For each test case, output a string of k letters which is the most optimal string that Ela can find.

Input:
5
12 3
cabccadabaac
12 6
cabccadabaac
12 12
cabccadabaac
25 1
abcdefghijklmnopqrstuvwxy
10 5
bcdxedbcfg

Output:
edb
ccbbba
bbbbbaaaaaaa
z
aaaaa
"""
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    seg_len = n // k

    # Count only 'a'..'y' (25 letters)
    cnt = [0] * 25
    for ch in s:
        cnt[ord(ch) - ord('a')] += 1

    ans = []

    for _ in range(k):
        need = seg_len
        j = 0

        # Try to place one of 'a', then one of 'b', etc.
        while j < 25 and need > 0 and cnt[j] > 0:
            cnt[j] -= 1
            need -= 1
            j += 1

        if j == 25:
            ans.append('z')
        else:
            ans.append(chr(ord('a') + j))

    print("".join(ans))