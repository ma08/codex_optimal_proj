
import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())

    def get_dog_status(time, aggressive, calm): # 각 개의 상태를 반환하는 함수
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

    def get_dog_attack(time): # 각 시간마다 개가 공격하는지 안하는지를 반환하는 함수
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
