

def main():
    n = int(input())
    temps = [int(i) for i in input().split()]
    best_day = 0
    best_temp = temps[0]
    for i in range(1, n):
        if temps[i] < best_temp:
            best_day = i
            best_temp = temps[i]
    print(best_day+1)

main()
