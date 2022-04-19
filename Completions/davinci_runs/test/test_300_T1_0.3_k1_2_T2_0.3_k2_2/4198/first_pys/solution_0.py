

def main():
    a, b, x = map(int, input().split())
    if x < a:
        print(0)
    else:
        print(min(10 ** 9, (x - b) // a))

if __name__ == '__main__':
    main()