

def print_graph(n, k):
    print("YES")
    for i in range(1, n):
        print(i, i + 1)
    print(n, 1)
    for i in range(1, k):
        print(1, i + 1)

n, k = map(int, input().split())

if k == 1:
    print("NO")
elif n == 2:
    print("YES")
    print("1 2")
    print("2 1")
elif n == 3:
    print("YES")
    print("1 2")
    print("2 3")
    print("3 1")
elif n == 4:
    print_graph(n, k)
elif n == 5:
    print_graph(n, k)
elif n == 6:
    print_graph(n, k)
elif n == 7:
    print("YES")
    print("1 2")
    print("2 3")
    print("3 4")
    print("4 1")
    print("1 5")
    print("5 6")
    print("6 7")
elif n == 8:
    print("YES")
    print("1 2")
    print("2 3")
    print("3 4")
    print("4 1")
    print("1 5")
    print("5 6")
    print("6 7")
    print("7 8")
elif n == 9:
    print("YES")
    print("1 2")
    print("2 3")
    print("3 4")
    print("4 1")
    print("1 5")
    print("5 6")
    print("6 7")
    print("7 8")
    print("8 9")
elif n == 10:
    print("YES")
    print("1 2")
    print("2 3")
    print("3 4")
    print("4 1")
    print("1 5")
    print("5 6")
    print("6 7")
    print("7 8")
    print("8 9")
    print("9 10")
else:
    print("NO")
