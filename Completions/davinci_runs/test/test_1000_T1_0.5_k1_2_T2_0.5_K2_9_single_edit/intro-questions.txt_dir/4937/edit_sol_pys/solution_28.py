

def main():
    n, a = map(int, input().split())
    e = sorted(list(map(int, input().split())))
    i = 0
    while a > 0 and i < n:
        if a >= e[i]:
            a -= e[i]
            i += 1
        else:
            break
    print(i)

if __name__ == "__main__":
    main()
