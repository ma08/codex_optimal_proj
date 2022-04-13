

def main():
    m, n = map(int, raw_input().split())
    clauses = []
    for i in range(m):
        clauses.append(list(map(int, raw_input().split())))
    if m < 8 or n < 8:
        print("unsatisfactory")
    else:
        print("satisfactory")

if __name__ == "__main__":
    main()
