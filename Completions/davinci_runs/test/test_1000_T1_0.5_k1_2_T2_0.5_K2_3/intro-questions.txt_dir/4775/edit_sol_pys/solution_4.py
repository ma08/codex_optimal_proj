

a, b = input().split()  # input는 공백을 기준으로 나눠서 문자열로 받는다.
N, M = len(a), len(b)  # 문자열의 길이를 계산하는 함수

for i in range(M):  # M번 반복
    for j in range(N):  # N번 반복
        if a[j] == b[i]:  # 문자열의 길이를 계산하는 함수
            print(b[i], end='')  # 문자열의 길이를 계산하는 함수
        else:
            print('.', end='')
    print()
