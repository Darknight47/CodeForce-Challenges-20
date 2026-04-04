"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/745/A -------------------------------------------

Hongcow is learning to spell! One day, his teacher gives him a word that he needs to learn to spell. Being a dutiful student, he immediately learns how to spell the word.

Hongcow has decided to try to make new words from this one. He starts by taking the word he just learned how to spell, 
and moves the last character of the word to the beginning of the word. He calls this a cyclic shift. He can apply cyclic shift many times. 
For example, consecutively applying cyclic shift operation to the word "abracadabra" Hongcow will get words "aabracadabr", "raabracadab" and so on.

Hongcow is now wondering how many distinct words he can generate by doing the cyclic shift arbitrarily many times. The initial string is also counted.

Input
The first line of input will be a single string s (1 ≤ |s| ≤ 50), the word Hongcow initially learns how to spell. The string s consists only of lowercase English letters ('a'–'z').

Output
Output a single integer equal to the number of distinct strings that Hongcow can obtain by applying the cyclic shift arbitrarily many times to the given string.

Input:
abcd

Output:
4
"""
s = input()
temp_set = set()
while s not in temp_set:
    temp_set.add(s)
    s = s[-1] + s[:-1]
print(len(temp_set))