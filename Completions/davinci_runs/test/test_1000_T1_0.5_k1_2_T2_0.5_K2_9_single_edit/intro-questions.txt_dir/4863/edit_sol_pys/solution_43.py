

def main():
    n = int(input())
    correct = [""] * n
    for i in range(n):
        correct[i] = input()
    print(n - 1)

if __name__ == '__main__':
    main()
