

def main():
    n,m = map(int,input().split())
    edges = []
    for _ in range(m):
        a,b = map(int,input().split())
        edges.append((a,b))
    print(n,m)
    print(edges)

if __name__ == '__main__':
    main()