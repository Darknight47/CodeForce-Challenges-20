"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1008/A ---------------------------------

Vitya has just started learning Berlanese language. It is known that Berlanese uses the Latin alphabet. Vowel letters are "a", "o", "u", "i", and "e". Other letters are consonant.

In Berlanese, there has to be a vowel after every consonant, but there can be any letter after any vowel. 
The only exception is a consonant "n"; after this letter, there can be any letter (not only a vowel) or there can be no letter at all. 
For example, the words "harakiri", "yupie", "man", and "nbo" are Berlanese while the words "horse", "king", "my", and "nz" are not.

Help Vitya find out if a word s is Berlanese.

Input
The first line of the input contains the string s consisting of |s| (1 ≤ |s| ≤ 100) lowercase Latin letters.

Output
Print "YES" (without quotes) if there is a vowel after every consonant except "n", otherwise print "NO".

You can print each letter in any case (upper or lower).

Input:
sumimasen

Output:
YES
"""
vowels = ['a', 'o', 'u', 'i', 'e']
s = input()
ok = True
for i in range(len(s) - 1):
    first = s[i]
    second = s[i + 1]
    if(first != 'n' and first not in vowels):
        if(second not in vowels):
            ok = False
            break
if(s[-1] != 'n' and s[-1] not in vowels):
        ok = False
print("YES" if ok else "NO")