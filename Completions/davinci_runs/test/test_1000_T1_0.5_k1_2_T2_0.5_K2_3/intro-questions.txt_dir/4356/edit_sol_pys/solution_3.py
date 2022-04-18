import sys

n, m = map(int, sys.stdin.readline().rstrip().split())  #n과 m을 공백을 기준으로 분리하여 정수형으로 변환하여 입력받는다.
A = []
for i in range(n):
    A.append(sys.stdin.readline().rstrip())  #문자열 A를 입력받는다.
B = []
for i in range(m):
    B.append(sys.stdin.readline().rstrip())  #문자열 B를 입력받는다.

for i in range(n - m + 1):  #문자열 A의 부분 문자열 중에서 문자열 B와 일치하는 것이 있으면 Yes를 출력하고 그렇지 않으면 No를 출력한다.
    for j in range(n - m + 1):
        match = True
        for k in range(m):
            if A[i + k][j:j + m] != B[k]:  #문자열 B의 길이만큼 반복문을 돌면서 일치하는지 확인한다.
                match = False
                break
        if match:
            print("Yes")
            sys.exit()  #일치하면 Yes를 출력하고 프로그램을 종료한다.
print("No")
