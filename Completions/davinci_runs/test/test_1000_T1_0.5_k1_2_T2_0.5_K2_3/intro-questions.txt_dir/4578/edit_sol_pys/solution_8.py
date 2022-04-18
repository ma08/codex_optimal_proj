N, X = map(int, input().split())

m_list = []
for i in range(N):
    m_list.append(int(input()))

m_list.sort()

num_doughnut_list = []
for i in range(N):
    num_doughnut_list.append(X // m_list[i])

print(sum(num_doughnut_list))
