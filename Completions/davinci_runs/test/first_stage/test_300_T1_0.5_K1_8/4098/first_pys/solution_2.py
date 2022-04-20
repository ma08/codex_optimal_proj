

def main():
    n, k = map(int, input().split())
    students = sorted(map(int, input().split()))
    max_students = 0
    for i in range(k):
        max_students += sum(1 for s in students if s >= students[0] + i*5)
    print(max_students)

if __name__ == '__main__':
    main()