
N, X = map(int, input().split())

m_list = [0] * N
for i in range(N):
    m_list.append(int(input()))

m_list.sort()

num_donut_list = []
for i in range(N):
    num_donut_list.append(X // m_list[i])

print(sum(num_donut_list))
