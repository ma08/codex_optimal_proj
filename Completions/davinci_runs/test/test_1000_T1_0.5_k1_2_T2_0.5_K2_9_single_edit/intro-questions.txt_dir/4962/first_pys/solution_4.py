

def main():
    n, l = map(int, input().split())
    drawers = [None] * l
    for _ in range(n):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if drawers[a] is None:
            drawers[a] = b
            print('LADICA')
        elif drawers[b] is None:
            drawers[b] = a
            print('LADICA')
        else:
            visited = set()
            while True:
                if drawers[a] is None:
                    drawers[a] = b
                    print('LADICA')
                    break
                elif drawers[b] is None:
                    drawers[b] = a
                    print('LADICA')
                    break
                elif (a, b) in visited:
                    print('SMECE')
                    break
                else:
                    visited.add((a, b))
                    a, b = drawers[a], drawers[b]


if __name__ == '__main__':
    main()