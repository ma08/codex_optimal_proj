

def soda(e, f, c):
    bottles = e + f  # Total bottles
    drinks = 0
    while bottles >= c:  # While bottles are greater than or equal to cost
        drinks += 1  # Add one drink
        bottles -= c  # Subtract cost from bottles
        bottles += 1  # Add one bottle
    return drinks

if __name__ == "__main__":
    e, f, c = map(int, input().split())
    print(soda(e, f, c))
