

def main():
    n = int(input())
    numbers = list(map(int, input().split()))

    gis = [numbers[0]]

    for i in range(1, n):
        if numbers[i] > gis[-1]:
            gis.append(numbers[i])

    print(len(gis))
    print(*gis)

if __name__ == '__main__':
    main()
