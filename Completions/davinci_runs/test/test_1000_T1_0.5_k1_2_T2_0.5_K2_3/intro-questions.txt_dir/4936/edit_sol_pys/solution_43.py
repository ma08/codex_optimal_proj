

def main():
    n = int(input())
    temps = [int(i) for i in input().split()]
    best_day = 0
    best_temp = temps[0] + temps[1] + temps[2] + temps[3] - 1
    for i in range(1, n-3):
        tmp = temps[i] + temps[i+1] + temps[i+2] + temps[i+3]
        if tmp <= best_temp:
            best_day = i
            best_temp = tmp
    print(best_day+1, best_temp)

main()
