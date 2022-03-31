

def main():
    n = int(input())
    a = input()  # a is a string, not a list
    f = list(map(int, input().split()))

    res = 0
    for i in range(n):
        res = res * 10 + f[int(a[i]) - 1]  # a[i] is a string, not a list

    print(res)

if __name__ == "__main__":
    main()
