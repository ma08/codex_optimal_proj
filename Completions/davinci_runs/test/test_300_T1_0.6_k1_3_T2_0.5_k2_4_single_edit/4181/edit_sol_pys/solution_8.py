

def main():
    n = int(input())
    monsters = list(map(int, input().split()))
    heroes = list(map(int, input().split()))

    print(sum(sorted(monsters, reverse=True)[:len(heroes)]))

if __name__ == '__main__':
    n = int(input())
    monsters = list(map(int, input().split()))
    heroes = list(map(int, input().split()))
    print(main(n, monsters, heroes))
