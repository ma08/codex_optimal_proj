
def main():
    a, b, c = map(int, input().split())
    if b + c <= a:
        print(0)
    elif b + c > a:
        print(b + c - a)
if __name__ == '__main__':
    main()
