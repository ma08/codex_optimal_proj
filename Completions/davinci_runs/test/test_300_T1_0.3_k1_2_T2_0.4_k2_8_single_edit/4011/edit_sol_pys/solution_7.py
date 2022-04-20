

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))  # f[i] = j
    f_inv = [0] * 10  # f_inv[i] = j
    for i in range(10):
        f_inv[f[i]] = i
    a = [str(f_inv[int(a[i])]) for i in range(n)]
    print(''.join(a))

if __name__ == '__main__':
    main()
