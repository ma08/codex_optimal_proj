

A, B, C = map(int, input().split())
order = input()

if order == "ABC":
    if A > B:
        A, B = B, A
    if B > C:
        B, C = C, B
    if A > B:
        A, B = B, A
elif order == "ACB":
    if A > C:
        A, C = C, A
    if A > B:
        A, B = B, A
    if B > C:
        B, C = C, B
elif order == "BAC":
    if B > A:
        B, A = A, B
    if B > C:
        B, C = C, B
    if A > C:
        A, C = C, A
elif order == "BCA":
    if B > C:
        B, C = C, B
    if B > A:
        B, A = A, B
    if A > C:
        A, C = C, A
elif order == "CAB":
    if C > A:
        C, A = A, C
    if C > B:
        C, B = B, C
    if A > B:
        A, B = B, A
elif order == "CBA":
    if C > B:
        C, B = B, C
    if C > A:
        C, A = A, C
    if A > B:
        A, B = B, A

print(A, B, C)
