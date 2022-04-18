
p = int(input())
x = int(input())
y = int(input())
k = int(input())
dep = 100 * x + y
for i in range(k):
    dep = dep * (100 + p) / 100
print(dep // 100, dep % 100)
