

n, k = map(int, input().split())
s = input()

if k > n or k == 0:
    print(-1)  # 해당 조건이 없으면 종료
else:
    print(n - k)  # 입력된 값에서 k만큼 제거한 값을 출력
