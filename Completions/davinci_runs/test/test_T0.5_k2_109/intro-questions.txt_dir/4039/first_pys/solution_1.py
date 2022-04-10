

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        projects.append(list(map(int, input().split())))
    projects.sort(key=lambda x: x[0])
    for a, b in projects:
        if r < a:
            print("NO")
            return
        else:
            r += b
    print("YES")

if __name__ == '__main__':
    main()