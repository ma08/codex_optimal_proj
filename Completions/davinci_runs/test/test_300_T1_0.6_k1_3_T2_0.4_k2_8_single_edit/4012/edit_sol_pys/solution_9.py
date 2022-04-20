

def main():
    t = int(input())
    for _ in range(t):
        a, b, c = [int(x) for x in input().split()]
        if a % b == 0:
            k = b // a
            k_ = c // b
            print(k + k_)
            print(1, a * k, b * k_)
        elif b % c == 0:
            k = c // b
            k_ = a // c
            print(k + k_)
            print(a * k, b * k, 1)
        else:
            print(1, a, b)


if __name__ == "__main__":
    main()
