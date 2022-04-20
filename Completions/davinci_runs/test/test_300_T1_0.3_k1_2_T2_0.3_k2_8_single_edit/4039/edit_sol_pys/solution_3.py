

def main():
    n, r = map(int, input().split())
    projects = [list(map(int, input().split())) for _ in range(n)]
    projects.sort(key=lambda x: x[0])
    for project in projects:
        if r < project[0]:
            print("NO")
            return
        r += project[1]
        if r < 0:
            print("NO")
            return
    print("YES")

main()
