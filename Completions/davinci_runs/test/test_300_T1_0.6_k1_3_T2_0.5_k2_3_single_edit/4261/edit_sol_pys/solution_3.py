

a, b, c = map(int, input().split()) # a, b, c를 입력받고 int형으로 변환

while 1: # 무한루프
    if b + c <= a:
        print(0) # 조건이 만족하면 0을 출력
        break
    elif b + c > a:
        print(b + c - a) # 조건이 만족하면 출력
        break
