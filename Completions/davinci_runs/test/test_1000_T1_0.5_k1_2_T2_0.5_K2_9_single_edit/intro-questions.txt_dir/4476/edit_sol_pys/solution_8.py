# 파일 이름 : 세 수.py
# 제작자 : 이소진
# 제작 날짜 : 2018년 2월 9일
# 제작 목적 : 가장 큰 수 구하기
# 사용언어 : 파이썬 3.6
# 풀이 방법 : 정렬

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    ans = 0
    if a < b:
        if (b - a) % 2 == 0:
            ans = 1
        else:
            ans = 2
    elif a > b:
        if (a - b) % 2 == 0:
            ans = 2
        else:
            ans = 1
    else:
        ans = 0
    print(ans)
