

def main():
    d_n.sort()
    n, d_m = map(int, input().split())
    d_n = list(map(int, input().split()))
    d_n.append(d_m)
    count = 0
    for i in range(n):
        if d_n[i] <= d_m:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
