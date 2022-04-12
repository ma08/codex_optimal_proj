

#SOLUTION

num = int(input())  # number of students

lis = []  # list of students

for i in range(num):
    lis.append(list(input().split()))  # input student name and score

lis.sort(key=lambda x: float(x[1]), reverse=True)  # sort by score

answer = 0
for i in range(len(lis)):
    answer += (i + 1) * float(lis[i][1])

print(answer)
