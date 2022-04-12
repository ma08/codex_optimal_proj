

def soda(e, f, c):
    bottles = e + f  # initial number of bottles
    drinks = 0
    while bottles >= c:  # while there are enough bottles to exchange for a drink
        drinks += 1
        bottles -= c  # exchange bottles for a drink
        bottles += 1  # get a bottle back
    return drinks

if __name__ == "__main__":
    e, f, c = map(int, input().split())
    print(soda(e, f, c))
