

#This is an implementation of the solution to the problem: https://codeforces.com/contest/1360/problem/D

def check_sorted(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True

def find_row_column(a):
    for i in range(len(a)):
        if a[i] == 1:
            return i
    return -1

def print_ans(r, c):
    print("YES")
    print(r)
    print(c)

def find_solution(a):
    r = ["0" for i in range(len(a))]
    c = ["0" for i in range(len(a[0]))]
    for i in range(len(a)):
        if a[i][0] == 1:
            r[i] = "1"
            for j in range(len(a[0])):
                a[i][j] ^= 1
    for i in range(len(a[0])):
        if a[0][i] == 1:
            c[i] = "1"
            for j in range(len(a)):
                a[j][i] ^= 1
    for i in range(len(a)):
        if not check_sorted(a[i]):
            return False
    for i in range(len(a[0])):
        if not check_sorted([a[j][i] for j in range(len(a))]):
            return False
    print_ans("".join(r), "".join(c))
    return True

def main():
    n, m = [int(i) for i in input().split(" ")]
    a = []
    for i in range(n):
        a.append([int(i) for i in input().split(" ")])
    if not find_solution(a):
        print("NO")

if __name__ == "__main__":
    main()