

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print(a*b)
    else:
        if a % 3 == 0 and b % 3 == 0:
            print(a * b // 9)
        elif a % 3 == 0 and b % 3 == 1:
            print(a * b // 9 + 1)
        elif a % 3 == 0 and b % 3 == 2:
            print(a * b // 9 + 2)
        elif a % 3 == 1 and b % 3 == 0:
            print(a * b // 9 + 1)
        elif a % 3 == 1 and b % 3 == 1:
            print(a * b // 9 + 2)
        elif a % 3 == 1 and b % 3 == 2:
            print(a * b // 9 + 3)
        elif a % 3 == 2 and b % 3 == 0:
            print(a * b // 9 + 2)
        elif a % 3 == 2 and b % 3 == 1:
            print(a * b // 9 + 3)
        elif a % 3 == 2 and b % 3 == 2:
            print(a * b // 9 + 4)

if __name__ == '__main__':
    main()
