

def main():
    a1, b1, a2, b2 = list(map(int, input().split()))
    a3, b3, a4, b4 = list(map(int, input().split()))
    gunnar = (b1 - a1 + 1) * (b2 - a2 + 1)
    emma = (b3 - a3 + 1) * (b4 - a4 + 1)
    if gunnar > emma:
        print('Gunnar')
    elif gunnar < emma:
        print('Emma')
    else:
        print('Tie')

if __name__ == "__main__":
    main()
