

def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    a.sort()
    for i in a:
        print(i)
main()
