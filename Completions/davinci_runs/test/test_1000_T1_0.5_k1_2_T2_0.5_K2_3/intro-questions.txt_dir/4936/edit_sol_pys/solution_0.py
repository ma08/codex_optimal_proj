
def main():
    n = int(input())
    t = list(map(int, input().split()))
    max_temp = 101
    max_day = 0
    for i in range(n-2):
        if max(t[i], t[i+2]) < max_temp:
            max_temp = max(t[i], t[i+2])
            max_day = i+1
    print(max_day, max_temp)

if __name__ == "__main__":
    main()
