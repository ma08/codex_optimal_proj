

# A,B,K = map(int,input().split())

# if A>=K:
#     print(A-K,B)
# else:
#     if A+B>=K:
#         print(0,A+B-K)
#     else:
#         print(0,0)

# from sys import exit
# A,B,K = map(int,input().split())
# if A>=K:
#     print(A-K,B)
#     exit()
# if A+B>=K:
#     print(0,A+B-K)
#     exit()
# print(0,0)

A,B,K = map(int,input().split())
if A>=K:
    print(A-K,B)
elif A+B>=K:
    print(0,A+B-K)
else:
    print(0,0)