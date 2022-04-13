

def get_hand_strength(hand):  # функция возвращает максимальное количество одинаковых значений
    ranks = [card[0] for card in hand]  # получаем все значения карт в руке
    return max([ranks.count(rank) for rank in ranks])  # возвращаем максимальное количество одинаковых значений в руке

def main():
    hand = input().split()
    print(get_hand_strength(hand))  # выводим максимальное количество одинаковых значений

main()
