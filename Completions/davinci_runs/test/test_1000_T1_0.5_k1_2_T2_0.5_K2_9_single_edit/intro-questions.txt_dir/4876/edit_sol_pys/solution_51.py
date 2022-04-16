#space-O(n)

n = int(input())




def find(n):
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
                        break
                break


find(n)
