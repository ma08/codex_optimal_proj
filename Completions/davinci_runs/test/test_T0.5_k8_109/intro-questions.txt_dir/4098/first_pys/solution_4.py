

def main():
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    teams = [[a[0]]]
    for i in range(1, n):
        for j in range(len(teams)):
            if a[i] <= teams[j][-1] + 5:
                teams[j].append(a[i])
                break
            if j == len(teams) - 1:
                teams.append([a[i]])
                break
    for i in range(len(teams)):
        if len(teams[i]) > k:
            teams[i] = teams[i][:k]
    print(sum([len(x) for x in teams]))

if __name__ == "__main__":
    main()