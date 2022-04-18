# coding: utf-8


n = int(input()) # n 값을 입력받음
l = list(map(int, input().split())) # l을 입력받는데 입력받은 값을 정수형으로 바꿔서 리스트로 넣음

cnt = 0 # cnt를 0으로 초기화
for i in range(n): # i를 0부터 n까지 반복
    for j in range(i+1, n): # j를 i+1부터 n까지 반복
        for k in range(j+1, n): # k를 j+1부터 n까지 반복
            if l[i] + l[j] > l[k] and l[i] + l[k] > l[j] and l[j] + l[k] > l[i]: # 조건에 맞는 경우
                cnt += 1 # cnt를 1씩 증가

print(cnt)
