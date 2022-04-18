
N = int(input())
a = list(map(int, input().split()))

a.sort()

# a_iが小さい順に、それを更新するのが最適かどうかを判定する
ans = 0
for i in range(N):
    # a_iを更新して、a_i+1, a_i+2, ..., a_Nを更新する
    # 更新前のa_i+1, a_i+2, ..., a_Nの値を記憶しておく
    # 更新後のa_i+1, a_i+2, ..., a_Nの値と更新前の値を比較して、
    # 更新前の値が大きい場合は、それを更新しても最適解にはならない
    # その場合は、更新しなくても良い
    prev_a = a[i:]
    a[i] += 1
    for j in range(i+1, N):
        if a[j] < a[j-1]:
            a[j] = a[j-1]
    if a[N-1] < prev_a[-1]:
        a[i] = a[i] - 1
    else:
        ans += 1

print(ans)
