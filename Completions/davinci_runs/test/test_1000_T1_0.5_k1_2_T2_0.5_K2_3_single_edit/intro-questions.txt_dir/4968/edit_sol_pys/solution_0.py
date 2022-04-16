

def main():
    n, s, r = map(int, input().split())
    damaged = set(map(int, input().split()))
    reserve = set(map(int, input().split()))
    count = len(damaged)
    for i in range(1, n+1):
        if i in damaged:
            for j in range(i-1, i+2):
                if j in reserve:
                    reserve.remove(j)
                    break
    print(count)

if __name__ == '__main__':
    main()
