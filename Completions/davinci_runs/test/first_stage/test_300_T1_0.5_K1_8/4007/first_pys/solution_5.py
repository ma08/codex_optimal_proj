

def main():
    n = int(input())
    f = list(map(int,input().split()))
    for i in range(len(f)):
        if f[i] == 0:
            f[i] = i+1
    for i in range(len(f)):
        if f[i] == 0:
            f[i] = i+1
    for i in range(len(f)):
        print(f[i],end=" ")

main()