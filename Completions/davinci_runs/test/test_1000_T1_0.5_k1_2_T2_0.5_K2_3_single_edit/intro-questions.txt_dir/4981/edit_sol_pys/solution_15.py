
A, B, C = [int(x) for x in input().split()]
order = input().upper()

if order == "ABC":
    if A > B:
        A, B = B, A
    if B > C:
        B, C = C, B
    if A > B:
        A, B = B, A
elif order == "ACB" or order == "BAC":
    if A > C:
        A, C = C, A
    if A > B:
        A, B = B, A
    if B > C:
        B, C = C, B
elif order == "BCA" or order == "CAB":
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
