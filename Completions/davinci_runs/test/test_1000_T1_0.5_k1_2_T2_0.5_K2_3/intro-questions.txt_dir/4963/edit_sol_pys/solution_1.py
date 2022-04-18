

def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    l = [0] * n
    l[0] = 1
    for i in range(n - 1):
        l[l[i] + 1] = i + 2
    print(' '.join([str(x) for x in l]))

if __name__ == '__main__':
    main()
