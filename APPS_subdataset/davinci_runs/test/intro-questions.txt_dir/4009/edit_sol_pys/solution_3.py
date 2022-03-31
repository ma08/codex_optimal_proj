
def main():
    n, x = map(int, input().split())
    num = input()
    if num[0] == '0':
        print(1)
    else:
        for i in range(x, n):
            if num[i] == '0':
                print(1)
                break
        else:
            print(0)

if __name__ == '__main__':
    main()
