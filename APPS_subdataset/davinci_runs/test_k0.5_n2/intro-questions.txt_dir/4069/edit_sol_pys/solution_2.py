
def main():
    x, k, d = map(int, input().split())
    if k >= abs(x)//d:
        print(abs(x) - k*d)
    else:
        print(abs(x) - (abs(x)//d)*d)


if __name__ == '__main__':
    main()
