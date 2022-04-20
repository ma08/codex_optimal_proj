def main():
    n, k = map(int, raw_input().split())
    edges = {}
    for i in range(n-1):
        a, b = map(int, raw_input().split())
        if a in edges:
            edges[a].append(i+1)
        else:
            edges[a] = [i+1]
        if b in edges:
            edges[b].append(i+1)
        else:
            edges[b] = [i+1]
    counts = {}
    for i in edges.keys():
        counts[i] = len(edges[i])
    r = 0
    print(edges)
    while counts:
        r += 1
        for i in counts.keys():
            if counts[i] == 1:
                del counts[i]
                print(i, edges[i])
                break
            else:
                counts[i] -= 1
    print(r)
    print(" ".join([str(i%r+1) for i in range(n-1)]))


if __name__ == "__main__":
    main()
