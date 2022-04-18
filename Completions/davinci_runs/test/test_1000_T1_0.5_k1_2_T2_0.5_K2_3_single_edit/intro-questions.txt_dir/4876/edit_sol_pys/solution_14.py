
n = int(input())

for i in range(n):
    k = int(input())
    name = ""
    for j in range(k):
        if j == 0:
            name = item
        item = input()
        if item == "pea soup":
            for l in range(k - 1):
                item = input()
                if item == "pancakes":
                    print(name)
                    break
            break
