

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    colors = {}
    for i in range(n):
        if a[i] in colors:
            colors[a[i]].append(i)
        else:
            colors[a[i]] = [i]
    if len(colors) > k:
        print("NO")
        return
    print("YES")
    used = set()
    for i in range(n):
        if a[i] not in used:
            used.add(a[i])
            print(a[i], end=" ")
        else:
            print(k, end=" ")
            k -= 1
    print()

if __name__ == "__main__":
    main()