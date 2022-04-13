

def main():
    n = int(input())
    prev_t = 0
    prev_s = 0
    max_a = 0
    for i in range(n):
        t, s = [int(x) for x in input().split()]
        a = (s - prev_s) / (t - prev_t)
        if a > max_a:
            max_a = a
        prev_t = t
        prev_s = s
    print(int(max_a))


if __name__ == "__main__":
    main()
