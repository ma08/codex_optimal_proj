n = int(input())

for i in range(n):
    k = int(input())
    name = ""
    for j in range(k):
        item = input()
        if j == 0:
            name = item
        if item == "pea soup":
            for l in range(k):
                item = input()
                if item == "pancakes":
                    print(name)
                    break
            name = "Anywhere is fine I guess"
            break
    print(name)
