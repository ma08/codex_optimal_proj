

def main():
    S = input()
    print(len(max(S.split('ACGT'), key=len)))

if __name__ == '__main__':
    main()
