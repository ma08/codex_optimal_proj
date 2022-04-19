

def main():
    n, k = map(int, input().split())
    if k == 0:
        print(n)
        return
    s = input()
    cost = 0
    for i in range(n):
        if s[i] == '0':
            cost += i + 1
        else:
            cost += min(i + 1, n - i)
    print(cost)

if __name__ == "__main__":
    main()
