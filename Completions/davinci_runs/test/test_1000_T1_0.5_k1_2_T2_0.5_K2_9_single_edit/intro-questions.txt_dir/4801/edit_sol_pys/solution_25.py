
def main():
    n = int(input())
    permutation = list(map(int, input().split()))

    gis = [permutation[0]]

    for i in range(1, n):
        if permutation[i] > gis[-1]:
            gis.append(permutation[i])

    print(len(gis))
    print(*gis)

if __name__ == '__main__':
    main()
