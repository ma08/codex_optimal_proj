

def main():
    a, b, c = map(float, input().split())
    i, j, k = map(float, input().split())
    x = min(a/i, b/j, c/k)  # x is the minimum number of bottles we can fill
    print("{:.6f} {:.6f} {:.6f}".format(a-x*i, b-x*j, c-x*k))  # print the remaining amounts

main()
