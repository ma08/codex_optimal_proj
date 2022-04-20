

def main():
    n = int(input())
    segments = []
    for i in range(n):
        segments.append([int(x) for x in input().split()])
    segments.sort(key=lambda x: x[0])
    print(max([segments[i][1] - segments[j][0] for i in range(n) for j in range(i + 1, n)]))

if __name__ == "__main__":
    main()