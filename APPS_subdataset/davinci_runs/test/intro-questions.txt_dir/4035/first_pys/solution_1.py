

def main():
    a, b = map(int, input().split())
    for i in range(a, b+1):
        if i*0.08 == int(i*0.08) and i*0.1 == int(i*0.1):
            print(i)
            exit()
    print(-1)

if __name__ == '__main__':
    main()