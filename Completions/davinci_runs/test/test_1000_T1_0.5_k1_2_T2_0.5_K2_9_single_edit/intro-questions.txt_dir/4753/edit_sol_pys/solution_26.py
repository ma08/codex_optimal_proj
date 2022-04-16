import sys
sys.stdin = open('input.txt', 'r')




n = int(sys.stdin.readline())

ans = (n - 3) * (n - 4) // 2

print(ans)
