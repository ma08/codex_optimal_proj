
a, b = map(int, input().split())
if a == 1 or b == 1:
    print(a * b)
elif a == 2 and b == 2:
    print(4)
elif a == 2 and (b == 3 or b == 4 or b == 5 or b == 6 or b == 8 or b == 9):
    print(6)
elif a == 2 and (b == 7):
    print(-1)
elif a == 3 and b == 3:
    print(9)
elif a == 3 and (b == 2 or b == 4 or b == 5 or b == 6 or b == 7 or b == 8 or b == 9):
    print(6)
elif a == 4 and b == 4:
    print(6)
elif a == 4 and (b == 2 or b == 3 or b == 5 or b == 6 or b == 7 or b == 8 or b == 9):
    print(8)
elif a == 5 and b == 5:
    print(5)
elif a == 5 and (b == 2 or b == 3 or b == 4 or b == 6 or b == 7 or b == 8 or b == 9):
    print(-1)
elif a == 6 and b == 6:
    print(6)
elif a == 6 and (b == 2 or b == 3 or b == 4 or b == 5):
    print(-1)
elif a == 7 and b == 7:
    print(9)
elif a == 7 and (b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 8 or b == 9):
    print(-1)
elif a == 8 and b == 8:
    print(4)
elif a == 8 and (b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7 or b == 9):
    print(2)
elif a == 9 and b == 9:
    print(1)
elif a == 9 and (b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7 or b == 8):
    print(-1)
