n = int(input())
flag = 0
for i in range(n):
    k = int(input())
    name = input()
    for j in range(k):
        item = input()
        if item == "pea soup":
            for l in range(k):
                item = input()
                if item == "pancakes":
                    print(name)
                    flag = 1
                    break;
            if flag == 1:
                break
    if flag == 1:
        break
if flag == 0:
    print("Anywhere is fine I guess")
