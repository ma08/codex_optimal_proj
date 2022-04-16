import math

N, X = map(int, input().split())

m_list = []
for i in range(N):
    m_list.append(int(input()))

m_list.sort()

print(math.ceil(X / m_list[0]))
