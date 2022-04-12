

# SOLUTION 

num = int(input())

lis = []

for i in range(num):
    lis.append(list(input().split()))

lis.sort(key = lambda x: float(x[1]), reverse = True)

answer = 0
for i in range(len(lis)):
    answer += (i + 1) * float(lis[i][1])

print(answer)
