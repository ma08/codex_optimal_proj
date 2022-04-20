

n = int(input())
for i in range(n):
    s = input()
    if len(s) != 26:
        print("No")
        continue
    else:
        s = sorted(s)
        if s == list("abcdefghijklmnopqrstuvwxyz"):
            print("Yes")
        else:
            print("No")