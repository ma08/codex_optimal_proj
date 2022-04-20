
import sys

def main():
    n, r = map(int, input().split()) # n projects and r resources
    projects = []
    for i in range(n):
        projects.append(list(map(int, input().split())))

    projects.sort(key=lambda x: x[1]) # sort by deadline

    for i in range(n):
        if projects[i][0] > r: # if the project requires more than the available resources
            print("NO")
            sys.exit()
        r += projects[i][1]
        if r < 0: # if there are negative resources
            print("NO")
            sys.exit()

    print("YES")

if __name__ == '__main__':
    main()
