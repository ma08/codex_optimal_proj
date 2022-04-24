
# 수학 시험을 보는 동안 점수를 기록한 시험지가 있다.
# 이 시험지의 점수는 점수를 쓰고 난 뒤에 뒤집어서 쓰는 형태로 적혀있다.
# 예를 들어, 점수가 87점이라면 처음엔 87을 쓰고, 뒤집어서 78을 쓴다.
# 점수가 주어졌을 때, 시험지의 점수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 시험지의 점수가 주어진다. 점수는 항상 양의 정수이며, 100보다 작거나 같은 정수이다.
#
# 출력
# 시험지의 점수를 출력한다.
#
# 예제 입력 1
# 87
# 예제 출력 1
# 78
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

prices = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

total = 0
for i in range(K):
    total += prices[i]

print(total)
