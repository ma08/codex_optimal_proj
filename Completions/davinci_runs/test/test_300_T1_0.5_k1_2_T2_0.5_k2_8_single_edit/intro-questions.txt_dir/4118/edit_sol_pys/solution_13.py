

def func(a):
    if a == 2 or a == 3 or a == 5 or a == 7:
        return True
    else:
        return False


def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print(a*b)
    else:
        if func(a) and func(b):
            print(a*b)
        else:
            print(-1)

if __name__ == '__main__':
    main()
