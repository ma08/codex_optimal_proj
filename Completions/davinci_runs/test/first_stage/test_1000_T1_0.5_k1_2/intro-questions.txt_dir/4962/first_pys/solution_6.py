

#import sys
#import os

#sys.stdin = open(os.path.join(sys.path[0], 'in.txt'))

def main():
    n, l = map(int, input().split())
    drawers = [None] * l
    for i in range(n):
        a, b = map(int, input().split())
        if drawers[a - 1] is None:
            drawers[a - 1] = i + 1
        elif drawers[b - 1] is None:
            drawers[b - 1] = i + 1
        else:
            current = drawers[a - 1]
            next = drawers[current - 1]
            while next != current:
                if drawers[next - 1] is None:
                    drawers[next - 1] = i + 1
                    break
                current = next
                next = drawers[current - 1]
            else:
                current = drawers[b - 1]
                next = drawers[current - 1]
                while next != current:
                    if drawers[next - 1] is None:
                        drawers[next - 1] = i + 1
                        break
                    current = next
                    next = drawers[current - 1]
                else:
                    print("SMECE")
                    continue
        print("LADICA")

main()