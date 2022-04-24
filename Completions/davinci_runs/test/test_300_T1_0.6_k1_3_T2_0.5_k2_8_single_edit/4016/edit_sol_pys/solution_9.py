

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print(" ".join([str(x) for x in a]))

if __name__ == '__main__':
    main()
