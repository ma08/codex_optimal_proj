
n = int(input())
recited = []

for i in range(n):
    recited.append(int(input()))

if len(recited) == recited[-1] and recited[-1] == 1:
    print("good job")
