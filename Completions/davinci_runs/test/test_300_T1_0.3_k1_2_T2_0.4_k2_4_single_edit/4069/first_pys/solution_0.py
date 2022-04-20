

def main():
    x, k, d = map(int, input().split())
    if x < 0:
        x = -x
    if x >= k * d:
        print(x - k * d)
    else:
        k -= x // d
        x %= d
        if k % 2 == 0:
            print(x)
        else:
            print(d - x)

if __name__ == '__main__':
    main()