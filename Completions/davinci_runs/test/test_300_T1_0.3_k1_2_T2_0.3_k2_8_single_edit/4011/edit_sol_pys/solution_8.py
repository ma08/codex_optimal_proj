

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))  # f: list[int]
    f_inv = [0] * 10
    for i in range(1, 10):
        f_inv[f[i - 1]] = i
    a = [f_inv[int(a[i])] for i in range(n)]  # a: list[int]
    a = [str(a[i]) for i in range(n)]  # a: list[str]
    a = ''.join(a)  # a: str
    print(a)

if __name__ == '__main__':
    main()
