

def main():
    x, k, d = map(int, input().split())
    if abs(x) > k * d:
        print(abs(x) - k * d)
    else:
        if (abs(x) % d) + (k - (abs(x) // d)) * d < (k - (abs(x) // d)) * d
            print(abs(x) % d)
        else
            print(abs((k - (abs(x) // d)) * d - abs(x) % d))


if __name__ == '__main__':
    main()
