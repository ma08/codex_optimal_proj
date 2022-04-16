

n = int(input())

for i in range(n):
    k = int(input())
    flag = 0
    name = input()
    for j in range(k):
        item = input()
        if item == "pea soup" or item == "pancakes":
            for l in range(k-1):
                item = input()
                if item == "pancakes":
                    print(name)
                    flag = 1
                    break 
    if flag == 1:
        break
