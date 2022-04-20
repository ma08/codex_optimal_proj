

def main():
    n = int(input())
    segments = []
    for i in range(n):
        segments.append(list(map(int, input().split())))
    segments.sort(key=lambda x: x[0])
    max_len = 0
    for i in range(n):
        if i == 0:
            max_len = max(max_len, segments[i][1] - segments[i][0])
        elif i == n-1:
            max_len = max(max_len, segments[i][1] - segments[i][0])
        else:
            max_len = max(max_len, segments[i-1][1] - segments[i-1][0], segments[i+1][1] - segments[i+1][0])
    print(max_len)

if __name__ == '__main__':
    main()
