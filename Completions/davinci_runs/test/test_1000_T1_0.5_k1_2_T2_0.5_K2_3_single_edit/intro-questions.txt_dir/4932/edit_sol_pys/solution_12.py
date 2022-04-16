

import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())

    def get_dog_status(time, aggressive, calm, dog_name):
        if time == 0:
            return f'{dog_name} is aggressive'
        time -= 1
        if time < aggressive:
            return f'{dog_name} is aggressive'
        time -= aggressive
        if time < calm:
            return f'{dog_name} is calm'
        time -= calm
        return get_dog_status(time, aggressive, calm, dog_name)

    def get_dog_attack(time):
        if 'aggressive' in get_dog_status(time, A, B, 'Small') and 'aggressive' in get_dog_status(time, C, D, 'Big'):
            return 'both dogs are aggressive'
        elif 'aggressive' in get_dog_status(time, A, B, 'Small') or 'aggressive' in get_dog_status(time, C, D, 'Big'):
            return 'one dog is aggressive'
        else:
            return 'none of the dogs are aggressive'

    print(get_dog_attack(P))
    print(get_dog_attack(M))
    print(get_dog_attack(G))

if __name__ == '__main__':
    main()
