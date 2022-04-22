N, A, B = map(int, input().split())
 
if N == 1:
    if A == B:
        print(1)
    else:
        print(0)
else:
    if A > B:
        print(0)
    else:
        print((N-2)*B - (N-2)*A + 1)
