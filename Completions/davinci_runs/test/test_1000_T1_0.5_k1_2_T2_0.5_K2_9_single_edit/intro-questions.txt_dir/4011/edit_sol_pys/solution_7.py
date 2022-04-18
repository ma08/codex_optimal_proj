

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    f = [0] + f

    for i in range(len(a)):
        a = a[:i] + str(f[int(a[i])]) + a[i + 1:]

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
