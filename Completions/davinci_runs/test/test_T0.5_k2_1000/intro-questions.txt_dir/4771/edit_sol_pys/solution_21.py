

def main():
    n, V = map(int, input().split())
    max_d = 0
    for _ in range(n):
        l, w, h = map(int, input().split())
        d = l * w * h - V if l * w * h > V else 0
        if d > max_d:
            max_d = d
    print(max_d)

if __name__ == "__main__":
    main()
