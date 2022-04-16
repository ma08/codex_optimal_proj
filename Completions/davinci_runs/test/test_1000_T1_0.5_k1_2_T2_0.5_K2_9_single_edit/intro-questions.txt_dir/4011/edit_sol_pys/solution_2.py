

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split())) + [0]

    a = ''.join(map(str, map(lambda x: f[int(x)], a)))


    print(a)

if __name__ == '__main__':
    main()
