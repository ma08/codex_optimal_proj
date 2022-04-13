
def main():
    n, a = map(int, input().split())
    w = list(map(int, input().split()))
    w.sort()
    i = 0
    while a > 0 and i < n:
        if a >= w[i]:
            a -= w[i]
            i += 1
        else:
            break
    print(i)

if __name__ == "__main__":
    main()
