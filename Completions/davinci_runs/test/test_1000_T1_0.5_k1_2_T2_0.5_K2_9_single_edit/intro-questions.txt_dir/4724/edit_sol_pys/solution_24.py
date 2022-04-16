
import sys

r = int(sys.stdin.readline().rstrip()) #첫째 줄에 빨간 구슬의 개수 R, 파란 구슬의 개수 G, 구슬을 교환할 수 있는 횟수 P가 주어진다.
g = int(sys.stdin.readline().rstrip()) #(1 ≤ R, G ≤ 10, 0 ≤ P ≤ 100)
p = int(sys.stdin.readline().rstrip())

print(int(g + (g-r)/2))
