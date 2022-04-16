

def main():
    n = int(input())
    permutation = list(map(int, input().split()))

    gis = [permutation[0]]

        else:
            for j in range(len(gis)):
                if gis[j] >= permutation[i]:
                    gis[j] = permutation[i]
                    break
    for i in range(1, n):
        if gis[-1] < permutation[i]:
            gis.append(permutation[i])

    print(len(gis))
    print(*gis)

if __name__ == '__main__':
    main()
