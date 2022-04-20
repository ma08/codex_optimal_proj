

def main():
    x, n = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]

    for i in range(n):
        if x <= p[i]:
            print(p[i] - x)
            break
        elif i == n - 1:
            print(x - p[i])

if __name__ == '__main__':
    main()