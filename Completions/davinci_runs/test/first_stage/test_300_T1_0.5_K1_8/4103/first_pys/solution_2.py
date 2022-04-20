

def main():
    n, b, a = map(int, input().split())
    s = list(map(int, input().split()))
    max_charge = b + a
    charge = b
    max_charge_used = 0
    for i in range(n):
        if s[i] == 1:
            if charge < max_charge:
                charge += 1
        if charge > 0:
            charge -= 1
            max_charge_used += 1
        else:
            break
    print(max_charge_used)

if __name__ == "__main__":
    main()