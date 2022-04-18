

def main():
    n, c = map(int, input().split())  # input format: n c
    fruits = [int(x) for x in input().split()]  # input format: fruit1 fruit2 fruit3 ...
    eaten = 0
    for i in range(n):
        if fruits[i] <= c:
            c -= fruits[i]
            eaten += 1
    print(eaten)

if __name__ == "__main__":
    main()
