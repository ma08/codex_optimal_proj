import math

a, b = map(int, input().split())

for i in range(1, a+1):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:  # math.floor()は小数点以下を切り捨てる
        print(i)
        exit()
print(-1)
