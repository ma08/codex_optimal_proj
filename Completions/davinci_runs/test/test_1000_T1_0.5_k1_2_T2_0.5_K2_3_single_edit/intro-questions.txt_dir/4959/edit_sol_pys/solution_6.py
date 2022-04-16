

def soda(e, f, c):
    bottles = e + f # total number of bottles, including empties
    drinks = 0
    while bottles >= c: # while you have enough bottles to buy a new one
        drinks += 1
        bottles -= c
        bottles += 1
    return drinks

if __name__ == "__main__":
    e,f,c = map(int,input().split())
    print(soda(e,f,c))
