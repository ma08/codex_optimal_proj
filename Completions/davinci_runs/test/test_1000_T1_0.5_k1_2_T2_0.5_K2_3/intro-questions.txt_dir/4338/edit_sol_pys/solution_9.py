

def get_number_of_broken_doors(n, x, y, a, b, d):
    return


def main():
    n, x, y, d = map(int, input().split())  # число дверей, номер первой двери, номер второй двери
    a = list(map(int, input().split()))  # номера дверей, которые нужно пройти
    b = list(map(int, input().split()))  # номера дверей, которые нужно открыть
    print(get_number_of_broken_doors(n, x, y, a, b, d))


if __name__ == '__main__':
    main()
