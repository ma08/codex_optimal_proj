

n = int(input())
recited = []

for i in range(n):
    recited.append(int(input()))

if len(recited) == recited[-1]:
    print("good job")
else:
    for i in range(1, recited[-1] + 1):
        if i not in recited:
            print(i)
        
