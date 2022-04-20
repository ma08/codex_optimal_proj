

def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]
    for i in a:
        b.append(b[-1] + i)
    if min(b) < 0:
        b = [i + abs(min(b)) for i in b]
    if max(b) > w:
        print(0)
    else:
        print(w - max(b) + 1)

if __name__ == "__main__":
    main()