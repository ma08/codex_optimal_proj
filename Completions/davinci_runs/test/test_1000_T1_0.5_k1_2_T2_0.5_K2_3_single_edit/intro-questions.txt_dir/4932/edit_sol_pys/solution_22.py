import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())

    def get_dog_status(time, aggressive_time, calm_time):
        while True:
            if time < aggressive_time:
                return 'aggressive'
            time -= aggressive_time
            if time < calm_time:
                return 'calm'
            time -= calm_time

    def get_dog_attack(time):
        if get_dog_status(time, A, B) == 'aggressive' \
                and get_dog_status(time, C, D) == 'aggressive':
            return 'both'
        elif get_dog_status(time, A, B) == 'aggressive' \
                or get_dog_status(time, C, D) == 'aggressive':
            return 'one'
        else:
            return 'none'

    print(get_dog_attack(P))
    print(get_dog_attack(M))
    print(get_dog_attack(G))

if __name__ == '__main__':
    main()
