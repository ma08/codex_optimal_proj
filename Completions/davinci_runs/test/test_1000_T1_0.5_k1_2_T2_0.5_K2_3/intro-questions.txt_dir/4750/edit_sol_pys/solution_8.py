
def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in range(1, 1+n):
        if i not in d:
            print(i)
            break

if __name__ == "__main__":
    main()
