

def main():
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    l = sorted(l)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if l[i] + l[j] + l[k] == m:
                    print('Yes')
                    return

    print('No')

if __name__ == "__main__":
    main()
