

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
for i in range(1, l[-1] + 1):
    if i not in l:
        print(i)
else:

    print("good job")
