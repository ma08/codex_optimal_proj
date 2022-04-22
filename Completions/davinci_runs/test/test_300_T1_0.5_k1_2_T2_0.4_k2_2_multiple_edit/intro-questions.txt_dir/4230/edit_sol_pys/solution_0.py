
x = int(input()) # 크레인 위치
n = int(input()) # 박스 개수
p = list(map(int, input().split())) # 박스 위치

p.sort() # 박스 위치 정렬

if x < p[0]: # 크레인 위치가 가장 왼쪽 박스보다 왼쪽에 있을 경우
    print(p[0] - x)
elif x > p[n-1]: # 크레인 위치가 가장 오른쪽 박스보다 오른쪽에 있을 경우
    print(x - p[n-1])
else: # 크레인 위치가 박스 사이에 있을 경우
    for i in range(1, n):
        if p[i-1] < x and x < p[i]: # 크레인 위치가 박스 사이에 있을 경우
            if abs(p[i-1] - x) < abs(p[i] - x): # 왼쪽 박스와의 거리가 오른쪽 박스와의 거리보다 작을 경우
                print(p[i-1] - x)
            else: # 오른쪽 박스와의 거리가 왼쪽 박스와의 거리보다 작을 경우
                print(p[i] - x)
            break
