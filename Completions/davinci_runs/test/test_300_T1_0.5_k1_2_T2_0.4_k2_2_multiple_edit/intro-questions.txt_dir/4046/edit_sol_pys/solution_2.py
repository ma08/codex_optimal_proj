

#get input
def get_input():
    n = int(input())
    q = [int(x) for x in input().split()]
    return n, q
#check permutation
def check_permutation(n, q):
    if len(q) != n - 1:
        return False
    if n == 1:
        return True
    for i in q:
        if abs(i) >= n:
            return False
    return True
#create permutation
def create_permutation(n, q):
    if n == 1:
        return [1]
    p = [0] * (n + 1)
    p[0] = q[0]
    p[1] = q[0] + q[1]
    for i in range(2, n + 1):
        p[i] = p[i-1] + q[i-1]
    return p
#print permutation
def print_permutation(p):
    print(" ".join([str(x) for x in p]))

def main():
    n, q = get_input()
    if not check_permutation(n, q):
        print(-1)
        return
    p = create_permutation(n, q)
    print_permutation(p)

if __name__ == "__main__":
    main()
