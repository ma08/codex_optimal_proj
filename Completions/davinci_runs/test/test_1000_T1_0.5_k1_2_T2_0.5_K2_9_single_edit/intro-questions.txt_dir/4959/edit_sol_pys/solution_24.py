

def soda(e, f, c):
    bottles = e + f  # initial bottles
    drinks = 0  # initial drinks
    while bottles >= c:  # while bottles is greater than or equal to c
        drinks += 1  # increment drinks
        bottles -= c  # subtract c from bottles
        bottles += 1  # add one back to bottles
    return drinks  # return drinks

if __name__ == "__main__":
    e, f, c = map(int, input().split())
    print(soda(e, f, c))
