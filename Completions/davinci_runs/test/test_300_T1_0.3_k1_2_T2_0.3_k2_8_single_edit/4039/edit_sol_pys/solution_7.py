

def main():
    n, r = map(int, input().split())  # n: number of projects, r: initial rating
    projects = []
    for i in range(n):
        projects.append(list(map(int, input().split())))  # [rating, difficulty]
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
