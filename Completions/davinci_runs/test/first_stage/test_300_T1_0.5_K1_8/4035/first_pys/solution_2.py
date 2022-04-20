

#1
def main():
    a, b = map(int, input().split())
    for i in range(1, 101):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            exit()
    print(-1)

if __name__ == '__main__':
    main()

#2
def main():
    a, b = map(int, input().split())
    ans = -1
    for i in range(1, 101):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            ans = i
    print(ans)

if __name__ == '__main__':
    main()