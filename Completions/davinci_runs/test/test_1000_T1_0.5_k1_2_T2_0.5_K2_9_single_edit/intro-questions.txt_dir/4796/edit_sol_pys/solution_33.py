

def main():
    a, b, c = map(int, input().split())
    i, j, k = map(int, input().split())
    x = min(a/i, b/j, c/k)
    print("{0:.6f} {1:.6f} {2:.6f}".format(a-x*i, b-x*j, c-x*k))

main()
