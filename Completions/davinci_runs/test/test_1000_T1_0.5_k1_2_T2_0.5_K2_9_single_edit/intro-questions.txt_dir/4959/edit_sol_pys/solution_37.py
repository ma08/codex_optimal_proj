

def soda(e, f, c):
    bottles = e+f
    total_drinks = 0
    while bottles >= c:  # while we have enough bottles to exchange
        total_drinks += 1
        bottles -= c
        bottles += 1
    return total_drinks

if __name__ == "__main__":
    e, f, c = map(int, input().split())
    print(soda(e, f, c))
