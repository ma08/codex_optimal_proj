
n = int(input())

def solution(x):
    i = 1 # 첫번째 행의 첫번째 열
    j = 1 # 첫번째 행의 두번째 열
    while i < x: # 행의 첫번째 열이 입력된 수보다 작을 때 까지 반복
        i += j # 행의 첫번째 열에 행의 두번째 열을 더함
        j += 1 # 행의 두번째 열에 1을 더함
    if i == x and (j % 2 == 1): # 행의 첫번째 열이 입력된 수와 같고 행의 두번째 열이 홀수일 때
        return 1
    else: # 그 외의 경우
        return 0

print(solution(n))
