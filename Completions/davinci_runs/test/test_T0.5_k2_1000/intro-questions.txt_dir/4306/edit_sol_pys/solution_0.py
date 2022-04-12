# 백준 알고리즘 1037번 문제
# https://www.acmicpc.net/problem/1037

a, b, c, d = map(int, input().split()) # a, b, c, d 각각 입력받음
if c < a: # c가 a보다 작을 때
    if d <= a: # d가 a보다 작거나 같을 때
        print(0) # 0 출력
    elif d <= b: # d가 a보다 크고 b보다 작거나 같을 때
        print(d - a) # d - a 출력
    else: # d가 b보다 클 때
        print(b - a) # b - a 출력
elif c < b: # c가 a보다 크고 b보다 작을 때
    if d <= b: # d가 b보다 작거나 같을 때
        print(d - c) # d - c 출력
    else: # d가 b보다 클 때
        print(b - c) # b - c 출력
else: # c가 b보다 클 때
    print(0) # 0 출력
