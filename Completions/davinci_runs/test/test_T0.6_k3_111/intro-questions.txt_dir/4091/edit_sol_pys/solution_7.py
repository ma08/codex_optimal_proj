

import fileinput

def solve(n, k, a):
    t = []
    while len(a) > 0:
        t.append(sum(1 for i in range(k) if len(a) > 0 and a[i] == max(a)))
        a = a[t[-1]:]
    return t

def main():
    f = fileinput.input()
    n, k = map(int, f.readline().split())
    a = map(int, f.readline().split())
    t = solve(n, k, a)
    print(sum(max(a[i:i+t[j]]) for j in range(len(t)) for i in range(0, n, t[j])))
    print(" ".join(map(str, t)))

if __name__ == "__main__":
    main()
