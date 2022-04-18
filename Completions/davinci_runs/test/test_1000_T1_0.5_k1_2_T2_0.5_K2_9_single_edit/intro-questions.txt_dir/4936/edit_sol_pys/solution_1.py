

def get_max_temp(t, i):
    max_temp = 100
    max_day = 0
    for j in range(i-1, i+2):
        if t[j] < max_temp:
            max_temp = t[j]
            max_day = j + 1
    return max_day, max_temp

def main():
    n = int(input())
    t = list(map(int, input().split()))
    if n == 2:
        print(1, min(t[0], t[1]))
    else:
        max_day, max_temp = get_max_temp(t, 0)
        for i in range(1, n-2):
            day, temp = get_max_temp(t, i)
            if temp > max_temp:
                max_day = day
                max_temp = temp
        print(max_day, max_temp)

if __name__ == "__main__":
    main()
