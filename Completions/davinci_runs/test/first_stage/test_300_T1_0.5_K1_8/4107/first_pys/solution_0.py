

def main():
    n, k = map(int, input().split())
    s = input()
    cost = 0
    for i in range(n):
        if s[i] == "1":
            cost += i + 1
            if i - k >= 0:
                s[i-k] = "0"
            if i + k < n:
                s[i+k] = "0"
    for i in range(n):
        if s[i] == "1":
            cost += i + 1
    print(cost)

if __name__ == "__main__":
    main()