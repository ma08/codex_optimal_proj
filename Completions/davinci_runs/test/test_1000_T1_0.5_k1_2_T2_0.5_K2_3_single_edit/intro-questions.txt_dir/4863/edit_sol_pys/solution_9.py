

def main():
    n = int(input())
    correct = set()
    for i in range(n):
        correct.add(input())
    print(len(correct))

if __name__ == '__main__':
    main()
