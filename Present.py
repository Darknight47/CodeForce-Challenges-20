"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/118/B -----------------------------------------

Vasya's birthday is approaching and Lena decided to sew a patterned handkerchief to him as a present. Lena chose digits from 0 to n as the pattern. 
The digits will form a rhombus. The largest digit n should be located in the centre. The digits should decrease as they approach the edges. 
For example, for n = 5 the handkerchief pattern should look like that:

          0
        0 1 0
      0 1 2 1 0
    0 1 2 3 2 1 0
  0 1 2 3 4 3 2 1 0
0 1 2 3 4 5 4 3 2 1 0
  0 1 2 3 4 3 2 1 0
    0 1 2 3 2 1 0
      0 1 2 1 0
        0 1 0
          0

Your task is to determine the way the handkerchief will look like by the given n.

Input
The first line contains the single integer n (2 ≤ n ≤ 9).

Output
Print a picture for the given n. You should strictly observe the number of spaces before the first digit on each line. 
Every two adjacent digits in the same line should be separated by exactly one space. There should be no spaces after the last digit at the end of each line.

Input:
2

Output:
    0
  0 1 0
0 1 2 1 0
  0 1 0
    0
"""
n = int(input())
arr = []
spaces = n * 2
num_range = 0
for i in range(n + 1):
    temp_nums = list(range(num_range + 1))
    if(i == n):
        spaces = 0
    temp = " " * spaces 
    for i in range(num_range + 1):
        temp += str(temp_nums[i]) + " "
    for j in range(num_range - 1, - 1, -1):
        temp += str(temp_nums[j]) + " "
    temp = temp.rstrip()
    arr.append(temp)
    spaces -= 2
    num_range += 1
for i in range(len(arr)):
    print(arr[i])
for j in range(len(arr) - 2, -1, -1):
    print(arr[j])