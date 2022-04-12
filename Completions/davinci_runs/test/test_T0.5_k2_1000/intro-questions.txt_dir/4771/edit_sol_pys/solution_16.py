
def main():
    n, V = map(int, input().split())
    max_v = -1
    for _ in range(n):
        l, w, h = map(int, input().split())
        v = l * w * h - V
        if v > max_v:
            max_v = v
    print(max_v)

if __name__ == "__main__":
    main()
