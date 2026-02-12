"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1559/B -------------------------------------------------

As their story unravels, a timeless tale is told once again...

Shirahime, a friend of Mocha's, is keen on playing the music game Arcaea and sharing Mocha interesting puzzles to solve. 
This day, Shirahime comes up with a new simple puzzle and wants Mocha to solve them. 
However, these puzzles are too easy for Mocha to solve, so she wants you to solve them and tell her the answers. The puzzles are described as follow.

There are n squares arranged in a row, and each of them can be painted either red or blue.

Among these squares, some of them have been painted already, and the others are blank. You can decide which color to paint on each blank square.

Some pairs of adjacent squares may have the same color, which is imperfect. We define the imperfectness as the number of pairs of adjacent squares that share the same color.

For example, the imperfectness of "BRRRBBR" is 3, with "BB" occurred once and "RR" occurred twice.

Your goal is to minimize the imperfectness and print out the colors of the squares after painting.

Input
Each test contains multiple test cases.

The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases. Each test case consists of two lines.

The first line of each test case contains an integer n (1 ≤ n ≤ 100) — the length of the squares row.

The second line of each test case contains a string s with length n, containing characters 'B', 'R' and '?'. Here 'B' stands for a blue square, 'R' for a red square, and '?' for a blank square.

Output
For each test case, print a line with a string only containing 'B' and 'R', the colors of the squares after painting, which imperfectness is minimized. If there are multiple solutions, print any of them.

Input:
5
7
?R???BR
7
???R???
1
?
1
B
10
?R??RB??B?

Output:
BRRBRBR
BRBRBRB
B
B
BRRBRBBRBR
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = list(input())
    
    first_known = -1
    for i in range(sze):
        if(s[i] in ('R', 'B')):
            first_known = i
            break
    
    if(first_known == -1):
        for i in range(sze):
            if(i % 2 == 0):
                s[i] = 'R'
            else:
                s[i] = 'B'
        print(''.join(s))
        continue
    
    # filling forward
    for i in range(first_known + 1, sze):
        if(s[i] == '?'):
            if(s[i - 1] == 'R'):
                s[i] = 'B'
            else:
                s[i] = 'R'
    
    # filling backward
    for i in range(first_known - 1, -1, -1):
        if(s[i] == '?'):
            if(s[i + 1] == 'R'):
                s[i] = 'B'
            else:
                s[i] = 'R'
    print(''.join(s))