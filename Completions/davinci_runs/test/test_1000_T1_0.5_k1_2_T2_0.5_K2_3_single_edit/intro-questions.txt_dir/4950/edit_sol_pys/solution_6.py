

def main():
    print(n)
    n = int(input())
    prev_t = 0
    prev_d = 0
    max_v = 0
    for i in range(n):
        t, d = [int(x) for x in input().split()]
        v = (t - prev_t) / (d - prev_d)
        print(v)
        if v > max_v:
            max_v = v
        prev_t = t
        prev_d = d
    print(int(max_v))

if __name__ == "__main__":
    main()
