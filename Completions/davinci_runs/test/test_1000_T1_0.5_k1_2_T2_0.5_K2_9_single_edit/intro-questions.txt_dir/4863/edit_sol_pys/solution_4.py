

def main():
    n = int(input())
    correct = ['']
    for i in range(n):
        correct.append(input().strip())
    print(n - len(set(correct)))

if __name__ == '__main__':
    main()
