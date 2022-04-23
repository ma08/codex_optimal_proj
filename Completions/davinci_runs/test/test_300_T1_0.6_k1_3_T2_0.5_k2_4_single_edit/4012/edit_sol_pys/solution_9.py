

def main():
    t = int(input())
    for _ in range(t):
        a, b, c = [int(x) for x in input().split()]
        k = b // a
        k_ = c // b
        print(k + k_)
        print(1, a * k, b * k_)


if __name__ == "__main__":
    main()
