

# S, C, K = map(int, input().split())
# socks = list(map(int, input().split()))
# # print(socks)
# socks.sort()

# machines = 0

# while len(socks) > 0:
#     current_machine = []
#     current_machine.append(socks.pop(0))
#     while len(current_machine) < C and len(socks) > 0:
#         if abs(current_machine[-1] - socks[0]) <= K:
#             current_machine.append(socks.pop(0))
#         else:
#             break
#     machines += 1

# print(machines)

def solution(A, B):
    # write your code in Python 3.6
    A = A.split(" ")
    B = B.split(" ")
    A = [int(x) for x in A]
    B = [int(x) for x in B]
    A.sort()
    B.sort()
    print(A)
    print(B)
    a = 0
    b = 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            a += 1
        elif A[a] > B[b]:
            b += 1
        else:
            a += 1
            b += 1
            return 1
    return 0

A = "1 4 5"
B = "2 3 3"
print(solution(A, B))
