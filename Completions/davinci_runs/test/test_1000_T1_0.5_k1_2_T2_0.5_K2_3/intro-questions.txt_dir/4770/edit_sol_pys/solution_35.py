

N, M = map(int, input().split())
if N > M:
    print("Dr. Chaz needs", N - M, "more piece[s] of chicken!")
else:
    print("Dr. Chaz will have", M - N, "piece[s] of chicken left over!") 
