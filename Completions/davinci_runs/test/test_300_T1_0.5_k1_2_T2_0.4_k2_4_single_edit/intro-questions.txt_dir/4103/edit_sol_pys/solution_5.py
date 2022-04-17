

def main():
    n, b, a = map(int, input().split())  # n: number of switches, b: number of batteries, a: number of battery
    s = list(map(int, input().split()))  # s: list of switches
    ans = 0
    i = 0
    while i < n:
        if s[i] == 1:  # if the switch is on
            if a < b:  # if the number of battery is less than the number of battery
                a += 1  # increase the number of battery
            else:  # if the number of battery is equal to or more than the number of battery
                b += 1  # increase the number of battery
        if a > 0:
            a -= 1
            ans += 1
        elif b > 0:
            b -= 1
            ans += 1
        else:
            break
        i += 1
    print(ans)

if __name__ == "__main__":
    main()
