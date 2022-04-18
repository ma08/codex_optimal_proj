

N, L = map(int, input().split())

drawers = [None] * L

for _ in range(N):
    A, B = map(int, input().split())
    if drawers[A - 1] is None:
        drawers[A - 1] = 1
        print("LADICA")
    elif drawers[B - 1] is None:
        drawers[B - 1] = 1
        print("LADICA")
    else:
        i = A - 1
        seen = set()
        while i != B - 1 and i not in seen:
            seen.add(i)
            if drawers[i] == 1:
                i = drawers[i]
            else:
                i = drawers[i]
        if i == B - 1:
            print("SMECE")
        else:
            drawers[i] = 1
            print("LADICA")