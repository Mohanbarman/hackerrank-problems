students = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
    scores.append(score)

second_low_grade = list(set(scores))
second_low_grade.sort()
print(second_low_grade)