

def main():
    n = int(input())
    temps = [int(i) for i in input().split()]
    best_day = 0
    best_temp = sum(temps[0:4])
    for i in range(1, n-2):
        tmp = sum(temps[i:i+4])
        if tmp < best_temp:
            best_day = i
            best_temp = tmp
    print(best_day+1, best_temp)

main()
