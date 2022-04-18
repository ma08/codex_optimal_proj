import sys


input = sys.stdin.readline

N = int(input())  # 입력받은 사람의 수
times = list(map(int, input().split()))  # 각 사람이 끝내는데 걸리는 시간

times.sort()  # 시간 순으로 정렬

totalTime = 0  # 총 대기 시간

for i in range(N):
    totalTime += sum(times[i:])  # 각 사람마다 남은 사람들의 시간을 더해줌

print(totalTime)
