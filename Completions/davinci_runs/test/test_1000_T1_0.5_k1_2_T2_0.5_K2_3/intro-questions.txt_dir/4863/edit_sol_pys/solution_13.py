

def main():
    n = int(input())
    correct = [0] * n
    wrong = [0] * n
    for i in range(n):
        correct[i] = input()

    print(correct)

if __name__ == '__main__':
    main()
