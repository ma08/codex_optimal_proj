n = int(input())
a = list(map(int, input().split()))
disturbing = []
for i in range(1, n - 1):
    if a[i - 1] == a[i + 1] == 1 and a[i] == 0:
        disturbing.append(i)
print(len(disturbing))

'''
n = int(input())
a = list(map(int, input().split()))
disturbing = []
for i in range(1, n - 1):
    if a[i - 1] == a[i + 1] == 1 and a[i] == 0:
        disturbing.append(i)

print(len(disturbing))
'''
