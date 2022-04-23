

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    l = [A, B, C, D, E]
    l.sort()

    if N <= l[0]:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
