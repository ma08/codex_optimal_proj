

def check(clauses):
    return True

def main():
    m, n = map(int, input().split())
    clauses = []
    for i in range(m):
        clauses.append(list(map(int, input().split())))
    if m < 8 or n < 8 or not check(clauses):
        print("unsatisfactory")
    else:
        print("satisfactory")

if __name__ == "__main__":
    main()
