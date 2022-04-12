

def main():
    n = int(input())
    temps = [int(i) for i in input().split()]
    best_day = 0
    best_temp = sum(temps[0:3]) - 3
    for i in range(1, n-2):
        tmp = temps[i] + temps[i+1] + temps[i+2]
        if tmp < best_temp:
            best_day = i+1
            best_temp = tmp
    print(best_day, best_temp)

main()
