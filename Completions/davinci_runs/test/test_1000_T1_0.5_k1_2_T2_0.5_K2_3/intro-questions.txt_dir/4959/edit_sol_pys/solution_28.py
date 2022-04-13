

def soda(empty,full,cost):
    bottles = empty + full
    drinks = 0
    while bottles >= cost:
        drinks += 1
        bottles -= cost
        bottles += 1
    return drinks

if __name__ == "__main__":
    e,f,c = map(int,input().split())
    print(soda(e,f,c))
