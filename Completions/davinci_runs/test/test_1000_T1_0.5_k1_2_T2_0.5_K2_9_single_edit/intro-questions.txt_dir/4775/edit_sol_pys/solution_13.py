
a, b = input().split()

for i in range(len(b)):
    if b[i] in a:
        j = 0
        while j < len(a):
            if a[j] == b[i]:
                break
            j += 1
        break

for i in range(len(b)):
    if b[i] in a:
        print("."*j + b[i] + "."*(len(a)-j-1), end="")
    else:
        print("."*len(a))
