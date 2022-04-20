

def main():
    n = int(input())
    testimonies = [None]*n
    for i in range(n):
        testimonies[i] = []
        a = int(input())
        for j in range(a):
            testimonies[i].append(list(map(int, input().split())))
    print(testimonies)
    honest_people = [0]*n
    for i in range(n):
        for testimony in testimonies[i]:
            if testimony[1] == 1:
                honest_people[testimony[0]-1] += 1
    print(max(honest_people))

if __name__ == '__main__':
    main()