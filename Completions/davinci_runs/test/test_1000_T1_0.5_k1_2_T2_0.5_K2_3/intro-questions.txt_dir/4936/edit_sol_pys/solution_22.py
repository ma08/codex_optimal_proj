import sys

def main():
    n = int(sys.stdin.readline())
    temps = [int(x) for x in sys.stdin.readline().split()]
    min_temp = max(temps[0], temps[n-1])
    min_day = 1
    for i in range(1, n-1):
        temp = max(temps[i], temps[i-1])
        if temp < min_temp:
            min_temp = temp
            min_day = i + 1
    print(min_day, min_temp)

if __name__ == "__main__":
    main()
