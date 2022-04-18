

def main():
    h, w, n = map(int, input().split())
    bricks = list(map(int, input().split()))
    for i in range(n):
        if bricks[i] > w:
            print('NO')
            return None
    layers = [0] * h
    for i in range(n):
        for j in range(h):
            if layers[j] + bricks[i] <= w:
                layers[j] += bricks[i]
                break
            if j == h - 1:
                print('NO')
                return None
    print('YES')
    return None

if __name__ == "__main__":
    main()
