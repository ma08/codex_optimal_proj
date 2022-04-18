

import sys

# TODO: Finish this.

def main():
    line = sys.stdin.readline().split()
    N = int(line[0])
    L = int(line[1])
    drawers = [[] for _ in range(L)]
    for _ in range(N):
        line = sys.stdin.readline().split()
        drawers[int(line[0]) - 1].append(int(line[1]) - 1)
        drawers[int(line[1]) - 1].append(int(line[0]) - 1)
    move_count = 0
    while True:
        move_count += 1
        for drawer in drawers:
            if len(drawer) == 2:
                if len(drawers[drawer[0]]) > 1 and len(drawers[drawer[1]]) > 1:
                    drawers[drawer[0]].remove(drawer[1])
                    drawers[drawer[1]].remove(drawer[0])
                    drawers[drawer[0]].append(drawer[0])
                    drawers[drawer[1]].append(drawer[1])
                    break
            elif len(drawer) == 1:
                for other in drawers[drawer[0]]:
                    if len(drawers[other]) == 1:
                        drawers[other].append(other)
                        drawers[drawer[0]].remove(other)
                        break
                else:
                    break
        else:
            break
    for drawer in drawers:
        if len(drawer) == 2:
            print("LADICA")
        else:
            print("SMECE")

if __name__ == "__main__":
    main()