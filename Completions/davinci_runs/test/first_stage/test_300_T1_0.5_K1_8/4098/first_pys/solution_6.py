

def main():
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())

    sortedA = sorted(set(a))
    maxStudents = 0
    for i in range(len(sortedA) - k + 1):
        maxStudents = max(maxStudents, i + 1 + sum(map(lambda x: 1 if x < sortedA[i + k - 1] and x > sortedA[i] else 0, a)))
    print maxStudents

if __name__ == '__main__':
    main()