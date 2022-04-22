

def main():
    n, m = map(int, input().split())  # n: number of students, m: number of problems
    a = list(map(int, input().split()))  # a: number of points for each problem

    if max(a) >= sum(a) / (4 * m):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
