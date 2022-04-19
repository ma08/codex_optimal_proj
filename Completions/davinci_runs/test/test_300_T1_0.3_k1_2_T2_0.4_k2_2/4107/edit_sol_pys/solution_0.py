

def main():
    n, k = map(int, input().split())
    s = input()
    total_cost = 0
    for i in range(n):
        if s[i] == '1':  # if the character is 1
            total_cost += i + 1
        else:
            total_cost += min(i + 1, n - i)
    print(total_cost)

if __name__ == "__main__":
    main()
