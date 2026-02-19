"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/152/A ---------------------------------------------------

Vasya, or Mr. Vasily Petrov is a dean of a department in a local university. After the winter exams he got his hands on a group's gradebook.

Overall the group has n students. They received marks for m subjects. Each student got a mark from 1 to 9 (inclusive) for each subject.

Let's consider a student the best at some subject, if there is no student who got a higher mark for this subject. Let's consider a student successful, if there exists a subject he is the best at.

Your task is to find the number of successful students in the group.

Input
The first input line contains two integers n and m (1 ≤ n, m ≤ 100) — the number of students and the number of subjects, correspondingly. 
Next n lines each containing m characters describe the gradebook. Each character in the gradebook is a number from 1 to 9. Note that the marks in a rows are not sepatated by spaces.

Output
Print the single number — the number of successful students in the given group.


Input:
3 3
223
232
112

Output:
2
"""
n, m = map(int, input().split())
strings = []
for _ in range(n):
    strings.append(input())
matrix = [[int(ch) for ch in row] for row  in strings]
diction = {}
for i in range(m):
    for j in range(n):
        temp = matrix[j][i]
        temp_max = diction.get(i, 0)
        if(temp > temp_max):
            diction[i] = temp
ans = 0
for i in range(n):
    successful = False
    for j in range(m):
        temp_mark = matrix[i][j]
        temp_max = diction[j]
        if(temp_mark == temp_max):
            successful = True
            break
    if(successful):
        ans += 1
print(ans)