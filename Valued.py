"""

--------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/801/B -------------------------------------

You found a mysterious function f. The function takes two strings s1 and s2. These strings must consist only of lowercase English letters, and must be the same length.

The output of the function f is another string of the same length. The i-th character of the output is equal to the minimum of the i-th character of s1 and the i-th character of s2.

For example, f("ab", "ba") = "aa", and f("nzwzl", "zizez") = "niwel".

You found two strings x and y of the same length and consisting of only lowercase English letters. Find any string z such that f(x, z) = y, or print -1 if no such string z exists.

Input
The first line of input contains the string x.

The second line of input contains the string y.

Both x and y consist only of lowercase English letters, x and y have same length and this length is between 1 and 100.

Output
If there is no string z such that f(x, z) = y, print -1.

Otherwise, print a string z such that f(x, z) = y. If there are multiple possible answers, print any of them. The string z should be the same length as x and y and consist only of lowercase English letters.

Input:
ab
aa

Output:
ba
"""
x = input()
y = input()
ans = ""
ok = True
for i in range(len(x)):
    first = x[i]
    second = y[i]
    if(first < second):
        ok = False
        break
    if(first == second):
        ans += chr(min(ord(first) + 1, ord('z')))
    else:
        ans += second
print(ans if ok else -1)