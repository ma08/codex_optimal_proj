import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())

    def get_dog_status(time, aggressive, calm, status):
        if status == 'aggressive':
            if time == 0:
                return 'aggressive'
            time -= 1
            if time < aggressive:
                return 'aggressive'
            time -= aggressive
            return get_dog_status(time, aggressive, calm, 'calm')
        else:
            if time == 0:
                return 'calm'
            time -= 1
            if time < calm:
                return 'calm'
            time -= calm
            return get_dog_status(time, aggressive, calm, 'aggressive')

    def get_dog_attack(time):
        if get_dog_status(time, A, B, 'aggressive') == 'aggressive' and get_dog_status(time, C, D, 'aggressive') == 'aggressive':
            return 'both'
        elif get_dog_status(time, A, B, 'aggressive') == 'aggressive' or get_dog_status(time, C, D, 'aggressive') == 'aggressive':
            return 'one'
        else:
            return 'none'

    print(get_dog_attack(P))
    print(get_dog_attack(M))
    print(get_dog_attack(G))

if __name__ == '__main__':
    main()
