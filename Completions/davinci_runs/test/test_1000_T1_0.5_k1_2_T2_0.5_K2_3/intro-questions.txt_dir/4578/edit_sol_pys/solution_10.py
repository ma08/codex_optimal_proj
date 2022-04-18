
N, X = map(int, input().split())

m_list = []
for i in range(N):
    m_list.append(int(input()))

m_list.sort()

num_doughnut = 0
for m in m_list:
    num_doughnut += X // m

print(sum(num_doughnut_list))
