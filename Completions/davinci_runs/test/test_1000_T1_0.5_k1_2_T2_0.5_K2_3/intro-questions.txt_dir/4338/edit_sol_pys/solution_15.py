

def get_number_of_broken_doors(n, x, y, a, b, c):
    return n, x, y, a, b, c


def main():
    c = list(map(int, input().split()))  # номера дверей, которые нужно закрыть
    n, x, y = map(int, input().split())  # число дверей, номер первой двери, номер второй двери
    a = list(map(int, input().split()))  # номера дверей, которые нужно пройти
    b = list(map(int, input().split()))  # номера дверей, которые нужно открыть
    print(get_number_of_broken_doors(n, x, y, a, b, c))


if __name__ == '__main__':
    main()
