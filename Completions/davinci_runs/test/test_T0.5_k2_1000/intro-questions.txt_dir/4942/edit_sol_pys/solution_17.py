import sys

def main():
    n = int(sys.stdin.readline())
    t = list(map(int, sys.stdin.readline().split())) # split()で文字列を分割して、map()でint型に変換してリストに格納
    t.sort()
    print(sum(t[i] * (n - i) for i in range(n)))

main()
