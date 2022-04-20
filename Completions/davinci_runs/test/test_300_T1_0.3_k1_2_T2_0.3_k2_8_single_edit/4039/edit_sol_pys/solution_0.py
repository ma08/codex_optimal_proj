

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        projects.append(list(map(int, input().split())))
    projects.sort(key=lambda x: x[1])
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
