

def intersection(segments):
    segments.sort()
    start = segments[0][0]
    finish = segments[0][1]
    for i in range(1, len(segments)):
        if segments[i][0] <= finish:
            finish = max(finish, segments[i][1])
        else:
            return finish - start
    return finish - start

def main():
    n = int(input())
    segments = []
    for _ in range(n):
        segments.append(list(map(int, input().split())))
    max_intersection = 0
    for i in range(n):
        inter = intersection(segments[:i] + segments[i+1:])
        if inter > max_intersection:
            max_intersection = inter
    print(max_intersection)

if __name__ == '__main__':
    main()