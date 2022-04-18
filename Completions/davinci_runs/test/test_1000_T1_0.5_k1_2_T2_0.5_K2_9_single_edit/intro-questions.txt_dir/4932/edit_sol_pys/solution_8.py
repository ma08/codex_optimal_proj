

import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    A, B, C, D = map(int, input().split())
    P, M, G = map(int, input().split())

    def get_dog_status(time, aggressive, calm):
        if time == 0:
            return 'aggressive'
        time -= 1
        if time < aggressive:
            return 'aggressive'
        time -= aggressive
        if time < calm:
            return 'calm'
        time -= calm
        return get_dog_status(time, aggressive, calm)

    def get_dog_attack(time):
        if get_dog_status(time, A, B) == 'aggressive' and get_dog_status(time, C, D) == 'aggressive':
            return 'both'
        elif get_dog_status(time, A, B) == 'aggressive' or get_dog_status(time, C, D) == 'aggressive':
            return 'one'
        else:
            return 'none'

    print(get_dog_attack(P, A, B, C, D))
    print(get_dog_attack(M, A, B, C, D))
    print(get_dog_attack(G, A, B, C, D))

if __name__ == '__main__':
    main()
