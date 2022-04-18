

# Use A[i] to represent the number of 0s required in the first i bits
# Use B[i] to represent the number of 1s required in the first i bits
# Use C[i] to represent the number of transitions required in the first i bits
# Initially, A[0] = a, B[0] = b, C[0] = 0
# At each step, we have 2 options:
# 1) Add 0 to the string: A[i] = A[i-1] - 1, B[i] = B[i-1], C[i] = C[i-1] + 1
# 2) Add 1 to the string: A[i] = A[i-1], B[i] = B[i-1] - 1, C[i] = C[i-1] + 1
# When adding 0 to the string, if A[i-1] == 0, then there is no more 0s left to add, we have to add 1,
# and we have to increase C[i] by 2 instead of 1
# When adding 1 to the string, if B[i-1] == 0, then there is no more 1s left to add, we have to add 0,
# and we have to increase C[i] by 2 instead of 1
# At each step, we choose the option that will give us C[i] == x
# If C[i] > x, then we need to add 0 to the string, and we have to increase C[i] by 1
# If C[i] < x, then we need to add 1 to the string, and we have to increase C[i] by 1
# If C[i] == x, then we have 2 options, we can add 0 or 1, but if A[i-1] == 0, then we have to add 1,
# and we have to increase C[i] by 2 instead of 1
# If B[i-1] == 0, then we have to add 0, and we have to increase C[i] by 2 instead of 1

def solve(a, b, x):
    A = [a]
    B = [b]
    C = [0]
    for _ in range(a + b - 1):
        if C[-1] > x:
            A.append(A[-1] - 1)
            B.append(B[-1])
            C.append(C[-1] + 1)
        elif C[-1] < x:
            A.append(A[-1])
            B.append(B[-1] - 1)
            C.append(C[-1] + 1)
        else:
            if A[-1] == 0:
                A.append(A[-1])
                B.append(B[-1] - 1)
                C.append(C[-1] + 2)
            elif B[-1] == 0:
                A.append(A[-1] - 1)
                B.append(B[-1])
                C.append(C[-1] + 2)
            else:
                A.append(A[-1] - 1)
                B.append(B[-1])
                C.append(C[-1] + 1)
    ans = []
    for i in range(a + b - 1):
        if A[i] > 0:
            ans.append('0')
        else:
            ans.append('1')
    if ans[0] == '0':
        ans.append('1')
    else:
        ans.append('0')
    return "".join(ans)

a, b, x = map(int, input().split())
print(solve(a, b, x))
