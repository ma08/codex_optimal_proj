
def main():
    n, c = map(int, input().split()) # number of fruits, capacity
    fruits = [int(x) for x in input().split()] # list of fruits
    eaten = 0
    for i in range(n):
        if fruits[i] <= c:
            c -= fruits[i]
            eaten += 1
    print(eaten)

if __name__ == "__main__":
    main()
