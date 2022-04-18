

def soda(e,f,c): #e is empty bottles, f is full bottles, c is cost of soda
    bottles = e + f #total bottles
    drinks = 0
    while bottles >= c:
        drinks += 1
        bottles -= c
        bottles += 1
    return drinks

if __name__ == "__main__":
    e,f,c = map(int,input().split()) #input e,f,c
    print(soda(e,f,c))
