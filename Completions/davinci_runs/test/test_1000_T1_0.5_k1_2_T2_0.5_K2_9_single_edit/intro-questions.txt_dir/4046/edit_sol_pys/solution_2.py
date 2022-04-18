

def get_input():
    n = int(input())
    q = [int(x) for x in input().split()]
    return n, q

def get_input2():
    n = int(input())
    q = [int(x) for x in input().split()]
    return n, q

def check_permutation(n, q):
    if len(q) != n - 1:
        return False
    if n == 1:
        return True
    for i in q:
        if abs(i) >= n:
            return False
    return True
def check_permutation2(n, q):
    if len(q) != n - 1:
        return False
    if n == 1:
        return True
    for i in q:
        if abs(i) >= n:
            return False
    return True


def create_permutation(n, q):
    if n == 1:
        return [1]
    p = [0] * n
    p[0] = q[0]
    p[1] = q[0] + q[1]
    for i in range(2, n):
        p[i] = p[i-1] + q[i-1]
    return p

def create_permutation2(n, q):
    if n == 1:
        return [1]
    p = [0] * n
    p[0] = q[0]
    p[1] = q[0] + q[1]
    for i in range(2, n):
        p[i] = p[i-1] + q[i-1]
    return p

def print_permutation(p):
    print(" ".join([str(x) for x in p]))

def print_permutation2(p):
    print(" ".join([str(x) for x in p]))

def main():
    n, q = get_input()
    if not check_permutation(n, q):
        print(-1)
        return
    p = create_permutation(n, q)
    print_permutation(p)

    n, q = get_input2()
    if not check_permutation2(n, q):
        print(-1)
        return
    p = create_permutation2(n, q)
    print_permutation2(p)

if __name__ == "__main__":
    main()
