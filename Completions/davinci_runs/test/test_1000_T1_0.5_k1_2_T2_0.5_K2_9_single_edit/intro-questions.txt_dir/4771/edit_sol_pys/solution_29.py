

def main():
    n, V = map(int, input().split())
    max_d = 0
    for _ in range(n):
        l, w, h = map(int, input().split())
        d = l * w * h
        if d > V and d > max_d:
            max_d = d - V
    print(max_d)

if __name__ == "__main__":
    main()
