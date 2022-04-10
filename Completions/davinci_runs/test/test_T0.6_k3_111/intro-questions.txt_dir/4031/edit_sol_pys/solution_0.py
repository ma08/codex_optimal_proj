n = int(input())
a = [input() for _ in range(n)]


def print_ans(a):
    print("YES")
    for i in range(n):
        print(a[i])


def print_no():
    print("NO")


d = {}
for i in range(n):
    d[a[i]] = d.get(a[i], 0) + 1

if len(d) == 1:
    print_ans(a)
else:
    print_no()
