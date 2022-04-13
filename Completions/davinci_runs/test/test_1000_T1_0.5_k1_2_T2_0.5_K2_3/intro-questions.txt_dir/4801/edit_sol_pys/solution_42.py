

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    lis = []
    lis.append(a[0])
    for i in range(1, n):
        if a[i] > lis[-1]:
            lis.append(a[i])
    print(len(lis))
    print(' '.join(lis))

if __name__ == "__main__":
    main()
