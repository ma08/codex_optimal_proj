

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if len(set(a)) < k:
        print("NO")
        return

    colors = [1] * n
    for i in range(1, n):
        if a[i] == a[i-1]:
            colors[i] = colors[i-1]
        else:
            colors[i] = colors[i-1] + 1

    print("YES")
    print(" ".join(map(str, colors)))

if __name__ == '__main__':
    main()