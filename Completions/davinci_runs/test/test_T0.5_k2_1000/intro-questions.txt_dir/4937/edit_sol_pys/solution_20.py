

def main():
    n, a = map(int, input().split())
    e = sorted(map(int, input().split()))
    i = 0
    while a > 0 and i < n:
        if e[i] < a:
            a -= e[i]
            i += 1
        else:
            break
    print(i)

if __name__ == "__main__":
    main()
