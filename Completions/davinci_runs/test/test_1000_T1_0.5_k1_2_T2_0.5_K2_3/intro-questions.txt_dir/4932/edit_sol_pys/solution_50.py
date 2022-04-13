
import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())

    def get_dog_status(time, aggressive, calm): # 강아지의 상태를 알려주는 함수
        if time == 0:
            return 'aggressive'
        time -= 1 # aggressive 단계를 제외하고 시간을 빼준다.
        if time < aggressive:
            return 'aggressive'
        time -= aggressive # calm 단계를 제외하고 시간을 빼준다.
        if time < calm:
            return 'calm'
        time -= calm # 강아지가 다시 시작하는 시점으로 간다.
        return get_dog_status(time, aggressive, calm)

    def get_dog_attack(time): # 강아지가 공격하는 여부를 알려주는 함수
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
