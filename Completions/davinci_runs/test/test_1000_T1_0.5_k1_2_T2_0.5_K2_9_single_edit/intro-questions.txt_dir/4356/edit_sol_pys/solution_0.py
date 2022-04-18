
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())  # split()로 문자열을 나누고 리스트로 리턴하고, map()으로 리스트를 순회하면서 int()로 정수형으로 변환한다.
A = []
for i in range(n):
    A.append(sys.stdin.readline().rstrip())  # rstrip()은 문자열의 맨 끝의 공백을 제거한다.
B = []
for i in range(m):
    B.append(sys.stdin.readline().rstrip())  # rstrip()은 문자열의 맨 끝의 공백을 제거한다.

for i in range(n - m + 1):  # 이중 for문을 이용해 원본 문자열을 순회한다.
    for j in range(n - m + 1):  # 이중 for문을 이용해 원본 문자열을 순회한다.
        match = True
        for k in range(m):  # 서브 문자열을 순회한다.
            if A[i + k][j:j + m] != B[k]:  # 이중 for문을 이용해 원본 문자열을 순회한다.
                match = False
                break
        if match:
            print("Yes")
            sys.exit()
print("No")  # 모든 경우를 순회했는데도 일치하는 부분이 없다면 No를 출력한다.
