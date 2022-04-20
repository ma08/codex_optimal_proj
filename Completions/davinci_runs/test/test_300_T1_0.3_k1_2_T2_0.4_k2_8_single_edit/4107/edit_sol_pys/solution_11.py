

def main():
    n = int(input())
    s = input()
    cost = 0
    for i in range(n):
        if s[i] == 'W':
            cost += i + 1
        else:
            cost += min(i + 1, n - i)
    print(cost)

if __name__ == "__main__":
    main()
