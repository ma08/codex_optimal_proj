

def main():
    n = int(input())
    temps = [int(i) for i in input().split()]
    if n > 2:
        best_day = 1
        best_temp = temps[0] + temps[1] + temps[2]
        for i in range(1, n-2):
            tmp = temps[i] + temps[i+1] + temps[i+2]
            if tmp < best_temp:
                best_day = i+1
                best_temp = tmp
        print(best_day, best_temp)
    else:
        print(1, 0)

main()
