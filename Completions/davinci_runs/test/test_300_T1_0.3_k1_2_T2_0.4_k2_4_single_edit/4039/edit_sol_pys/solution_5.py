

def main():
    n, r = map(int, input().split()) # n is the number of projects, r is the amount of money
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split()))) # a project is a list of two ints, the first is the cost, the second is the reward
    projects.sort(key=lambda x: x[1]) # sort the projects by reward
    for project in projects:
        if r >= project[0]:
            r += project[1]
            if r < 0:
                print("NO")
                return
    print("YES")

if __name__ == '__main__':
    main()
