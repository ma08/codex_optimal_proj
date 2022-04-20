
# print(len([i for i in range(1, 10) if i % 2 == 1]))
# print(len([i for i in range(1, 10)]))

n = int(input())
print(len([i for i in range(1, n+1) if i % 2 == 1])/len([i for i in range(1, n+1)]))