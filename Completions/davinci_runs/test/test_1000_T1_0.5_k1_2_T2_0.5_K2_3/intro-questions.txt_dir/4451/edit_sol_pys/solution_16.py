

def main():
    n = int(input())
    skills = list(map(int, input().split()))
    skills.sort()
    i = 0
    j = n - 1
    k = n
    while i < j - 1:
        while j - i > 1 and skills[j] - skills[i] >= k:
            j -= 1
        if skills[j] - skills[i] < k:
            k = skills[j] - skills[i]
        i += 1
    print(k)
    print(j - i)


if __name__ == '__main__':
    main()
