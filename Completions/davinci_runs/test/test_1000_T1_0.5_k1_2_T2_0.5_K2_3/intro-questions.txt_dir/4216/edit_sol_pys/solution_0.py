
def main():
    N = int(input()) + 1
    while True:
        if len(set(str(N))) == len(str(N)):
            print(N)
            break
        N += 1

def main():
    N = int(input())
    r = math.ceil(math.sqrt(N)) + 1
    for i in range(r, 1, -1):
        if N % i == 0:
            print(N // i // 10 ** (len(str(i)) - 1))
            break

if __name__ == '__main__':
    main()
