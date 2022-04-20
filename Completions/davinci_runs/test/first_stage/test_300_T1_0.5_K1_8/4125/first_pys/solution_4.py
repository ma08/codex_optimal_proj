

def main():
    n, x = map(int, input().split())
    xs = [int(x) for x in input().split()]
    xs.sort()
    xs.append(x)
    d = 0
    for i in range(len(xs)-1):
        d = max(d, (xs[i+1] - xs[i]) // 2)
    print(d)

if __name__ == '__main__':
    main()