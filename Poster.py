"""

------------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/412/A ---------------------------------------------

The R1 company has recently bought a high rise building in the centre of Moscow for its main office. 
It's time to decorate the new office, and the first thing to do is to write the company's slogan above the main entrance to the building.

The slogan of the company consists of n characters, so the decorators hung a large banner, n meters wide and 1 meter high, divided into n equal squares. 
The first character of the slogan must be in the first square (the leftmost) of the poster, the second character must be in the second square, and so on.

Of course, the R1 programmers want to write the slogan on the poster themselves. To do this, they have a large (and a very heavy) ladder which was put exactly opposite the k-th square of the poster. 
To draw the i-th character of the slogan on the poster, you need to climb the ladder, standing in front of the i-th square of the poster. This action (along with climbing up and down the ladder) 
takes one hour for a painter. The painter is not allowed to draw characters in the adjacent squares when the ladder is in front of the i-th square because the uncomfortable position of the ladder 
may make the characters untidy. Besides, the programmers can move the ladder. In one hour, they can move the ladder either a meter to the right or a meter to the left.

Drawing characters and moving the ladder is very tiring, so the programmers want to finish the job in as little time as possible. 
Develop for them an optimal poster painting plan!

Input
The first line contains two integers, n and k (1 ≤ k ≤ n ≤ 100) — the number of characters in the slogan and the initial position of the ladder, correspondingly. 
The next line contains the slogan as n characters written without spaces. Each character of the slogan is either a large English letter, or digit, or one of the characters: '.', '!', ',', '?'.

Output
In t lines, print the actions the programmers need to make. In the i-th line print:

"LEFT" (without the quotes), if the i-th action was "move the ladder to the left";
"RIGHT" (without the quotes), if the i-th action was "move the ladder to the right";
"PRINT x" (without the quotes), if the i-th action was to "go up the ladder, paint character x, go down the ladder".
The painting time (variable t) must be minimum possible. If there are multiple optimal painting plans, you can print any of them.

Input:
2 2
R1

Output:
PRINT 1
LEFT
PRINT R
"""
n, k = map(int, input().split())
s = input()
right_side = n - k
left_side = k - 1
if(right_side < left_side):
    temp_dir = 'RIGHT'
    dir = 'LEFT'
else:
    temp_dir = 'LEFT'
    dir = 'RIGHT'
min_side = min(right_side, left_side)
for _ in range(min_side):
    print(temp_dir)
if(dir == 'LEFT'):
    for i in range(n - 1, -1, -1):
        print(f"PRINT {s[i]}")
        if(i != 0):
            print(dir)
else:
    for i in range(n):
        print(f"PRINT {s[i]}")
        if(i != n - 1):
            print(dir)