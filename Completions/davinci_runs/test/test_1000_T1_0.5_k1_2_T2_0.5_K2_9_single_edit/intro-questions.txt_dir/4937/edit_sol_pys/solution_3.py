def solve(n, a, e):
    e.sort()
    i = 0
    while a > 0 and i < n:
        if e[i] < a:
            a -= e[i]
            i += 1
        else:
            break
    return i
    

def main():
    n, a = [int(x) for x in input().split()]
    e = [int(x) for x in input().split()]
    print(solve(n, a, e))

if __name__ == "__main__":
    main()
