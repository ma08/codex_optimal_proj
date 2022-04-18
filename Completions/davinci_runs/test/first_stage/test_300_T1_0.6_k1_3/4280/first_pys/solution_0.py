


def main():
    n, k = map(int, raw_input().split())
    edges = {}
    for i in range(n-1):
        a, b = map(int, raw_input().split())
        if a in edges:
            edges[a].append(i)
        else:
            edges[a] = [i]
        if b in edges:
            edges[b].append(i)
        else:
            edges[b] = [i]
    counts = {}
    for i in edges.keys():
        counts[i] = len(edges[i])
    r = 0
    while counts:
        r += 1
        for i in counts.keys():
            if counts[i] == 1:
                del counts[i]
                break
            else:
                counts[i] -= 1
    print(r)
    print(" ".join([str(i%r+1) for i in range(n-1)]))


if __name__ == "__main__":
    main()