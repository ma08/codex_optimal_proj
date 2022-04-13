import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())

    def get_dog_status(time, aggressive, calm):
        if time == 0:
            return 'A'
        time -= 1
        if time < aggressive:
            return 'A'
        time -= aggressive
        if time < calm:
            return 'C'
        time -= calm
        return get_dog_status(time, aggressive, calm)

    def get_dog_attack(time):
        if get_dog_status(time, A, B) == 'A' and get_dog_status(time, C, D) == 'A':
            return 'both are angry'
        elif get_dog_status(time, A, B) == 'A' or get_dog_status(time, C, D) == 'A':
            return 'one is angry'
        else:
            return 'none is angry'

    print(get_dog_attack(P))
    print(get_dog_attack(M))
    print(get_dog_attack(G))

if __name__ == '__main__':
    main()
