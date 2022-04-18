

def main():
    m, n = map(int, input().split())
    clauses = []
    for i in range(m):
        clauses.append(list(map(int, input().split())))
    if m < 8:
        print("unsatisfactory")
    else:
        print("satisfactory")

main()
