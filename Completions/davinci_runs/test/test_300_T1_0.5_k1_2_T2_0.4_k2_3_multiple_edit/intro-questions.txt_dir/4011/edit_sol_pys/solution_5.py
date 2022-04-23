

def main():
    n = int(input())
    a = input()
    t = list(map(int, input().split()))
    t = [0] + t

    for i in range(n):
        a = a.replace(str(i+1), str(t[i+1]))


    print(a)

if __name__ == '__main__':
    main()
