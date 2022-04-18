

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    f = [0] + f

    a = list(map(lambda x: f[int(x)], a))


    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
