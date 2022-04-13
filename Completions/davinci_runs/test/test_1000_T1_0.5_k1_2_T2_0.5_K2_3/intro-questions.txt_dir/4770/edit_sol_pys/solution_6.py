

n, m = map(int, input().split())
if n > m:
    print("Dr. Chaz needs", n-m, "more piece[s] of chicken!")  # printing the result
elif n < m:
    print("Dr. Chaz will have", m-n, "piece[s] of chicken left over!")  # printing the result
