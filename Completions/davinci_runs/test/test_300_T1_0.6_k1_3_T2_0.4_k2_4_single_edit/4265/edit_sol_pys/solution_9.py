

def main():
    S = input()
    T = input()

    print(sum(1 for s, t in zip(S, T) if s != t))

if __name__ == '__main__':
    main()
