

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        projects.append(list(map(int, input().split())))
    projects.sort(key=lambda x: x[0])  # sort by start time
    for project in projects:
        if r < project[0]:  # start time is later than current time
            print("NO")
            return
        r += project[1]
        if r < 0:  # current time is later than end time
            print("NO")
            return
    print("YES")

main()
