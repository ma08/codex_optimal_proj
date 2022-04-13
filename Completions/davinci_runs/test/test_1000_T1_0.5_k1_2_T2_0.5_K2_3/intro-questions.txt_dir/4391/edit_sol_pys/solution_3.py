
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

n,k = map(int, input().split())
temps = list(map(int, input().split())) #리스트로 변환


ans = 0
for i in range(n-k+1):
    avg = sum(temps[i:i+k]) / k
    ans = max(ans, avg)

print(ans)
