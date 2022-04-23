
import sys

S, W = map(int, sys.stdin.readline().split())  # 강수량과 낙뢰 발생여부

if S <= W:  # 강수량이 낙뢰 발생여부보다 작을 때
    print("unsafe")
else:
    print("safe")
