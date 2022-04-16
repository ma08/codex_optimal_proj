

def main():
    """Ants"""
    n1 = int(input())
    n2 = int(input())
    ant1 = input()
    ant2 = input()
    time = int(input())
    if time % 2 == 0:
        print(ant1 + ant2)
    else:
        print(ant2 + ant1)

if __name__ == "__main__":
    main()
