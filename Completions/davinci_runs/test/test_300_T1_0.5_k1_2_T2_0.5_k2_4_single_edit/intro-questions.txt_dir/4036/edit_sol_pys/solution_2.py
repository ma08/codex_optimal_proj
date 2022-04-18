
def main():
    n, k = map(int, input().split())
    a = [1]
    for i in range(k - 1):
        a.append(2 * a[i])
    if(sum(a) == n):
        print("YES")
        print(" ".join(map(str, a)))
    else:
        print("NO")

if __name__ == "__main__":
    main()
