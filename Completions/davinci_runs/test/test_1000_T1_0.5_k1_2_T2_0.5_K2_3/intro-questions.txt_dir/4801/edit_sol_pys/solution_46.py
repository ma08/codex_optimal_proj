def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    gis = []
    gis.append(a[0]) # append first element to gis
    for i in range(1, n):
        if a[i] > gis[-1]: # if a[i] is greater than the last element of gis
            gis.append(a[i]) # append a[i] to gis
    print(len(gis))
    print(*gis)

if __name__ == "__main__":
    main()
