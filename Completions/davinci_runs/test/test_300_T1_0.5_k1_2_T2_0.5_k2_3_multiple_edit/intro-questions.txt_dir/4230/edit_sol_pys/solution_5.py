
def solution(a, b, c, d):
    if a <= c and b >= d:
        return 0
    elif a <= c and b <= d:
        return d-b
    elif a >= c and b >= d:
        return a-c
    else:
        return a-c + d-b


if __name__ == '__main__':
    a = int(input().split()[0])
    b = int(input().split()[0])
    c = int(input().split()[0])
    d = int(input().split()[0])

    print(solution(a, b, c, d))
