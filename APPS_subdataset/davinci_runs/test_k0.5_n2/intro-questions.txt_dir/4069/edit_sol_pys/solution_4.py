

def main():
    x, k, d = map(int, input().split())
    if k >= abs(x) // d and x >= 0:
        print(abs(x) - k * d if abs(x) - k * d >= 0 else abs(x) - k * d + 2 * d)
    else:
        print(abs(x) - (abs(x) // d) * d if abs(x) - (abs(x) // d) * d >= 0 else abs(x) - (abs(x) // d) * d + 2 * d)


if __name__ == '__main__':
    main()
