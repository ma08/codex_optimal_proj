

N, M = map(int, input().split())

A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# print(N, M)
# print(A)
# print(B)

# Sort by A
sort_A = sorted(zip(A, B), key=lambda x: x[0])
# print(sort_A)

# Sort by B
sort_B = sorted(zip(A, B), key=lambda x: x[1])
# print(sort_B)

# Sort by A and B
sort_AB = sorted(zip(A, B), key=lambda x: (x[0], x[1]))
# print(sort_AB)

# Sort by B and A
sort_BA = sorted(zip(A, B), key=lambda x: (x[1], x[0]))
# print(sort_BA)

cost_1 = 0
cost_2 = 0
cost_3 = 0
cost_4 = 0

cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0

for i in range(N):
    # cost_1 += sort_A[i][0] * sort_A[i][1]
    # cost_2 += sort_B[i][0] * sort_B[i][1]
    # cost_3 += sort_AB[i][0] * sort_AB[i][1]
    # cost_4 += sort_BA[i][0] * sort_BA[i][1]

    if cnt_1 + sort_A[i][1] <= M:
        cnt_1 += sort_A[i][1]
        cost_1 += sort_A[i][0] * sort_A[i][1]
    else:
        cost_1 += sort_A[i][0] * (M - cnt_1)
        cnt_1 = M
        break

    if cnt_2 + sort_B[i][1] <= M:
        cnt_2 += sort_B[i][1]
        cost_2 += sort_B[i][0] * sort_B[i][1]
    else:
        cost_2 += sort_B[i][0] * (M - cnt_2)
        cnt_2 = M
        break

    if cnt_3 + sort_AB[i][1] <= M:
        cnt_3 += sort_AB[i][1]
        cost_3 += sort_AB[i][0] * sort_AB[i][1]
    else:
        cost_3 += sort_AB[i][0] * (M - cnt_3)
        cnt_3 = M
        break

    if cnt_4 + sort_BA[i][1] <= M:
        cnt_4 += sort_BA[i][1]
        cost_4 += sort_BA[i][0] * sort_BA[i][1]
    else:
        cost_4 += sort_BA[i][0] * (M - cnt_4)
        cnt_4 = M
        break

print(cost_1)
print(cost_2)
print(cost_3)
print(cost_4)