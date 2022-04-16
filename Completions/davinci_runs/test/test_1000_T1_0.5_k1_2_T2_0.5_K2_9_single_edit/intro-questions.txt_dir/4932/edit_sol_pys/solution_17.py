
import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    p, m, g = map(int, sys.stdin.readline().split())

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
        if get_dog_status(time, a, b) == 'aggressive' and get_dog_status(time, c, d) == 'aggressive':
            return 'both'
        elif get_dog_status(time, a, b) == 'aggressive' or get_dog_status(time, c, d) == 'aggressive':
            return 'one'
        else:
            return 'none'

    print(get_dog_attack(p))
    print(get_dog_attack(m))
    print(get_dog_attack(g))

if __name__ == '__main__':
    main()
