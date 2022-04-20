

def main():
    n = int(input())
    a = input()
    f = [int(x) for x in input().split()]
    f_inv = [0 for x in range(10)]
    for i in range(1, 10):
        f_inv[f[i-1]] = i
    a = [int(x) for x in a]
    a_inv = [f_inv[x] for x in a]
    a_inv_str = "".join([str(x) for x in a_inv])
    a_str = "".join([str(x) for x in a])
    print(max(a_inv_str, a_str))

if __name__ == "__main__":
    main()