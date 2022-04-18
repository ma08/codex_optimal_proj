

def main():
    n, s, r = map(int, input().split())
    damaged = list(map(int, input().split()))
    reserve = list(map(int, input().split()))
    count = 0
    if len(damaged) == 0:
        print(0)
        return
    if len(reserve) == 0:
        print(len(damaged))
        return
    damaged.sort()
    reserve.sort()
    for i in range(len(damaged)):
        if damaged[i] - 1 in reserve:
            reserve.remove(damaged[i]-1)
            damaged.remove(damaged[i])
            i -= 1
        elif damaged[i] + 1 in reserve:
            reserve.remove(damaged[i]+1)
            damaged.remove(damaged[i])
            i -= 1
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
