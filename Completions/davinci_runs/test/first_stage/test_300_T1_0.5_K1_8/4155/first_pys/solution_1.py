

def main():
    N = int(input())
    h = list(map(int, input().split()))

    count = 0
    while True:
        max_h = max(h)
        if max_h == 0:
            break
        for i in range(N):
            if h[i] == max_h:
                h[i] = 0
                count += 1
    print(count)

if __name__ == '__main__':
    main()