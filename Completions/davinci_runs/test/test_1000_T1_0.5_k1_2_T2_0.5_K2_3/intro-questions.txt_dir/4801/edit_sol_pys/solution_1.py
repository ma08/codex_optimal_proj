

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    lis = []
    lis.append(a[0])
    for i in range(1, n):
        if a[i] > lis[-1]:
        else:
            for j in range(len(lis)):
                if lis[j] >= a[i]:
                    lis[j] = a[i]
                    break
            lis.append(a[i])
    print(len(lis))
    print(*lis)

if __name__ == "__main__":
    main()
