

def main():
    n = int(input())
    s = input()
    left, right = 0, n - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            break
    if left >= right:
        print(n)
    else:
        cost = 0
        for i in range(n):
            if s[i] == '1':
                cost += i + 1
            else:
                cost += min(i + 1, n - i)
        print(cost)

if __name__ == "__main__":
    main()
