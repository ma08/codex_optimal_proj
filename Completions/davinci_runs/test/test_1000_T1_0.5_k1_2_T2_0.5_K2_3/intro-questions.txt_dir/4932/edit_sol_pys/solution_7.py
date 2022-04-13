

import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())

    def get_dog_status(time, agressive, calm):
        if time == 0:
            return 'aggressive'
        time -= 1
        if time < agressive:
            return 'aggressive'
        time -= agressive
        if time < calm:
            return 'calm'
        time -= calm
        return get_dog_status(time, agressive, calm)

    def get_dog_attack(time):
        if get_dog_status(time, A, B) == 'aggressive' and get_dog_status(time, C, D) == 'aggressive':
            return 'both'
        elif get_dog_status(time, A, B) == 'aggressive' or get_dog_status(time, C, D) == 'aggressive':
            return 'one'
        else:
            return 'none'

    print(get_dog_attack(P))
    print(get_dog_attack(M))
    print(get_dog_attack(G))

if __name__ == '__main__':
    main()
