

def main():
    n = int(input())  # number of students
    a = list(map(int, input().split()))  # student's scores
    m = int(input())  # number of queries
    q = list(map(int, input().split()))  # query scores
    for query in q:
        print(a.count(query))

if __name__ == "__main__":
    main()
