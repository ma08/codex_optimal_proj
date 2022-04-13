

def main():
    a, b, c = map(float, input().split())
    x, y, z = map(float, input().split())
    m = min(a/x, b/y, c/z)
    print("{:.6f} {:.6f} {:.6f}".format(a-m*x, b-m*y, c-m*z))

main()
