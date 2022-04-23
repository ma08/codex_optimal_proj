import sys

def main():
    n, r = map(int, input().split())
    tasks = []
    for i in range(n):
        tasks.append(list(map(int, input().split())))

    tasks.sort(key=lambda x: x[1])

    for i in range(n):
        if tasks[i][0] > r:
            print("NO")
            sys.exit()
        r += tasks[i][1]

    print("YES")

if __name__ == '__main__':
    main()
