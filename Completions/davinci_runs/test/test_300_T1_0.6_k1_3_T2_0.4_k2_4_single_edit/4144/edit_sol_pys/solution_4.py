import sys
def main():
    N = int(sys.stdin.readline()) # 테스트 케이스 개수
    for i in range(N):
        M, K = map(int, sys.stdin.readline().split()) # 각 테스트 케이스의 첫 번째 줄에 M과 K가 주어짐
        for j in range(K):
            data = list(map(int, sys.stdin.readline().split())) # 각 테스트 케이스의 두 번째 줄에는 K개의 정수가 주어짐
            data.sort()
            print(data)


if __name__ == "__main__":
    main()
