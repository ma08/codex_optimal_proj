

# Use A to represent the number of 0s required in the first i bits
# Use B to represent the number of 1s required in the first i bits
# Use C to represent the number of transitions required in the first i bits
# Initially, A = a, B = b, C = 0
# At each step, we have 2 options for adding to the string:
# 1) Add 0: A -= 1, B remains the same, C += 1
# 2) Add 1: A remains the same, B -= 1, C += 1
# When adding 0 to the string, if A == 0, then there is no more 0s left to add, we have to add 1
# When adding 1 to the string, if B == 0, then there is no more 1s left to add, we have to add 0
# At each step, we choose the option that will give us C == x
# If C > x, then we need to add 0 to the string
# If C < x, then we need to add 1 to the string
# If C == x, then we have 2 options, we can add 0 or 1, but if A == 0, then we have to add 1
# If B == 0, then we have to add 0

def solve(a, b, x):
    A = a
    B = b
    C = 0
    for _ in range(a + b - 1):
        if C > x:
            A -= 1
            C += 1
        elif C < x:
            B -= 1
            C += 1
        else:
            if A == 0:
                B -= 1
                C += 1
            elif B == 0:
                A -= 1
                C += 1
            else:
                A -= 1
                C += 1
    ans = []
    for i in range(a + b - 1):
        if A > 0:
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
