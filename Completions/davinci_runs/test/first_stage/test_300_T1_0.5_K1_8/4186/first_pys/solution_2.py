

def main():
    n = int(input())
    skills = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if skills[i] == skills[j]:
                count += 1
                skills[i] = -1
                skills[j] = -1
                break
    print(sum(skills))

if __name__ == "__main__":
    main()