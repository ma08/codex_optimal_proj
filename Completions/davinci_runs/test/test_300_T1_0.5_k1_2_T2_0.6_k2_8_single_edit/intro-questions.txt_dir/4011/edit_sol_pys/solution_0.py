

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    f = [0] + f

    a = str(a)

    for i in range(len(a)):
        a = a.replace(str(i), str(f[i]))

    print(a)

if __name__ == '__main__':
    main()
