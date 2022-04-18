

import sys

def main():
    N, L = map(int, sys.stdin.readline().split())
    drawers = [None for _ in range(L + 1)]
    for i in range(1, N + 1):
        A, B = map(int, sys.stdin.readline().split())
        if drawers[A] == None:
            drawers[A] = i
        elif drawers[B] == None:
            drawers[B] = i
        else:
            A_i = A
            A_i_moved = False
            B_i = B
            B_i_moved = False
            while True:
                if not A_i_moved:
                    A_i_moved = True
                    if drawers[A_i] == i:
                        print("SMECE")
                        break
                    if drawers[A_i] == None:
                        drawers[A_i] = i
                        print("LADICA")
                        break
                    if drawers[drawers[A_i]] == None:
                        drawers[drawers[A_i]] = i
                        print("LADICA")
                        break
                    A_i = drawers[A_i]
                elif not B_i_moved:
                    B_i_moved = True
                    if drawers[B_i] == i:
                        print("SMECE")
                        break
                    if drawers[B_i] == None:
                        drawers[B_i] = i
                        print("LADICA")
                        break
                    if drawers[drawers[B_i]] == None:
                        drawers[drawers[B_i]] = i
                        print("LADICA")
                        break
                    B_i = drawers[B_i]
                else:
                    print("SMECE")
                    break

if __name__ == "__main__":
    main()