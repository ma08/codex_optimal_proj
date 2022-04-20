



def main():
    n, b, a = map(int, input().split())
    s = list(map(int, input().split()))

    b_charge = b
    a_charge = a
    max_count = 0
    for i in range(n):
        if s[i] == 1:
            if b_charge > 0:
                b_charge -= 1
                a_charge += 1
            elif a_charge > 0:
                a_charge -= 1
        else:
            if b_charge > 0:
                b_charge -= 1
            elif a_charge > 0:
                a_charge -= 1
            else:
                break
        max_count += 1

    print(max_count)


if __name__ == '__main__':
    main()