A,B = map(int, input().split())
print(min(B-A, A+10-B))
# if A <= B:
#     print(min(B-A, A+10-B))
# else:
#     print(min(A-B, B+10-A))
