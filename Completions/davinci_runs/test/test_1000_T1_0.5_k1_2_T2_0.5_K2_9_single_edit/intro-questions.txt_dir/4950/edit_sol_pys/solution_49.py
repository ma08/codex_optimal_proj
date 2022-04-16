

def main():
    n = int(input())
    prev_t = 0
    prev_x = 0
    max_v = 0
    for i in range(n):
        t, x = [int(x) for x in input().split()]
        v = (x - prev_x) / (t - prev_t)
        if v > max_v:
            max_v = v
        prev_t = t
        prev_x = x
    print(int(max_v))

if __name__ == "__main__":
    main()
