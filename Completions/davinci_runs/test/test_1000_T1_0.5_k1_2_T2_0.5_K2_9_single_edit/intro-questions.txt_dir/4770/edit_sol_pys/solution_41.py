
print(n, m)
n, m = map(int, input().split())

if n > m:
    print("Dr. Chaz needs", n-m, "more piece[s] of chicken!")
else:
    print("Dr. Chaz will have", m-n, "piece[s] of chicken left over!")
