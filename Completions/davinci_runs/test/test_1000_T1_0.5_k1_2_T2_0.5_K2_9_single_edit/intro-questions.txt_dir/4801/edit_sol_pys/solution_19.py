
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    gis = []
    gis.append(a[0])  # first element is always included
    for i in range(1, n):
        if a[i] > gis[-1]:  # if current element is greater than the last element in gis
            gis.append(a[i])
    print(len(gis))
    print(*gis)

if __name__ == "__main__":
    main()
