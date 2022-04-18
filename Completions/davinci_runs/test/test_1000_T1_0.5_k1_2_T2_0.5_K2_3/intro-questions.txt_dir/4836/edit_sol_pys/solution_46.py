
def main():
    n, m = map(int, input().split())
    fruits = [int(x) for x in input().split()]
    eaten_fruits = 0
    for i in range(n):
        if fruits[i] <= m:
            m -= fruits[i]
            eaten_fruits += 1
    print(eaten_fruits)

if __name__ == "__main__":
    main()
