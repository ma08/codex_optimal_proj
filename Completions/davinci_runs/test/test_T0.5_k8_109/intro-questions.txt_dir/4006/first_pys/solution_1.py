

#-----------------------------my code-----------------------------
def f(x):
    while (x % 10 == 0):
        x = x // 10
    return x + 1

n = int(input())
s = set()
while (n not in s):
    s.add(n)
    n = f(n)
print(len(s))