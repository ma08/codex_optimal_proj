
import sys

N = int(sys.stdin.readline())
costumes = set()  # set 은 중복되는 값을 제거해주는 자료구조
for _ in range(N):
    costumes.add(sys.stdin.readline().strip())

costumes = list(costumes)  # set 에서 list 형태로 변환
costumes.sort()  # 오름차순 정렬
for costume in costumes:
    print(costume)
