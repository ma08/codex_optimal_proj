

def main(n, temps):
    n = n
    temps = temps

    max_temp = 0
    day = 0

    for i in range(n - 2):
        temp = max(temps[i], temps[i + 1], temps[i + 2])

        if temp > max_temp:
            max_temp = temp
            day = i + 1

    print(day, max_temp)

if __name__ == "__main__":
    n = int(input())
    temps = list(map(int, input().split()))

    main(n, temps)
