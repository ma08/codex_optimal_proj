
def solution(n, m, matrix):
    pass


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solution(n, m, matrix))
