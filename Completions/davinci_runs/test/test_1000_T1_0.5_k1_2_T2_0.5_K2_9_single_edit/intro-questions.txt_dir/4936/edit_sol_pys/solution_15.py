

def main():
    n = int(input())
    t = list(map(int, input().split()))
    max_temp = t[0]
    max_day = 0
    for i in range(1, n-1):
        if max(t[i-1], t[i+1]) < max_temp:
            max_temp = max(t[i-1], t[i+1])
            max_day = i+1
    print(max_day, max_temp)

if __name__ == "__main__":
    main()
